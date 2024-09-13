using LW3;
using System.Drawing;

#pragma warning disable CA1416

const string sourceFileName = "white";
const string targetFileName = "black";

Bitmap source = new($"{sourceFileName}.png");
Bitmap target = new($"{targetFileName}.png");

var processed = source.EqualizeBrightness(target);

processed.Save($"{sourceFileName}_equalized.png");
