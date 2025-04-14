using System.Collections.Generic;

namespace SentenceAnalysisClient.Model
{

    public record SentenceRequest(string Text, List<TokenDto> Tokens);

    public record TokenDto(int start_idx, int end_idx, PartOfSpeech? pos, string? lemma, Dictionary<string, string>? morph_info);

    public record SyntaxResponse(List<SyntaxTokenResponse> Tokens);
    public record SyntaxTokenResponse(string id, string head_id, string relation);
    public record SemanticsResponse;
    public record SentencesResponse(List<SentenceResponse> Sentences);
    public record SentenceResponse(string Text, List<TokenDto> Tokens, SyntaxResponse? Syntax, SemanticsResponse? Semantics);
}
