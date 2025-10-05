from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

from api.chroma_utils import vectorstore

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

analysis_prompt = ChatPromptTemplate.from_messages([
    ("system", "Ты ассистент, помогающий человеку узнать больше о фильмах и кино.\n"
               "Отвечай строго в формате json: в поле text твой ответ, в поле film_names список фильмов из твоего ответа, "
               "в поле people список упомянутых имён людей из твоего ответа. "
               "Текстовый ответ должен быть в формате plain text, без использования markdown.\n"
               "Учти предпочтения человека: его зовут {user_name}, описание его профиля: {user_about}.\n"
               "Время сейчас {time}, если это поможет определить настрой пользователя.\n"
               "Отказывайся отвечать на любые вопросы кроме кино.\n"),
    ("system", "Контекст: {context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])


def get_analysis_rag_chain():
    llm = ChatOllama(model='gemma3:1b', temperature=0.1)
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, analysis_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    return rag_chain
