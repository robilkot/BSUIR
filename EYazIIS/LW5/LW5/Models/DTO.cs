using System;
using System.Collections.Generic;

namespace LW5.Models
{
    public record Message(
        MessageContent Content,
        MessageMetadata Metadata,
        MessageReactions? Reactions
        );

    public record MessageContent(
        List<string> Images,
        List<string> Links,
        string? Text
        );

    public record MessageMetadata(
        DateTimeOffset Sent,
        User Sender
        );

    public record MessageReactions(
        MessageRating Rating
        );

    public record User(
        string Name,
        string About
        );

    public record RateMessageRequest(
        Message Message,
        MessageRating Rating
        );
}
