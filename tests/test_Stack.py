import unittest
from utils.utils import Stack

item = Stack()
item.push('data1')
item.push('data2')
item.push('data3')

class TestStack(unittest.TestCase):

    def test_Stack(self):
        self.assertEqual(item.top.data, 'data3')
        self.assertEqual(item.top.next.data, 'data2')
        self.assertEqual(item.top.next.next.data, 'data1')
        self.assertEqual(item.top.next.next.next_node, None)

    def test_pop(self):
        self.assertEqual(item.pop(), 'data3')
        self.assertEqual(item.pop(), 'data2')
        self.assertEqual(item.pop(), 'data1')
        self.assertEqual(item.pop(), None)