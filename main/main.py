from utils.utils import Stack

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

print(stack.top.data)
print(stack.top.next.data)
print(stack.top.next.next.data)
print(stack.top.next.next.next_node)
