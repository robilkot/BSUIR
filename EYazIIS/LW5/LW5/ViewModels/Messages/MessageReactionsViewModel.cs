using LW5.Models;
using ReactiveUI;
using System;
using System.Reactive;
using System.Threading.Tasks;

namespace LW5.ViewModels.Messages;

public class MessageReactionsViewModel : MessageViewModel
{
    private MessageRating _rating = MessageRating.None;
    public MessageRating Rating
    {
        get => _rating;
        private set => this.RaiseAndSetIfChanged(ref _rating, value);
    }

    public ReactiveCommand<MessageRating, Unit> SetRatingCommand { get; }

    public MessageReactionsViewModel()
    {
        SetRatingCommand = ReactiveCommand.CreateFromTask<MessageRating>(
            SetRating,
            this.WhenAny(
                x => x.Rating,
                rating => rating.Value == MessageRating.None
            )
        );
    }

    public Task SetRating(MessageRating rating)
    {
        if (Rating is not MessageRating.None)
            throw new NotSupportedException();

        // todo
        Rating = rating;

        return Task.CompletedTask;
    }
}
