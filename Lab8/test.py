import unittest
from main import *

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        arr1 = [3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        remove_duplicates(arr1)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6])

        arr2 = [1, 1, 1, 1, 1]
        remove_duplicates(arr2)
        self.assertEqual(arr2, [1])

        arr3 = [1, 2, 3, 4, 5]
        remove_duplicates(arr3)
        self.assertEqual(arr3, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
