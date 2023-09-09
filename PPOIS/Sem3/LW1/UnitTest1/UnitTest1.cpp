#include "CppUnitTest.h"
#include "../CantorSet.h"

using std::string;
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace Microsoft {
	namespace VisualStudio {
		namespace CppUnitTestFramework {
			template <> static std::wstring ToString(const CantorSet& set)
			{
				string converted = set.toString();
				return std::wstring(converted.begin(), converted.end());
			}
		}
	}
}

namespace CantorSetUnitTest
{
	TEST_CLASS(CantorSetCreation)
	{
	public:
		TEST_METHOD(empty)
		{
			CantorSet testSet;

			Assert::IsTrue(testSet.empty());
			Assert::AreEqual((size_t) 0, testSet.cardinality());
		}
		TEST_METHOD(singleElement)
		{
			CantorSet testSet('a');

			Assert::AreEqual((string)"a", testSet.toString());
			Assert::AreEqual((size_t)0, testSet.cardinality());
		}
		TEST_METHOD(multipleElements)
		{
			string expectedSet = "{a,b,c}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
			Assert::AreEqual((size_t)3, testSet.cardinality());
		}

		TEST_METHOD(subset)
		{
			string expectedSet = "{a,b,{c,d}}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
			Assert::AreEqual((size_t)3, testSet.cardinality());
		}
		TEST_METHOD(multipleSubsets)
		{
			string expectedSet = "{a,b,{c,d},{e,f}}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
			Assert::AreEqual((size_t)4, testSet.cardinality());
		}
		TEST_METHOD(nestedSubsets)
		{
			string expectedSet = "{a,{{e,f}},{d,{c}}}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
			Assert::AreEqual((size_t)3, testSet.cardinality());
		}
		TEST_METHOD(nestedSubsets_char)
		{
			const char* const expectedSet = "{a,{{e,f}},{d,{c}}}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(string(expectedSet), testSet.toString());
			Assert::AreEqual((size_t)3, testSet.cardinality());
		}
		TEST_METHOD(invalidSetTest)
		{
			string expectedSet = "{{{e,f}";
			
			auto func = [&] { CantorSet testSet(expectedSet); };
			Assert::ExpectException<std::invalid_argument>(func);
		}
	};

	TEST_CLASS(CantorSetModification)
	{
	public:
		TEST_METHOD(pushEmpty)
		{
			string expectedSet = "{{}}";
			CantorSet testSet;

			testSet.push();

			Assert::IsFalse(testSet.empty());
			Assert::AreEqual((size_t)1, testSet.cardinality());
			Assert::AreEqual(expectedSet, testSet.toString());
		}
		TEST_METHOD(pushElement)
		{
			string expectedSet = "{a,b}";
			CantorSet testSet;

			testSet.push('a');
			testSet.push("b");

			Assert::IsFalse(testSet.empty());
			Assert::AreEqual((size_t)2, testSet.cardinality());
			Assert::AreEqual(expectedSet, testSet.toString());
		}
		TEST_METHOD(pushString)
		{
			string expectedSet = "{a,b,{c,d}}";
			CantorSet testSet("{a,b}");
			
			testSet.push("{c,d}");

			Assert::AreEqual((size_t)3, testSet.cardinality());
			Assert::AreEqual(expectedSet, testSet.toString());
		}
		TEST_METHOD(pushString_char)
		{
			const char* const expectedSet = "{a,b,{c,d}}";
			CantorSet testSet("{a,b}");

			testSet.push("{c,d}");

			Assert::AreEqual((size_t)3, testSet.cardinality());
			Assert::AreEqual(string(expectedSet), testSet.toString());
		}
		TEST_METHOD(pushSet)
		{
			string expectedSet = "{a,b,{c,d}}";
			CantorSet testSet("{a,b}");
			CantorSet testSet2("{c,d}");

			testSet.push(testSet2);

			Assert::AreEqual((size_t)3, testSet.cardinality());
			Assert::AreEqual(expectedSet, testSet.toString());
		}

		TEST_METHOD(popString)
		{
			string expectedSet = "{a,b}";
			CantorSet testSet("{a,b,{c,{e,d}}}");

			testSet.pop("{c,{d,e}}");

			Assert::AreEqual((size_t)2, testSet.cardinality());
			Assert::AreEqual(expectedSet, testSet.toString());
		}
		TEST_METHOD(popString_char)
		{
			const char* const expectedSet = "{a,b}";
			CantorSet testSet("{a,b,{c,{e,d}}}");

			testSet.pop("{c,{d,e}}");

			Assert::AreEqual((size_t)2, testSet.cardinality());
			Assert::AreEqual(string(expectedSet), testSet.toString());
		}
		TEST_METHOD(popElement)
		{
			string expectedSet = "{a,b}";
			CantorSet testSet("{a,b,{c,d}}");
			CantorSet testSet2("{c,d}");

			testSet.pop(testSet2);

			Assert::AreEqual((size_t)2, testSet.cardinality());
			Assert::AreEqual(expectedSet, testSet.toString());
		}

		TEST_METHOD(clear)
		{
			string expectedSet = "{}";
			CantorSet testSet("{a,{b,{c,d}},{e,f}}");

			testSet.clear();

			Assert::AreEqual((size_t)0, testSet.cardinality());
			Assert::IsTrue(testSet.empty());
			Assert::AreEqual(expectedSet, testSet.toString());
		}
	};

