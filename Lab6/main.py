class ContactsManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, last_name, first_name, number):
        self.contacts.append((last_name, first_name, number))

    def remove_contact(self, last_name, first_name):
        self.contacts = [(l, f, n) for l, f, n in self.contacts if l != last_name or f != first_name]

    def remove_second_number(self, last_name, first_name):
        for i, (l, f, n) in enumerate(self.contacts):
            if l == last_name and f == first_name:
                if ',' in n:
                    self.contacts[i] = (l, f, n.split(',')[0])
                    break

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

import re

def find_deer_and_hare(text):
    pattern = r'\bолень\b([\s,]*(?:\w+[\s,]*){0,5})\bзаяц\b'
    matches = re.findall(pattern, text)
    results = [f'олень{match}заяц' for match in matches]
    return results

