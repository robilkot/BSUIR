using System.Collections.Generic;
using System.Linq;


namespace SentenceAnalysisClient.Model
{
#pragma warning disable IDE1006 // Naming Styles
    public record TokenDto(int id, int start_idx, int end_idx, MorphologyDto? morphology, SyntaxDto? syntax, SemanticsDto? semantics);
    public record TextRequest(string text);
    public record SentenceRequest(string text);

    public record SentenceResponse(string text, List<TokenDto> tokens);
    public record SentencesResponse(List<SentenceResponse> sentences);

    public record SyntaxDto(string id, string head_id, SyntaxRole relation);
    public record SyntaxResponse(List<SyntaxDto> tokens);

    public record MorphologyDto(PartOfSpeech pos, string lemma, Dictionary<string, string> morph_info);
    public record MorphologyResponse(List<MorphologyDto> tokens);


    public record SemanticsDto(NamedEntityDto? named_entity_info, ObjectDescriptionDto? object_description);
    public record NamedEntityDto(string text, NERClass ner_class, string? normal_form);
    public record ObjectDescriptionDto(string text, int emphasis, string description, List<string>? images_urls);
    public record SemanticsResponse(List<SemanticsDto> tokens);

    public static class DtoExtensions
    {
    }
#pragma warning restore IDE1006 // Naming Styles
}
