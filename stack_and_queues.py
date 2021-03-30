class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, values=None):
        self.head = None
        self.length = 0

        if values:
            node = Node(values.pop(0))
            self.head = node
            self.length = len(values)
            for elem in values:
                temp = self.head
                node = Node(value=elem)
                self.head = node
                node.next = temp
                # node = node.next
        # if values:
        #     self.length = len(values)
        #     if len(values) == 1:
        #         self.head = Node(value=values.pop(0))
        #     else:
        #         node = Node(value=values.pop(0))
        #         self.head = node
        #         self.tail = Node(value=values.pop(len(values) - 1))
        #         for val in values:
        #             node.next = Node(value=val)
        #             node = node.next
        #             if values.index(val) == len(values) - 1:
        #                 node.next = self.tail

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def peek(self):
        if self.head is not None:
            return self.head.value
        return None

    def push(self, node: Node):
        temp = self.head
        self.head = node
        node.next = temp
        self.length += 1

    def pop(self):
        if self.head is None:
            return self.head

        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.value

    def print_stack(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return nodes


my_stack = Stack(["Web1", "Web2", "Web3", "Web5", "Web4"])
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
my_stack.push(Node("Web 99"))

print(my_stack)

print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())

print(my_stack.print_stack())

print(my_stack.peek())
print(my_stack.push(Node(3)))
print(my_stack.push(Node({1: "A", 2: "B"})))

print(my_stack.print_stack())
print(my_stack)
