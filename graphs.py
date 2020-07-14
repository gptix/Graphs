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

    def __init__(self):
        self.vertices = {} # a dict

    def add_vertex(self, vertex_label):
        if not vertex_label in self.vertices:
            self.vertices[vertex_label] = set() # a set within the dict
        return self.vertices[vertex_label]

    def add_edge(self, vertex_label, other_node):
        if not vertex_label in self.vertices:
            raise Exception(f"No 'from' vertex with value {vertex_label}")
        
        self.vertices[vertex_label].add(other_node)
        
    """Write a function within your Graph class that takes takes a starting 
node as an argument, then performs BFT. Your function should print 
the resulting nodes in the order they were visited. Note that there 
are multiple valid paths that may be printed."""

    def bft(starting_node):
        q = starting_node.vertices
        while q != []:
            this_vertex = q.pop(0)
            q += this_vertex.vertices
            print(this_vertex)
