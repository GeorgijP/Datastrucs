import unittest
from utils.linked_list import LinkedList

ll = LinkedList()
ll.insert_beginning({"id": 1})
ll.insert_at_end({"id": 2})
ll.insert_at_end({"id": 3})
ll.insert_beginning({"id": 0})


def test_LinkedList(self):
    self.assertEqual(ll.print_ll(), ' {"id": 0} -> {"id": 1} -> {"id": 2} -> {"id": 3} -> None')

def test_to_list(self):
    self.assertEqual(print(ll.to_list()), "[{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}]")

def test_get_data_by_id(self):
    self.assertEqual(print(ll.get_data_by_id(0)), "{'id': 0}")
    self.assertEqual(print(ll.get_data_by_id(1)), "{'id': 1}")
    self.assertEqual(print(ll.get_data_by_id(2)), "{'id': 2}")
    self.assertEqual(print(ll.get_data_by_id(3)), "{'id': 3}")
    self.assertEqual(print(ll.get_data_by_id(4)), None)
