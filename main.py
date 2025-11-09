from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        new_frontier = set()
        for x in frontier:
            for y in graph.get(x, set()):
                if y not in result:
                    result.add(y)
                    new_frontier.add(y)
        frontier = new_frontier


        pass
    return sorted(result)





def connected(graph):
    if not graph: 
        return True

    start = next(iter(graph))
    return reachable(graph, start) == set(graph.keys())




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    if not graph:
        return 0

    visited = set()
    count = 0

    for node in graph.keys():
        if node not in visited:
            reachable_nodes = reachable(graph, node)
            visited = visited.union(reachable_nodes)
            count += 1
    return count
    pass

