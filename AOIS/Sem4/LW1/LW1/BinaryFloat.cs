namespace LW1;
using System;
using System.Collections;

public class BinaryFloat
{
    private bool[] bits;

    public BinaryFloat(float value)
    {
        int intValue = BitConverter.ToInt32(BitConverter.GetBytes(value), 0);
        bits = new bool[32];

        for (int i = 0; i < 32; i++)
        {
            bits[i] = (intValue & (1 << (31 - i))) != 0;
        }
    }

    public float ToFloat()
    {
        int intValue = 0;
        for (int i = 0; i < 32; i++)
        {
            if (bits[i])
                intValue |= 1 << (31 - i);
        }
        return BitConverter.ToSingle(BitConverter.GetBytes(intValue), 0);
    }

    public static BinaryFloat operator +(BinaryFloat a, BinaryFloat b)
    {
        // Check if only sign differs
        a.bits[0] = !a.bits[0];
        bool sequenceEquals = a.bits.SequenceEqual(b.bits);
        a.bits[0] = !a.bits[0];

        if (sequenceEquals)
        {
            return new BinaryFloat(0);
        }

        var resultBits = new bool[32];

        int exponentA = 0;
        int exponentB = 0;
        int mantissaA = 0;
        int mantissaB = 0;

        for (int i = 1; i <= 8; i++)
        {
            exponentA |= (a.bits[i] ? 1 : 0) << (8 - i);
            exponentB |= (b.bits[i] ? 1 : 0) << (8 - i);
        }
        for (int i = 9; i <= 31; i++)
        {
            mantissaA |= (a.bits[i] ? 1 : 0) << (31 - i);
            mantissaB |= (b.bits[i] ? 1 : 0) << (31 - i);
        }

        mantissaA |= 1 << 23;
        mantissaB |= 1 << 23;

        int resultExponent = Math.Max(exponentA, exponentB);

        // Shift mantissas if necessary
        mantissaA >>= resultExponent - exponentA;
        mantissaB >>= resultExponent - exponentB;

        int resultMantissa = (a.bits[0] ? -mantissaA : mantissaA) + (b.bits[0] ? -mantissaB : mantissaB);

        if (resultMantissa < 0)
        {
            resultBits[0] = true;
            resultMantissa = -resultMantissa;
        }

        // Normalize the mantissa
        while (resultMantissa >= (1 << 23))
        {
            resultMantissa >>= 1;
            resultExponent++;
        }

        if (resultMantissa != 0)
        {
            while (resultMantissa < (1 << 23))
            {
                resultMantissa <<= 1;
                resultExponent--;
            }
        }

        for (int i = 1; i <= 8; i++)
        {
            resultBits[i] = ((resultExponent >> (8 - i)) & 1) == 1;
        }

        for (int i = 9; i <= 31; i++)
        {
            resultBits[i] = ((resultMantissa >> (31 - i)) & 1) == 1;
        }

        return new BinaryFloat(0) { bits = resultBits };
    }

    public BitArray ToBitArray()
    {
        return new BitArray(bits);
    }
}