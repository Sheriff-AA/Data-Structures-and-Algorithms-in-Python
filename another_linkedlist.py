class LinkedList:
    def __init__(self, value):
        self.head = {"value": value,
                     "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {"value": value,
                    "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = {"value": value,
                    "next": None}
        new_node["next"] = self.head
        self.head = new_node

    def print_list(self):
        array1 = []
        current_node = self.head
        while current_node:
            array1.append(current_node["value"])
            current_node = current_node["next"]

        return array1


linked_list = LinkedList(12)
linked_list.append(3)
linked_list.append(12)
linked_list.append(5)
print(linked_list.print_list())
