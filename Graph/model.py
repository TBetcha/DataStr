"""
a -  b \
| \     e
c - d  /

---------adjacency matrix------

 create a 2d array the size of the
number of vertices in the graph with all elements at 0
use if graph is almost complete

  a b c d e 
a 0 0 0 0 0 
b 0 0 0 0 0
c 0 0 0 0 0
d 0 0 0 0 0
e 0 0 0 0 0

starting at the first vertice, say a, if there is connection to another vertice 
we place a 1 in that index. Here there is a connection between B, C, D

  a b c d e 
a 0 1 1 1 0

------------adjacency list------------

 make an array with the size of the vertices in the graph 
 use if number of edges are few

[ a,b,c,d,e ]

easier to use dictionary though 

{ A: [B,C,D], 
  B: [A,E],
  C: [A,D],
  D: [A,C,E],
  E: [B,D] }


we then use a linked list to list the connections (edges)

a -> b -> c -> d

"""


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        # structure to hold data
        visited = [vertex]
        queue = [vertex]
        while queue:
            # while queue is not empyty dequeue next item
            de_vertex = queue.pop(0)
            print(de_vertex)
            # if item is unvisited
            for adjacent_vertex in self.gdict[de_vertex]:
                #  mark it visited
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    # append all adjacent vertices
                    queue.append(adjacent_vertex)


'''
Breadth first search

enqueue any starting vertex
while queue is not empty 
  p=dequeue()
  if p is unvisited
    mark it visited
    enqueue all adjacent unvisited vertices of p
'''


custom_dict = {"a": ["b", "c"],
               "b": ["a", "d", "e"],
               "c": ["a", "e"],
               "d": ["b", "e", "f"],
               "e": ["d", "f"],
               "f": ["d", "e"]
               }

graph = Graph(custom_dict)
graph.add_edge("e", "c")
print(graph.gdict)
graph.bfs("a")
