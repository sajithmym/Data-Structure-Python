class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Example usage
node1 = Node(1)
node2 = Node(2)
node1.next = node2
