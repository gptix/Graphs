from util import Stack
from util import Queue

"""In the file graph.py, implement a Graph class that supports the API in the example below. In particular, 
this means there should be a field 

vertices that contains

a dictionary 

mapping vertex labels to edges.

 For example:

{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}
This represents a graph with four vertices and two total (bidirectional) edges. The vertex '2' has no edges, 
while '0' is connected to both '1' and '3'.

You should also create add_vertex and add_edge methods that add the specified entities to the graph. To 
test your implementation, instantiate an empty graph and then try to run the following:
"""

class Graph():
    """A graph stored as a dictionary mapping labels to sets of edges."""

    def __init__(self):
        self.vertices = {} # a dict

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() # a set within the dict

    def add_edge(self, vertex_id, other_node):
        # if not vertex_id in self.vertices:
            # raise Exception(f"No 'from' vertex with value {vertex_label}")
        self.vertices[vertex_id].add(other_node)
        
    def get_neighbors(self, vertex_label):
        return self.vertices[vertex_label]
        
    def bft(self, node):
        """Breadth-first traversal of graph."""
        q = Queue()
        q.enqueue(node)

        visited = set()

        while q.size() > 0:
            current_node = q.dequeue()

            if current_node not in visited:

                visited.add(current_node)

                neighbors  = self.get_neighbors(current_node)

                for n in neighbors:

                    q.enqueue(n)

        for v in visited:
            print(f'{v}')


    def dft(self, node):
        """Depth-first traversal of graph."""
        s = Stack()
        s.push(node)

        visited = []

        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visited:
                # print(current_node)


                visited.append(current_node)
                # print(visited)

                neighbors  = self.get_neighbors(current_node)

                for n in neighbors:

                    s.push(n)

        for v in visited:
            print(f'{v}')
  

    def dft_recursive(self, node, visited=set()):
        """Use recursion to do DFT."""
        print(node)
        visited.add(node)

        neighbors  = self.get_neighbors(node)
        for n in neighbors:

            if n not in visited:
                self.dft_recursive(n, visited)
                
    def bfs(self, start, seek):
        """Breadth-first search, returning the shortest path to
        the target."""

        q = Queue()
        visited = set()
        path = [start]
        # print(path)
    
        q.enqueue(path)

        while q.size() > 0:
            # print(visited)
            # print(q.size())
            current_path = q.dequeue()
            # print(current_path)
            current_node = current_path[-1]
            # print(current_node)

            if current_node == seek:
                return current_path

            if current_node not in visited:
                visited.add(current_node)

            neighbors = self.get_neighbors(current_node)
            for n in neighbors:

                path_copy = current_path[:]
                # print(path_copy)
                path_copy.append(n)
                # print(path_copy)

                q.enqueue(path_copy)




    def dfs(self, start, seek):
        """Depth-first search, returning the shortest path to
        the target."""

        s = Stack()
        visited = set()
        path = [start]
        # print(path)
    
        s.push(path)

        while s.size() > 0:
            # print(visited)
            # print(q.size())
            current_path = s.pop()
            # print(current_path)
            current_node = current_path[-1]
            # print(current_node)

            if current_node == seek:
                return current_path

            if current_node not in visited:
                visited.add(current_node)

            neighbors = self.get_neighbors(current_node)
            for n in neighbors:

                path_copy = current_path[:]
                # print(path_copy)
                path_copy.append(n)
                # print(path_copy)

                s.push(path_copy)





    def dfs_recursive(self, vertex, seek, path=[], visited=set()):
        """Use recursion to do search and return a path."""

        # keep track of nodes we have visited.
        visited.add(vertex)

        # Test to see if vertex is what we are seeking.
        # This is a halting case.
        if vertex == seek:
            return path

        if len(path) == 0:
            path.append(vertex)

        neighbors  = self.get_neighbors(vertex)
        for n in neighbors:

            # If we have not yet visited the neighbor, recurse.
            if n not in visited:
                result = self.dfs_recursive(n, seek, path + [n], visited)


                # if recursion returns a path, pass that path back 'up'.
                # This is a second halting case.
                if result is not None:
                    return result
                

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
# 
# graph.dfs_recursive(1,6)