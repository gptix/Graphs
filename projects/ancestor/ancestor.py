"""
Understand:
Find most distant nodes from starting node.
Return lowest ID of these.

Plan:
Approach: 
- Invert the graph by reversing the edges, so we will look 'down' the matrix.
- Instantiate graph and add vertices.
- Find vertices with no 'to' nodes.  The furthest must be one of these.

- Use breadth-first search to find possible paths to targets.

- Filter Nones.
- Find max path length.
- Filter paths on this length.
- Get id's of terminal nodes of these paths.

Return min of these.

"""
from util import Stack
from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    pass


    g = Graph()

    # add vertices to g
    v_range = range(1,12)
    for vertex in v_range:
        g.add_vertex(vertex)

    # flip the edges so we can move from children to parents
    original_edges = ancestors

    # This creates a new list of tuples, since tuples are immutable.
    edges = [(y, x) for (x, y) in original_edges]
    # edges = [reversed(e) for e in original_edges]

    # add the edges
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    # get list of nodes with no parents. The most distant from any node must be one of these.
    target_nodes = [v for v in v_range if g.vertices[v] == set()]

        
    if starting_node in target_nodes:
        return -1

    # collect shortest paths to targets using bfs. Filter out Nones.
    paths = [p for p in 
             [g.bfs(starting_node, t) for t in target_nodes] 
             if p is not None]

    max_length = max([len(p) for p in paths])

    longest_paths = [p for p in paths if len(p) == max_length]

    max_distance_ancestors = [p[-1] for p in longest_paths]
    
    return min(max_distance_ancestors)


ancestor_edges = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
starting_node = 6

earliest_ancestor