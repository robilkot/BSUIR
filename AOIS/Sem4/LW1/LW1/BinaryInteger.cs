using System.Collections;
using System.Text;

namespace LW1
{
    public class BinaryInteger
    {
        private BitArray _digits;

        public BinaryInteger()
        {
            _digits = new(sizeof(int) * 8);
        }
        public BinaryInteger(int decimalNumber)
        {
            int bitCount = sizeof(int) * 8;

            _digits = new BitArray(bitCount, false);

            // Set sign bit
            if (decimalNumber < 0)
            {
                _digits[0] = decimalNumber < 0;
                decimalNumber = -decimalNumber;
            }

            for (int i = 0; i < bitCount - 1; i++)
            {
                _digits[bitCount - i - 1] = decimalNumber % 2 == 1;

                decimalNumber /= 2;
            }
        }
        public BinaryInteger(BitArray digits)
        {
            _digits = digits;
        }

        public bool Positive()
        {
            return _digits[0] == false;
        }

        public int ToDecimal()
        {
            int result = 0;

            for (int i = _digits.Length - 1; i >= 1; i--)
            {
                result += _digits[i] ? (int)Math.Pow(2, _digits.Length - i - 1) : 0;
            }

            if (_digits[0])
            {
                result *= -1;
            }

            return result;
        }
        public BitArray DirectCode()
        {
            return (BitArray)_digits.Clone();
        }
        public BitArray AdditionalCode()
        {
            if (_digits[0])
            {
                var result = InvertCode();

                var bitCount = _digits.Length;

                for (int i = bitCount - 1; i > 1; i--)
                {
                    if (result[i] == false)
                    {
                        result[i] = true;
                        break;
                    }
                    else
                    {
                        result[i] = false;
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
            var result = (BitArray)_digits.Clone();

            if (_digits[0])
            {
                result = result.Not();

                // Preserve sign bit
                result[0] = !result[0];
            }

            return result;
        }

        public static BinaryInteger operator +(BinaryInteger first, BinaryInteger second)
        {
            if (first._digits[0])
            {
                first = new(first.AdditionalCode());
            }
            if (second._digits[0])
            {
                second = new(second.AdditionalCode());
            }

            BinaryInteger answer = new();

            bool carry = false;

            for (int i = first._digits.Length - 1; i >= 0; i--)
            {
                answer._digits[i] = first._digits[i] ^ second._digits[i];

                if (carry)
                {
                    answer._digits[i] = !answer._digits[i];
                }

                carry = (
                    (first._digits[i] && second._digits[i]) ||
                    (first._digits[i] ^ second._digits[i] && carry) 
                    );
            }

            if (answer._digits[0])
            {
                answer._digits = answer.AdditionalCode();
            }

            return answer;
        }

        public static BinaryInteger operator *(BinaryInteger first, BinaryInteger second)
        {
            BinaryInteger answer = new();

            var signBit = first._digits[0];
            var arrayToShift = first.DirectCode();
            int shiftingAmount = 0;

            for(int i = 1; i < second._digits.Length; i++)
            {
                if (second._digits[second._digits.Length - i])
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

            if(first.Positive() ^ second.Positive())
            {
                answer._digits[0] = true;
            }

            return answer;
        }
    }
}