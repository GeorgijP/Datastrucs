class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """Удаляет элемент, который добавили первым"""
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next_node
        return data
