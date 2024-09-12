using LW1;

const int Frequency = 16;

var data = Fourier.GetDiscreteValues(Math.Cos, Frequency, 0, 4 * Math.PI);
Console.WriteLine("\n\nSource:");
data.ForEach(x => Console.WriteLine(x));

Console.WriteLine("\nProcessed:");
var processed = Fourier.FFT(data);
processed.ForEach(x => Console.WriteLine(x.Real));

var data2 = Fourier.GetDiscreteValues(Math.Sin, Frequency, 0, 4 * Math.PI);
Console.WriteLine("\n\nSource:");
data2.ForEach(x => Console.WriteLine(x));

Console.WriteLine("\nProcessed:");
var processed2 = Fourier.FFT(data2);
processed2.ForEach(x => Console.WriteLine(x.Real));
