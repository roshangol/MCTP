import networkx as nx


def read_graph(g, firs, last):
    edges = {}
    nodes = list(nx.nodes(g))
    initNodes = [firs]
    endNodes = [last]
    for i in nx.nodes(g):
        edges[i] = [j[1] for j in list(g.edges(i))]
    graph = {'nodes': nodes, 'init': initNodes, 'end': endNodes, 'edges': edges}
    return graph


def isPrimePath(path, graph):
    """Whether a path is a prime path."""
    if len(path) >= 2 and path[0] == path[-1]:
        return True
    elif reachHead(path, graph) and reachEnd(path, graph):
        return True
    else:
        return False


def reachHead(path, graph):
    """
    Whether the path can be extended at head, and the extended path is still
    a simple path.
    """
    former_nodes = filter(lambda n: path[0] in graph[
                          'edges'][n], graph['nodes'])
    for n in former_nodes:
        if n not in path or n == path[-1]:
            return False
    return True


def reachEnd(path, graph):
    """
    Whether the path can be extended at tail, and the extended path is still
    a simple path.
    """
    later_nodes = graph['edges'][path[-1]]
    for n in later_nodes:
        if n not in path or n == path[0]:
            return False
    return True


def extendable(path, graph):
    """Whether a path is extendable."""
    if isPrimePath(path, graph) or reachEnd(path, graph):
        return False
    else:
        return True


def findSimplePath(graph, exPaths, paths=[]):
    """Find the simple paths of a graph."""
    paths.extend(filter(lambda p: isPrimePath(p, graph), exPaths))
    exPaths = filter(lambda p: extendable(p, graph), exPaths)
    newExPaths = []
    for p in exPaths:
        for nxx in graph['edges'][p[-1]]:
            if nxx not in p or nxx == p[0]:
                newExPaths.append(p + (nxx, ))
    if len(newExPaths) > 0:
        findSimplePath(graph, newExPaths, paths)


def findPrimePaths(graph):
    """Find the prime paths of a graph."""
    last_prime = []
    exPaths = [(n, ) for n in graph['nodes']]
    simplePaths = []
    # recursively finding the simple paths of the graph
    findSimplePath(graph, exPaths, simplePaths)
    primePaths = sorted(simplePaths, key=lambda a: (len(a), a), reverse=True)

    for i in primePaths:
        if len(i) != 1:
            last_prime.append(list(i))

    return last_prime


def simple_path(g):
    sims = []
    for i in g.nodes():
        sims.append(list(i))
        for j in g.nodes():
            sim = list(nx.all_simple_paths(g, i, j))
            for k in sim:
                if k not in sims and k != []:
                    sims.append(k)
    return sims


def prime_paths(g, first, last):
    graph = read_graph(g, first, last)
    primes = findPrimePaths(graph)
    return primes
