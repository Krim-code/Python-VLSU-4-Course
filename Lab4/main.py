class DoublyListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_beginning(self, value):
        new_node = DoublyListNode(value, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_to_end(self, value):
        new_node = DoublyListNode(value, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_beginning(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def remove_from_end(self):
        if not self.tail:
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

class CircularDoublyLinkedList(DoublyLinkedList):
    def add_to_beginning(self, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = self.tail = new_node
            self.head.next = self.head.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = self.tail.next = new_node
            self.head = new_node

    def add_to_end(self, value):
        if not self.head:
            self.add_to_beginning(value)
        else:
            new_node = DoublyListNode(value, self.tail, self.head)
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def remove_from_beginning(self):
        if self.head == self.head.next:
            self.head = self.tail = None
        elif self.head:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

    def remove_from_end(self):
        if self.tail == self.head:
            self.head = self.tail = None
        elif self.tail:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def display(self):
        values = []
        if self.head:
            current = self.head
            while True:
                values.append(current.value)
                current = current.next
                if current == self.head:
                    break
        return values
