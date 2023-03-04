<<<<<<< HEAD
=======
import pytest
>>>>>>> origin/develop
from utils.utils import Stack

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

def test_Stack():
    assert stack.top.data == "data3"
    assert stack.top.next_node.data == "data2"
    assert stack.top.next_node.next_node.data == "data1"
