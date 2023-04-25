import unittest
from src.node.node import Node


class TestNode(unittest.TestCase):

    def test_reset_number_total_node(self):
        node1 = Node(1, 1)
        node2 = Node(2, 2)
        Node.reset_number_total_node()
        self.assertEqual(Node.get_number_total_node(), 0)

    # Create a node Errors
    def test_node_id(self):
        node1 = Node(1, 2)
        node2 = Node(2, 2)
        self.assertEqual(node1.id, 0)
        self.assertEqual(node2.id, 1)

    def test_valid_input_output(self):
        node = Node(3, 4)
        self.assertEqual(node.n_input, 3)
        self.assertEqual(node.n_output, 4)

    def test_invalid_input_type(self):
        with self.assertRaises(AssertionError):
            node = Node('invalid', 4)

    def test_invalid_output_type(self):
        with self.assertRaises(AssertionError):
            node = Node(3, 'invalid')

    def test_negative_input(self):
        with self.assertRaises(AssertionError):
            node = Node(-1, 4)

    def test_negative_output(self):
        with self.assertRaises(AssertionError):
            node = Node(3, -1)

    def test_zero_input_output(self):
        node = Node(0, 0)
        self.assertEqual(node.n_input, 0)
        self.assertEqual(node.n_output, 0)

    # Print a node Errors
    def test_print_node(self):
        Node.reset_number_total_node()
        node = Node(1, 2)
        self.assertEqual(str(node), f"Node 0: (1,2)")

    # Test for total node number
    def test_total_node(self):
        Node.reset_number_total_node()
        self.assertEqual(Node.get_number_total_node(), 0)
        node1 = Node(1, 2)
        self.assertEqual(Node.get_number_total_node(), 1)
        node2 = Node(1, 2)
        self.assertEqual(Node.get_number_total_node(), 2)


if __name__ == '__main__':
    unittest.main()
