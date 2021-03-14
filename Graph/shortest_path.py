'''
Breadth first search

    time -> O(E)
    space -> O(E)

enqueue any starting vertex
while queue is not empty 
  p=dequeue()
  if p is unvisited
    mark it visited
    enqueue all adjacent unvisited vertices of p
    update parent of adjacent vertices to current vertex
    
Although this works on an unweighted graph it will not work on a weighted graph

'''


class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        else:
            self.gdict = gdict

    def bfs(self, start, end):
        queue = []              # -> O(1)
        queue.append([start])
        while queue:            # -> O(V)
            path = queue.pop(0)
            node = path[-1]     # -> O(1)
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):  # -> O(E)
                new_path = list(path)
                new_path.append(adjacent)  # -> O(1)
                queue.append(new_path)


custom_dict = {"a": ["b", "c"],
               "b": ["d", "g"],
               "c": ["d", "e"],
               "d": ["f"],
               "e": ["f"],
               "g": ["f"]
               }

g = Graph(custom_dict)
print(g.bfs("a", "e"))
