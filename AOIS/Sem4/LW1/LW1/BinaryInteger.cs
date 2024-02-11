using System.Collections;

namespace LW1;
public class BinaryInteger
{
    private BitArray _bits = new(sizeof(int) * 8);

    public BinaryInteger() { }
    public BinaryInteger(int decimalNumber)
    {
        int bitCount = _bits.Length;
        // Set sign bit
        if (decimalNumber < 0)
        {
            _bits[0] = decimalNumber < 0;
            decimalNumber = -decimalNumber;
        }

        for (int i = 0; i < bitCount - 1; i++)
        {
            _bits[bitCount - i - 1] = decimalNumber % 2 == 1;

            decimalNumber /= 2;
        }
    }
    public BinaryInteger(BitArray digits)
    {
        _bits = digits;
    }

    public bool Positive()
    {
        return !_bits[0];
    }

    public int ToDecimal()
    {
        int result = 0;

        for (int i = _bits.Length - 1; i >= 1; i--)
        {
            result += _bits[i] ? 1 << (_bits.Length - i - 1) : 0;
        }

        if (!Positive())
        {
            result *= -1;
        }

        return result;
    }
    public BitArray DirectCode()
    {
        return (BitArray)_bits.Clone();
    }
    public BitArray AdditionalCode()
    {
        if (!Positive())
        {
            var result = InvertCode();

            var bitCount = _bits.Length;

            // Add one to the number
            for (int i = bitCount - 1; i > 1; i--)
            {
                // Adding a bit means changing inverting value
                result[i] = !result[i];

                // If changed value was 0, no need update bits on left side from it
                if (result[i])
                {
                    break;
                }
            }

            return result;
        }
        else
        {
            return DirectCode();
        }
    }
    public BitArray InvertCode()
    {
        var result = (BitArray)_bits.Clone();

        if (!Positive())
        {
            result = result.Not();

            // Preserve sign bit
            result[0] = !result[0];
        }

        return result;
    }

    public static BinaryInteger operator +(BinaryInteger first, BinaryInteger second)
    {
        first._bits = first.AdditionalCode();
        second._bits = second.AdditionalCode();

        BinaryInteger answer = new();

        bool carry = false;

        for (int i = first._bits.Length - 1; i >= 0; i--)
        {
            answer._bits[i] = first._bits[i] ^ second._bits[i] ^ carry;

            carry = (
                (first._bits[i] && second._bits[i]) ||
                (first._bits[i] ^ second._bits[i] && carry)
                );
        }

        if (!answer.Positive())
        {
            answer._bits = answer.AdditionalCode();
        }

        return answer;
    }

    public static BinaryInteger operator *(BinaryInteger first, BinaryInteger second)
    {
        BinaryInteger answer = new();

        var signBit = first._bits[0];
        var arrayToShift = first.DirectCode();
        int shiftingAmount = 0;

        for (int i = 1; i < second._bits.Length; i++)
        {
            if (second._bits[second._bits.Length - i])
            {
                var shifted = arrayToShift.RightShift(shiftingAmount);
                shifted[0] = signBit;
                shiftingAmount = 1;
                answer += new BinaryInteger(shifted);
            }
            else
            {
                shiftingAmount++;
            }
        }

        answer._bits[0] = first.Positive() ^ second.Positive();

        return answer;
    }
}