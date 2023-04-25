class Node:
    _total_node = 0

    def __init__(self, n_in: int, n_out: int) -> None:
        assert isinstance(n_in, int) and n_in >= 0, "n_in should be a non-negative integer"
        assert isinstance(n_out, int) and n_out >= 0, "n_out should be a non-negative integer"

        self.__id = Node._total_node
        Node._total_node += 1

        self.n_input = n_in
        self.n_output = n_out

    def __str__(self) -> str:
        return f"Node {str(self.__id)}: ({str(self.n_input)},{str(self.n_output)})"

    @classmethod
    def get_number_total_node(cls):
        return cls._total_node

    @classmethod
    def reset_number_total_node(cls):
        cls._total_node = 0

    def get_id(self):
        return self.__id


if __name__ == '__main__':
    print("------- Main in node.py -------")

    print("------- End node.py -------")
