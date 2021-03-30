class Graphs:
    def __init__(self):
        self.numofNodes = 0
        self.adjacentList = {}

    def add_vertex(self, node):
        self.adjacentList.update({node: []})
        self.numofNodes += 1

    def add_edge(self, node1, node2):
        if node1 and node2 in self.adjacentList:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
            return
        print("Node(s) not present")

    def print(self):
        print(self.adjacentList)


new_graph = Graphs()
new_graph.add_vertex(3)
new_graph.add_vertex(5)
new_graph.add_vertex(4)
new_graph.add_vertex(2)
new_graph.add_vertex(1)
new_graph.add_vertex(6)
new_graph.add_vertex(7)

new_graph.add_edge(3, 5)
new_graph.add_edge(1, 5)
new_graph.add_edge(1, 2)
new_graph.add_edge(2, 5)
new_graph.add_edge(2, 3)
new_graph.add_edge(5, 4)
new_graph.add_edge(4, 6)
new_graph.add_edge(4, 3)
new_graph.add_edge(7, 1)

new_graph.print()
