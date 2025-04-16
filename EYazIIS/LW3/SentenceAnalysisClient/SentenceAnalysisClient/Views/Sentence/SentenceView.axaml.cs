using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Shapes;
using Avalonia.Media;
using SentenceAnalysisClient.ViewModels;
using System;
using System.Linq;
using System.Reactive.Linq;

namespace SentenceAnalysisClient.Views.Sentence;

public partial class SentenceView : UserControl
{
    public static readonly DirectProperty<SentenceView, double> SyntaxArrowsHeightProperty =
        AvaloniaProperty.RegisterDirect<SentenceView, double>(nameof(SyntaxArrowsHeight), o => o.SyntaxArrowsHeight);

    private double _syntaxArrowsHeight = 20;
    public double SyntaxArrowsHeight
    {
        get { return _syntaxArrowsHeight; }
        private set { SetAndRaise(SyntaxArrowsHeightProperty, ref _syntaxArrowsHeight, value); }
    }

    private double _baseSyntaxArrowsHeight = 20;
    private double _syntaxArrowOffset = 2;
    private double _syntaxArrowsHeightMultiplier = 1;

    public SentenceView()
    {
        InitializeComponent();

        AttachedToVisualTree += OnAttachedToVisualTree;
        DetachedFromVisualTree += OnDetachedFromVisualTree;

        TokenItems.Items.CollectionChanged += TokenItems_ItemsChanged;
    }

    private void TokenItems_ItemsChanged(object? sender, EventArgs e)
    {
        _syntaxArrowsHeightMultiplier = Math.Max(1d, TokenItems.ItemCount / 5d);

        SyntaxArrowsHeight = _baseSyntaxArrowsHeight * _syntaxArrowsHeightMultiplier + _syntaxArrowOffset;
    }

    protected override void OnDataContextChanged(EventArgs e)
    {
        base.OnDataContextChanged(e);

        if (DataContext is not SentenceViewModel viewModel)
            return;
    }

    private void OnAttachedToVisualTree(object? sender, VisualTreeAttachmentEventArgs e)
    {
        TokenItems.EffectiveViewportChanged += OnLayoutUpdated;
    }

    private void OnDetachedFromVisualTree(object? sender, VisualTreeAttachmentEventArgs e)
    {
        TokenItems.EffectiveViewportChanged -= OnLayoutUpdated;
    }

    private void OnLayoutUpdated(object? sender, EventArgs e)
    {
        DrawArrows();
    }

    private void DrawArrows()
    {
        if (DataContext is not SentenceViewModel viewModel)
            return;

        ArrowCanvas.Children.Clear();

        var tokenToControl = TokenItems.ItemsPanelRoot?
            .Children
            .ToDictionary(x => (SentenceTokenViewModel)x.DataContext!, x => x) ?? [];

        foreach (var token in viewModel.Tokens)
        {
            var syntax = token.Syntax;
            if (syntax?.HeadToken == null 
                || !tokenToControl.ContainsKey(token) 
                || !tokenToControl.ContainsKey(syntax.HeadToken)
                || syntax.Token == syntax.HeadToken
                || syntax.Relation == Model.GrammaticalRelation.Punct)
                continue;

            var from = tokenToControl[syntax.HeadToken];
            var to = tokenToControl[token];

            var fromCenter = from.Bounds.Center;
            var toCenter = to.Bounds.Center;

            fromCenter = TokenItems.TranslatePoint(fromCenter, ArrowCanvas).Value;
            toCenter = TokenItems.TranslatePoint(toCenter, ArrowCanvas).Value;

            var fromPoint = fromCenter.WithY(fromCenter.Y - from.Bounds.Height / 2 - _syntaxArrowOffset);
            var toPoint = toCenter.WithY(toCenter.Y - to.Bounds.Height / 2 - _syntaxArrowOffset);

            var path = CreateArrowPath(fromPoint, toPoint);
            ArrowCanvas.Children.Add(path);
        }
    }

    private Path CreateArrowPath(Point start, Point end)
    {
        var geometry = new StreamGeometry();

        using (var context = geometry.Open())
        {
            context.BeginFigure(start, false);
            context.QuadraticBezierTo(new Point((start.X + end.X) / 2, -SyntaxArrowsHeight / 2), end);

            var angle = Math.Atan2(end.Y, end.X - (start.X + end.X) / 2);
            var headLength = _baseSyntaxArrowsHeight / 2;
            var arrowP1 = new Point(
                end.X - headLength * Math.Cos(angle - Math.PI / 6),
                end.Y - headLength * Math.Sin(angle - Math.PI / 6));
            var arrowP2 = new Point(
                end.X - headLength * Math.Cos(angle + Math.PI / 6),
                end.Y - headLength * Math.Sin(angle + Math.PI / 6));

            context.BeginFigure(end, false);
            context.LineTo(arrowP1);
            context.BeginFigure(end, false);
            context.LineTo(arrowP2);
        }

        return new Path
        {
            Data = geometry,
            Stroke = Brushes.White,
            StrokeThickness = 1.5
        };
    }
}
