class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root_value=None):
        self.root = root_value

        if root_value:
            self.root = Node(root_value)

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
            return

        current_node = self.root
        if node.value == current_node.value:
            return

        while True:
            if node.value > current_node.value:
                if node.value == current_node.value:
                    return
                if not current_node.right:
                    current_node.right = node
                    return self
                current_node = current_node.right
            else:
                if node.value == current_node.value:
                    return
                if not current_node.left:
                    current_node.left = node
                    return self
                current_node = current_node.left

    def lookup(self, value):
        if not self.root:
            return False
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return {"Node": current_node.value, "Left": current_node.left, "Right": current_node.right}

        return False

    def breadth_first_search(self):
        current_node = self.root
        array1 = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            array1.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return array1


bst = BinarySearchTree(root_value=9)
bst.insert(Node(9))
bst.insert(Node(4))
bst.insert(Node(6))
bst.insert(Node(20))
bst.insert(Node(170))
bst.insert(Node(15))
bst.insert(Node(1))

print(bst.breadth_first_search())

# print(bst.lookup(6))
