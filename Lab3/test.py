import unittest
from main import *

class TestLinkedList(unittest.TestCase):
    def test_operations(self):
        ll = LinkedList()
        ll.add_to_end(1)
        ll.add_to_beginning(0)
        self.assertEqual(ll.display(), [0, 1])
        
        ll.remove_from_beginning()
        self.assertEqual(ll.display(), [1])
        
        ll.add_to_end(2)
        ll.remove_from_end()
        self.assertTrue(ll.find(1))
        self.assertFalse(ll.find(2))

    def test_copy(self):
        ll = LinkedList()
        ll.add_to_end(1)
        ll.add_to_end(2)
        ll.add_to_end(3)
        copied_head = ll.copy_from_node(2)
        copied_list = []
        while copied_head:
            copied_list.append(copied_head.value)
            copied_head = copied_head.next
        self.assertEqual(copied_list, [2, 3])

if __name__ == "__main__":
    unittest.main()