import unittest
from collections import deque
from main import Stack , Queue, Deque, AlphabetStack

class TestStackQueueDeque(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)

    def test_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 1)

    def test_deque(self):
        deq = Deque()
        deq.add_front(1)
        deq.add_rear(2)
        self.assertEqual(deq.size(), 2)
        self.assertEqual(deq.remove_front(), 1)
        self.assertEqual(deq.size(), 1)
        self.assertEqual(deq.remove_rear(), 2)
        self.assertEqual(deq.size(), 0)

    def test_alphabet_stack(self):
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        alphabet_stack = AlphabetStack(alphabet)
        vowel_count, consonant_count = alphabet_stack.count_vowels_consonants()
        self.assertEqual(vowel_count, 10)
        self.assertEqual(consonant_count, 21)


if __name__ == "__main__":
    unittest.main()
