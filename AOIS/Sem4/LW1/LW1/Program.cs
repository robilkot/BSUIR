using LW1;
using System.Diagnostics.CodeAnalysis;
using static LW1.Helper;


//BinaryFloat fa = new(ReadFloat());

//ShowDetails(fa);

//BinaryFloat fb = new(ReadFloat());

//ShowDetails(fb);

//BinaryFloat fc = fa + fb;

//ShowDetails(fc);

BinaryFloat float1 = new(1.5f);
BinaryFloat float2 = new(3.5f);

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