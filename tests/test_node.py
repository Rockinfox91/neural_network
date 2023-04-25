import unittest
from src.node.node import Node


class TestNode(unittest.TestCase):

    # Test privacy of Node.__total_node
    def test_total_node_privacy(self):
        with self.assertRaises(AttributeError):
            self.assertEqual(Node.total_node, 0)
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
        node = Node(1, 2)
        self.assertEqual(str(node), f"Node {node.id}: ({node.n_input},{node.n_output})")


if __name__ == '__main__':
    unittest.main()
