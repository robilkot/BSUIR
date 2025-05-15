import json

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import uuid
import logging
import shutil

from fastapi.openapi.utils import get_openapi

from api.chroma_utils import *
from api.cinema_utils import get_image_url_by_query, get_search_result_url
from api.db_utils import *
from api.langchain_utils import *
from api.pydantic_models import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s %(asctime)s %(name)s - %(message)s", "%H:%M:%S")

file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Cinema dialog system API",
        version="1.0.0",
        description="API for dialog with AI",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    port = int(os.getenv("API_PORT", "8000"))
    logger.info(f"Documentation available at http://127.0.0.1:{port}/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=port)



@app.post("/chat",
          response_model=ChatResponse)
def send_message(request: ChatRequest):
    metadata = MessageMetadata(
        sent=datetime.now(),
        sender=User(
            name='Кинопомощник',
            about='Помогаю познать мир кино'
        )
    )
    reactions = MessageReactions(
        rating=0
    )
    msg: Message

    if request.message.content.text == 'test':
        msg = Message(
            content=MessageContent(
                images=[],
                links=[],
                text='test response',
            ),
            metadata=metadata,
            reactions=reactions
        )
        return ChatResponse(message=msg, session_id=request.session_id)

    session_id = request.session_id or str(uuid.uuid4())

    chat_history = get_chat_history(session_id)
    rag_chain = get_analysis_rag_chain()

    max_retry_count = 1
    retry_count = 0
    while retry_count < max_retry_count:
        try:
            answer = rag_chain.invoke({
                "input": request.message.content.text,
                "user_name": request.message.metadata.sender.name,
                "user_about": request.message.metadata.sender.about,
                "time": request.message.metadata.sent,
                "chat_history": chat_history
            })['answer']

            logger.debug(answer)
            # markdown stuff
            summary_str = answer
            summary_str = str.replace(summary_str, '```json', '')
            summary_str = str.replace(summary_str, '```', '')
            summary = json.loads(summary_str)

            # generate links and urls
            film_names = summary['film_names']
            people = summary['people']
            text = summary['text']
            break
        except Exception as e:
            logger.error(f'{e}')
            logger.warning("error formatting llm response, retrying")
            logger.warning(summary_str)
            retry_count += 1

    if retry_count >= max_retry_count:
        msg = Message(
            content=MessageContent(
                images=[],
                links=[],
                text=summary_str,
            ),
            metadata=metadata,
            reactions=reactions
        )
    else:
        related_image_url = get_image_url_by_query(film_names[0]) if len(film_names) > 0 else None

        links = [get_search_result_url(query) for query in (people + film_names)[:3]]

        if related_image_url is None:
            related_image_url = get_image_url_by_query(people[0]) if len(people) > 0 else None

        msg = Message(
            content=MessageContent(
                images=[related_image_url] if related_image_url else [],
                links=links,
                text=text,
            ),
            metadata=metadata,
            reactions=reactions
        )

    insert_application_logs(session_id, request.message.content.text, answer)
    return ChatResponse(message=msg, session_id=session_id)



@app.post("/context/files")
def upload_file(file: UploadFile = File(...)):
    allowed_extensions = ['.pdf', '.docx', '.html']
    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400,
                            detail=f"Unsupported file type. Allowed types are: {', '.join(allowed_extensions)}")

    temp_file_path = f"temp_{file.filename}"

    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        file_id = insert_document_record(file.filename)
        success = index_document_to_chroma(temp_file_path, file_id)

        if success:
            return {"message": f"File {file.filename} has been successfully uploaded and indexed.", "file_id": file_id}
        else:
            delete_document_record(file_id)
            raise HTTPException(status_code=500, detail=f"Failed to index {file.filename}.")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


@app.get("/context/files",
         response_model=list[DocumentInfo])
def list_files():
    return get_all_documents()


@app.delete("/context/files/{id}")
def delete_requirements(file_id: int):
    chroma_delete_success = delete_doc_from_chroma(file_id)

    if chroma_delete_success:
        db_delete_success = delete_document_record(file_id)
        if db_delete_success:
            return {"message": f"Successfully deleted document with id {file_id} from the system."}
        else:
            return {
                "error": f"Deleted from Chroma but failed to delete document with id {file_id} from the database."}
    else:
        return {"error": f"Failed to delete document with id {file_id} from Chroma."}
