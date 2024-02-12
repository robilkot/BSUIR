using LW1;
using System.Diagnostics.CodeAnalysis;
using static LW1.Helper;


BinaryFloat float1 = new(ReadFloat());

ShowDetails(float1);

BinaryFloat float2 = new(ReadFloat());

ShowDetails(float2);

BinaryFloat float3 = float1 + float2;

ShowDetails(float3);


//BinaryInteger a = new(ReadInt());

//ShowDetails(a);

//BinaryInteger b = new(ReadInt());

//ShowDetails(b);

//BinaryInteger c = a * b;

//ShowDetails(c);

[ExcludeFromCodeCoverage]
public partial class Program { }