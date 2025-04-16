using System.Collections.Generic;

namespace SentenceAnalysisClient.Model
{
    public record TokenDto(int id, int start_idx, int end_idx, MorphologyDto? morphology, SyntaxDto? syntax, SemanticsDto? semantics);
    public record TextRequest(string Text);
    public record SentenceRequest(string Text);

    public record SentenceResponse(string Text, List<TokenDto> Tokens);
    public record SentencesResponse(List<SentenceResponse> Sentences);

    public record SyntaxDto(string id, string head_id, SyntaxRole relation);
    public record SyntaxResponse(List<SyntaxDto> Tokens);

    public record MorphologyDto(PartOfSpeech pos, string lemma, Dictionary<string, string> morph_info);
    public record MorphologyResponse(List<MorphologyDto> Tokens);

    public record SemanticsDto();
    public record SemanticsResponse(List<Semantics> Tokens);
}
