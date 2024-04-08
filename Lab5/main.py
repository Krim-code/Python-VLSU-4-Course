class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


class AlphabetStack:
    def __init__(self, alphabet):
        self.stack = Stack()
        for letter in alphabet:
            self.stack.push(letter)

    def count_vowels_consonants(self):
        vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
        consonants = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}
        vowel_count = 0
        consonant_count = 0
        for letter in self.stack.display():
            if letter.lower() in vowels:
                vowel_count += 1
            elif letter.lower() in consonants:
                consonant_count += 1
        return vowel_count, consonant_count


if __name__ == "__main__":
    # Исходные данные - массив букв русского алфавита
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    
    # Создаем стек из элементов массива
    alphabet_stack = AlphabetStack(alphabet)

    # Определяем количество гласных и согласных букв в стеке
    vowel_count, consonant_count = alphabet_stack.count_vowels_consonants()

    # Выводим результат
    print("Количество гласных букв:", vowel_count)
    print("Количество согласных букв:", consonant_count)
