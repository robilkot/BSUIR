using Avalonia.Collections;
using Avalonia.Controls;
using Avalonia.Controls.Shapes;
using Avalonia.Media;
using SentenceAnalysisClient.Model;
using SentenceAnalysisClient.ViewModels;
using System;
using System.Collections.Generic;

namespace SentenceAnalysisClient.Views.Sentence;

public partial class TokenSyntaxView : UserControl
{
    private SentenceTokenViewModel? vm;

    public TokenSyntaxView()
    {
        InitializeComponent();

        Loaded += (_, _) => DrawLine();
        DataContextChanged += TokenSyntaxView_DataContextChanged;
    }

    private void TokenSyntaxView_DataContextChanged(object? sender, EventArgs e)
    {
        if (DataContext is not SentenceTokenViewModel viewmodel)
        {
            if (vm is not null)
            {
                vm.PropertyChanged -= SyntaxPropertyChanged;
            }
            return;
        }

        vm = viewmodel;
        vm.PropertyChanged += SyntaxPropertyChanged;

        DrawLine();
    }

    private void SyntaxPropertyChanged(object? sender, System.ComponentModel.PropertyChangedEventArgs e)
    {
        DrawLine();
    }

    private void OnRedrawNeeded(object? sender, System.EventArgs e)
    {
        DrawLine();
    }

    private record LineParams(IBrush Brush, double Thickness, bool Double = false, AvaloniaList<double>? StrokeDashArray1 = null, AvaloniaList<double>? StrokeDashArray2 = null);

    private void DrawLine()
    {
        if (vm is not null && vm.Syntax is not null)
        {
            var lineParams = GetLine(vm.Syntax.Relation);

            if (lineParams != null)
            {
                Underline1.Stroke = lineParams.Brush;
                Underline1.StrokeThickness = lineParams.Thickness;
                Underline1.StartPoint = new(TokenBorder.Bounds.Left, lineParams.Thickness);
                Underline1.EndPoint = new(TokenBorder.Bounds.Right, lineParams.Thickness);
                Underline1.StrokeDashArray = lineParams.StrokeDashArray1;

                if (lineParams.Double)
                {
                    Underline2.Stroke = lineParams.Brush;
                    Underline2.StrokeThickness = lineParams.Thickness;
                    Underline2.StartPoint = new(TokenBorder.Bounds.Left, lineParams.Thickness);
                    Underline2.EndPoint = new(TokenBorder.Bounds.Right, lineParams.Thickness);
                    Underline2.StrokeDashArray = lineParams.StrokeDashArray2;
                    Underline2.StrokeDashOffset = lineParams.StrokeDashArray1 is not null ? lineParams.StrokeDashArray1[0] : 0;
                }
            }
        }
    }

    private static LineParams? GetLine(SyntaxRole relation) => relation switch
    {
        SyntaxRole.Root or SyntaxRole.Xcomp or SyntaxRole.Acl or SyntaxRole.Ccomp or SyntaxRole.Conj => new(Brushes.White, 2, true), // Сказуемое

        SyntaxRole.Nsubj => new(Brushes.White, 2, false), // Подлежащее

        SyntaxRole.Obj or SyntaxRole.Iobj or SyntaxRole.Obl or SyntaxRole.Nmod => new(Brushes.White, 2, false, [6, 1.5]), // Дополнение

        SyntaxRole.Amod or SyntaxRole.Det => new(Brushes.White, 2, true, [1.5, 1.5], [1.5, 1.5]), // Определение

        SyntaxRole.Advmod => new(Brushes.White, 2, false, [6, 1.5, 1, 1.5]), // Обстоятельство

        _ => null
    };
}