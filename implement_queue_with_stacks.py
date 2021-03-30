class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue(object):

    def __init__(self, values=None):
        self.head = None
        self.length = 0
        # self.tail = None
        if values:
            node = Node(values.pop(0))
            self.head = node
            self.length = len(values)
            for elem in values:
                node.next = Node(value=elem)
                node = node.next

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

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: any
        :rtype: None
        """
        new_node = Node(x)

        if self.length == 0:
            self.head = new_node
            # self.tail = new_node
            return

        if self.head is None:
            self.head = new_node
            return
        # self.tail.next = new_node
        # self.tail = new_node
        #
        current_node = self.head
        for current_node in self:
            pass
        current_node.next = new_node
        self.length += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.head is None:
            return None
        # if self.head == self.tail:
        #     self.tail = None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.value

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.head is not None:
            return self.head.value
        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.head is None:
            return True
        return False

    def print_queue(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next

        return nodes


my_stack = MyQueue(["Web1", "Web2", "Web3", "Web5", "Web4"])
print(my_stack.pop())
print(my_stack.pop())
# print(my_stack.pop())

print(my_stack)
print(my_stack.print_queue())

my_stack.push({1: "A", 2: "B"})
my_stack.push([5, 6, 7])

print(my_stack)
print(my_stack.print_queue())
