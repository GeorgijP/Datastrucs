class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """
        Тут добавление элемента
        """
        self.new_node = Node(data)
        self.new_node.next = self.top
        self.top = self.new_node

    def pop(self):
        """
        Удаляет последний элемент (LIFO)
        """
        if self.top == None:
            return None
        else:
            self.pop_node = self.top
            self.top = self.pop_node.next
            self.pop_node.next = None
            return self.pop_node.data