	TEST_CLASS(CantorSetMisc)
	{
	public:
		TEST_METHOD(isSingleElement1)
		{
			CantorSet testSet("{}");

			Assert::IsFalse(testSet.isSingleElement());
		}
		TEST_METHOD(isSingleElement2)
		{
			CantorSet testSet("{b,c}");

			Assert::IsFalse(testSet.isSingleElement());
		}
		TEST_METHOD(isSingleElement3)
		{
			CantorSet testSet("d");

			Assert::IsTrue(testSet.isSingleElement());
		}

		TEST_METHOD(isEmpty1)
		{
			CantorSet testSet("{}");

			Assert::IsTrue(testSet.empty());
		}
		TEST_METHOD(isEmpty2)
		{
			CantorSet testSet("{a}");

			Assert::IsFalse(testSet.empty());
		}
		TEST_METHOD(isEmpty3)
		{
			CantorSet testSet("{{a,b}}");

			Assert::IsFalse(testSet.empty());
		}

		TEST_METHOD(toString1)
		{
			string expectedSet = "{}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
		}
		TEST_METHOD(toString2)
		{
			string expectedSet = "{a,b,{c,d}}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
		}
		TEST_METHOD(toString3)
		{
			string expectedSet = "{a,{b},{c,{d,e,f}}}";
			CantorSet testSet(expectedSet);

			Assert::AreEqual(expectedSet, testSet.toString());
		}

		TEST_METHOD(boolean1)
		{
			string expectedSet = "{{},{a},{b},{c},{a,b},{a,c},{b,c},{a,b,c}}";

			CantorSet testSet("{a,b,c}");
			CantorSet boolean1 = testSet.boolean();

			Assert::AreEqual(expectedSet, boolean1.toString());
		}
		TEST_METHOD(boolean2)
		{
			string expectedSet = "{{},{a},{c},{d},{{b,c}},{a,c},{a,d},{a,{b,c}},{c,d},{c,{b,c}},{d,{b,c}},{a,c,d},{a,c,{b,c}},{a,d,{b,c}},{c,d,{b,c}},{a,c,d,{b,c}}}";

			CantorSet testSet("{a,{b,c},c,d}");
			CantorSet boolean1 = testSet.boolean();

			Assert::AreEqual(expectedSet, boolean1.toString());
		}
	};

	TEST_CLASS(CantorSetOperators)
	{
	public:
		TEST_METHOD(union1)
		{
			string expectedSet = "{a,b,d,{c,d},{e,{f,g}}}";

			CantorSet testSet1("{a,b,{c,d}}");
			CantorSet testSet2("{a,d,{c,d},{e,{f,g}}}");

			testSet1 = testSet1 + testSet2;

			Assert::AreEqual(expectedSet, testSet1.toString());
		}
		TEST_METHOD(union2)
		{
			string expectedSet = "{a,b,d,{c,d},{e,{f,g}}}";

			CantorSet testSet1("{a,b,{c,d}}");
			CantorSet testSet2("{a,d,{c,d},{e,{f,g}}}");

			testSet1 += testSet2;

			Assert::AreEqual(expectedSet, testSet1.toString());
		}

		TEST_METHOD(intersection1)
		{
			string expectedSet = "{a,{c,d}}";

			CantorSet testSet1("{a,b,{c,d}}");
			CantorSet testSet2("{a,d,{c,d},{e,{f,g}}}");

			testSet1 = testSet1 * testSet2;

			Assert::AreEqual(expectedSet, testSet1.toString());
		}
		TEST_METHOD(intersection2)
		{
			string expectedSet = "{a,{c,d}}";

			CantorSet testSet1("{a,b,{c,d}}");
			CantorSet testSet2("{a,d,{c,d},{e,{f,g}}}");

			testSet1 *= testSet2;

			Assert::AreEqual(expectedSet, testSet1.toString());
		}

		TEST_METHOD(difference1)
		{
			string expectedSet = "{b}";

			CantorSet testSet1("{a,b,{c,d}}");
			CantorSet testSet2("{a,d,{c,d},{e,{f,g}}}");

			testSet1 = testSet1 - testSet2;

			Assert::AreEqual(expectedSet, testSet1.toString());
		}
		TEST_METHOD(difference2)
		{
			string expectedSet = "{b}";

			CantorSet testSet1("{a,b,{c,d}}");
			CantorSet testSet2("{a,d,{c,d},{e,{f,g}}}");

			testSet1 -= testSet2;

			Assert::AreEqual(expectedSet, testSet1.toString());
		}
	};
}