import unittest
from utils.linked_list import LinkedList

ll = LinkedList()
ll.insert_beginning({"id": 1})
ll.insert_at_end({"id": 2})
ll.insert_at_end({"id": 3})
ll.insert_beginning({"id": 0})


def test_LinkedList(self):
    self.assertEqual(ll.print_ll(), ' {"id": 0} -> {"id": 1} -> {"id": 2} -> {"id": 3} -> None')
