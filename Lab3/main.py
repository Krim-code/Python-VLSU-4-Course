class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_beginning(self, value):
        new_node = ListNode(value, self.head)
        self.head = new_node

    def add_to_end(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def remove_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def copy_from_node(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        if current:
            return self._copy_list(current)
        return None

    def _copy_list(self, node):
        if not node:
            return None
        new_head = ListNode(node.value)
        current_new = new_head
        current_old = node.next
        while current_old:
            current_new.next = ListNode(current_old.value)
            current_new = current_new.next
            current_old = current_old.next
        return new_head


if __name__ == "__main__":
    # Создание списка и тестирование функций
    ll = LinkedList()
    ll.add_to_end(1)
    ll.add_to_end(2)
    ll.add_to_beginning(0)
    ll.add_to_beginning(2)
    ll.add_to_end(3)
    ll.add_to_end(4)
    print("Список после добавления элементов:", ll.display())

    ll.remove_from_end()
    print("Список после удаления с конца:", ll.display())

    ll.remove_from_beginning()
    print("Список после удаления с начала:", ll.display())


    print("Поиск значения 2 в списке:", "Найдено" if ll.find(2) else "Не найдено")

    # Копирование списка начиная с элемента со значением 2
    copied_head = ll.copy_from_node(2)
    # Переводим копию в список для отображения
    copied_list = []
    while copied_head:
        copied_list.append(copied_head.value)
        copied_head = copied_head.next
    print("Копия списка начиная с элемента 2:", copied_list)
