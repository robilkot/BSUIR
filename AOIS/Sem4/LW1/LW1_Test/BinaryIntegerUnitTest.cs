using LW1;
using System.Collections;
using System.Numerics;

namespace LW1_Test
{
    public class BinaryIntegerUnitTest
    {
        [Fact]
        public void BinaryInteger_InitializeWithEmptyArray_ShouldBePositive()
        {
            BinaryInteger integer = new(new BitArray(5, false));

            var result = integer.Positive();

            Assert.True(result);
        }

        [Fact]
        public void BinaryInteger_InitializeEmpty_ShouldBePositive()
        {
            BinaryInteger integer = new();

            var result = integer.Positive();

            Assert.True(result);
        }

        [Theory]
        [InlineData(10)]
        [InlineData(25)]
        [InlineData(0)]
        [InlineData(-10)]
        [InlineData(-25)]
        public void BinaryInteger_InitializeWithNumber_DecimalRepresentationShouldEqual(int input)
        {
            BinaryInteger integer = new(input);

            var result = integer.ToDecimal();

            Assert.Equal(input, result);
        }

        [Theory]
        [InlineData(0, 5, 5)]
        [InlineData(5, 0, 5)]
        [InlineData(-15, 22, 7)]
        [InlineData(22, -15, 7)]
        [InlineData(-55, 55, 0)]
        [InlineData(55, -55, 0)]
        public void BinaryInteger_Addition_ResultShouldEqualExpected(int val1, int val2, int result)
        {
            BinaryInteger integer1 = new(val1);
            BinaryInteger integer2 = new(val2);

            var integer3 = integer1 + integer2;

            Assert.Equal(result, integer3.ToDecimal());
        }

        [Theory]
        [InlineData(0, 5, 0)]
        [InlineData(5, 0, 0)]
        [InlineData(-15, 22, -330)]
        [InlineData(22, -15, -330)]
        [InlineData(-55, 55, -3025)]
        [InlineData(55, -55, -3025)]
        [InlineData(12, 10, 120)]
        [InlineData(10, 12, 120)]
        public void BinaryInteger_Multiplication_ResultShouldEqualExpected(int val1, int val2, int result)
        {
            BinaryInteger integer1 = new(val1);
            BinaryInteger integer2 = new(val2);

            var integer3 = integer1 * integer2;

            Assert.Equal(result, integer3.ToDecimal());
        }
    }
}