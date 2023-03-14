from unittest import TestCase

from utils.linked_list import LinkedList

ll = LinkedList()
ll.insert_beginning({"id": 1})
ll.insert_at_end({"id": 2})
ll.insert_at_end({"id": 3})
ll.insert_beginning({"id": 0})

class Test_ll(TestCase):
    def test_LinkedList(self):
        self.assertEqual(ll.print_ll(), print(" {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"))

    def test_to_list(self):
        self.assertEqual(print(ll.to_list()), print("[{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}]"))

    def test_get_data_by_id(self):
        self.assertEqual(print(ll.get_data_by_id(0)), print("{'id': 0}"))
        self.assertEqual(print(ll.get_data_by_id(1)), print("{'id': 1}"))
        self.assertEqual(print(ll.get_data_by_id(2)), print("{'id': 2}"))
        self.assertEqual(print(ll.get_data_by_id(3)), print("{'id': 3}"))
        self.assertEqual(print(ll.get_data_by_id(4)), None)
