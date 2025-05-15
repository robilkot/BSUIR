using System;
using System.Collections.Generic;

namespace LW5.Models
{
    public record ChatRequest(
        string? session_id,
        Message message
        );

    public record ChatResponse(
        string session_id,
        Message message
        );

    public record Message(
        MessageContent content,
        MessageMetadata metadata,
        MessageReactions? reactions
        );

    public record MessageContent(
        List<string> images,
        List<string> links,
        string? text
        );

    public record MessageMetadata(
        DateTimeOffset sent,
        User sender
        );

    public record MessageReactions(
        MessageRating rating
        );

    public record User(
        string name,
        string about
        );

    public record RateMessageRequest(
        Message Message,
        MessageRating Rating
        );
}
