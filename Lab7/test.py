import unittest
from main import *

class TestKMPAlgorithm(unittest.TestCase):
    def test_search(self):
        kmp = KMP("abc")
        self.assertEqual(kmp.search("abcdabc"), [0, 4])
        self.assertEqual(kmp.search("xabcy"), [1])
        self.assertEqual(kmp.search("xabcdabcd"), [1,5])

class TestPatternChecker(unittest.TestCase):
    def test_check(self):
        patterns = ["abc", "def"]
        text1 = "abcdef"
        text2 = "abcdefg"
        checker1 = PatternChecker(patterns, text1)
        checker2 = PatternChecker(patterns, text2)
        self.assertFalse(checker1.check())  # Должен вернуть False, так как текст содержит образец "abc"
        # self.assertTrue(checker2.check())   # Должен вернуть True, так как текст не содержит подстрок, не совпадающих с образцами

if __name__ == "__main__":
    unittest.main()