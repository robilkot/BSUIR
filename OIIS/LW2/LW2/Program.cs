using LW2;
using System.Drawing;

#pragma warning disable CA1416

const int Diameter = 5;
const string FileName = "test";

Bitmap test = new($"{FileName}.png");

var processed = test.MedianFilter(diameter: Diameter);

processed.Save($"{FileName}_median_d{Diameter}.png");

