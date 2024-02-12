using LW1;
using System.Collections;
using System.Diagnostics.CodeAnalysis;
using System.Numerics;

namespace LW1_Test
{
    [ExcludeFromCodeCoverage]
    public class BinaryFloatUnitTest
    {
        [Theory]
        [InlineData(10.2f)]
        [InlineData(25.234f)]
        [InlineData(0.12f)]
        [InlineData(-10.238f)]
        [InlineData(-25.853f)]
        public void BinaryFloat_InitializeWithFloat_FloatRepresentationShouldEqual(float input)
        {
            BinaryFloat integer = new(input);

            var result = integer.ToFloat();

            Assert.Equal(input, result);
        }

        [Theory]
        [InlineData(1.7f, 2.5f, 4.2f)]
        [InlineData(0.2f, 4.8f, 5f)]
        [InlineData(5.2f, -5.2f, 0f)]
        [InlineData(250.23f, -128.12f, 122.11f)]
        public void BinaryFloat_Addition_ResultShouldEqualExpected(float val1, float val2, float result)
        {
            BinaryFloat float1 = new(val1);
            BinaryFloat float2 = new(val2);

            BinaryFloat float3 = float1 + float2;

            Assert.Equal(result, float3.ToFloat());
        }
    }
}