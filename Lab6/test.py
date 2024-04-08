import unittest
from main import *

class TestContactsManager(unittest.TestCase):
    def test_add_contact(self):
        contacts_manager = ContactsManager()
        contacts_manager.add_contact('Иванов', 'Иван', '12345')
        self.assertIn(('Иванов', 'Иван', '12345'), contacts_manager.contacts)

    def test_remove_contact(self):
        contacts_manager = ContactsManager()
        contacts_manager.add_contact('Иванов', 'Иван', '12345')
        contacts_manager.add_contact('Петров', 'Петр', '54321')
        contacts_manager.remove_contact('Иванов', 'Иван')
        self.assertNotIn(('Иванов', 'Иван', '12345'), contacts_manager.contacts)

    def test_remove_second_number(self):
        contacts_manager = ContactsManager()
        contacts_manager.add_contact('Иванов', 'Иван', '12345,67890')
        contacts_manager.remove_second_number('Иванов', 'Иван')
        self.assertEqual(contacts_manager.contacts[0][2], '12345')

class TestFindDeerAndHare(unittest.TestCase):
    def test_find_deer_and_hare(self):
        text1 = "Да он олень, а не заяц! Это олень, это точно не заяц. Заяц, а не олень. олень, а не заяц! олень, это точно не заяц."
        self.assertEqual(find_deer_and_hare(text1), ['олень, а не заяц','олень, это точно не заяц', 'олень, а не заяц','олень, это точно не заяц'])

        text2 = "Ошибка и напиши тесты"
        self.assertEqual(find_deer_and_hare(text2), [])

if __name__ == "__main__":
    unittest.main()