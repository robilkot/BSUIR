using LW5.Models;
using ReactiveUI;
using System;
using System.Reactive;
using System.Threading.Tasks;

namespace LW5.ViewModels.Messages;

public class MessageReactionsViewModel : MessageViewModel
{
    private MessageRating _rating;
    public MessageRating Rating
    {
        get => _rating;
        private set => this.RaiseAndSetIfChanged(ref _rating, value);
    }

    public ReactiveCommand<MessageRating, Unit> SetRatingCommand;

    public MessageReactionsViewModel()
    {
        var canSetRating = this.WhenAny(
            r => r.Rating,
            rating => rating.Value == MessageRating.None
            );

        SetRatingCommand = ReactiveCommand.CreateFromTask<MessageRating>(SetRating, canSetRating);
    }

    public Task SetRating(MessageRating rating)
    {
        if (Rating is not MessageRating.None)
            throw new NotSupportedException();

        // todo

        return Task.CompletedTask;
    }
}
