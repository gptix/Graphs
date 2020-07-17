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
        if not self.vertices[vertex_label]:
            # raise ValueError(f'No vertex {vertex_label}')
        self.vertices[vertex_label].add(other_node)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('1', '0')
graph.add_edge('0', '3')
graph.add_edge('3', '0')
print(graph.vertices)