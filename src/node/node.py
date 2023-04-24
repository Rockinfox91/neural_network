class Node:
    total_node = 0

    def __init__(self, n_in: int, n_out: int):
        assert isinstance(n_in, int) and n_in >= 0, "n_in should be a non-negative integer"
        assert isinstance(n_out, int) and n_out >= 0, "n_out should be a non-negative integer"

        self.id = Node.total_node
        Node.total_node += 1

        self.input = n_in
        self.output = n_out

    def __str__(self):
        return f"Node {str(self.id)}: ({str(self.input)},{str(self.output)})"


if __name__ == '__main__':
    print("------- Main in node.py -------")

    print("------- End node.py -------")
