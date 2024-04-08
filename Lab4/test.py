import unittest
from main import DoublyLinkedList, CircularDoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_doubly_linked_list(self):
        dll = DoublyLinkedList()
        dll.add_to_beginning(1)
        dll.add_to_end(2)
        self.assertEqual([1, 2], dll.display())

        dll.remove_from_end()
        self.assertEqual([1], dll.display())

        dll.remove_from_beginning()
        self.assertEqual([], dll.display())
        dll.add_to_end(3)
        dll.add_to_end(4)
        self.assertTrue(dll.find(3))
        self.assertFalse(dll.find(5))

    def test_circular_doubly_linked_list(self):
        cdl = CircularDoublyLinkedList()
        cdl.add_to_beginning(1)
        cdl.add_to_end(2)
        self.assertEqual([1, 2], cdl.display())

        cdl.remove_from_beginning()
        self.assertEqual([2], cdl.display())
        cdl.remove_from_end()
        self.assertEqual([], cdl.display())

        cdl.add_to_beginning(3)
        cdl.add_to_beginning(4)
        cdl.add_to_end(5)
        self.assertTrue(cdl.find(3))
        self.assertTrue(cdl.find(5))
        
        # Проверка на кольцевость
        cdl.add_to_end(6)
        self.assertEqual(cdl.head.prev.value, cdl.tail.value)
        self.assertEqual(cdl.tail.next.value, cdl.head.value)

if __name__ == "__main__":
    unittest.main()