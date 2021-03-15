'''
Dijkstra's is good for single source shortest path esp w/ weighted graphs
  -BFS won't work because it goes level by level absorbing all the costs associated with that
  -DFS won't work becuase it goes until everything is explored not a particular vertice

Dijkstra's will not work with negative cycles though
it can't identify them and therefore the cost will decrease every time through

NOTE: A negative edge doesn't constitute a negative cycle
      It has to be a cycle with a negatvie edge where the cycle count is a negative number
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)

    return visited, path


cust_graph = Graph()
cust_graph.add_node("A")
cust_graph.add_node("B")
cust_graph.add_node("C")
cust_graph.add_node("D")
cust_graph.add_node("E")
cust_graph.add_node("F")
cust_graph.add_node("G")
cust_graph.add_edge("A", "B", 2)
cust_graph.add_edge("A", "C", 5)
cust_graph.add_edge("B", "C", 6)
cust_graph.add_edge("B", "D", 1)
cust_graph.add_edge("B", "E", 3)
cust_graph.add_edge("C", "F", 8)
cust_graph.add_edge("D", "E", 4)
cust_graph.add_edge("E", "G", 9)
cust_graph.add_edge("F", "G", 7)

print(dijkstra(cust_graph, "A"))
