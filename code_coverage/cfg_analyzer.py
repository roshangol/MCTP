import networkx as nx
import matplotlib.pyplot as plt
from .path_finder import simple_paths, prime_paths
from .prime_path_coverage import prime_path_coverage_bruteforce, prime_path_coverage_superset


class cfg_coverage:

    def __init__(self, file_path_name, first_node, last_node):

        self.graph = nx.drawing.nx_pydot.read_dot(file_path_name)
        self.alll = list()
        self.node_coverages = list()
        self.edge_coverages = list()
        self.simple_pathes = list()
        self.prime_pathes = list()
        self.paths = list()
        self.req = list()
        self.first = str(first_node)
        self.last = str(last_node)

    def graph_nodes(self):
        # This function return all nodes in your cfg
        return self.graph.nodes()

    def graph_edge(self):
        # This function return all edges in your cfg
        return self.graph.edges()

    def edge_pair(self):
        edges = list()
        self.pairs = list()
        for edge in self.graph_edge():
            edges.append(edge)
        for i in edges:
            for j in edges:
                if i == j:
                    continue
                else:
                    if i[1] == j[0]:
                        self.pairs.append([i[0], i[1], j[1]])
        return self.pairs

    def cyclomatic_complexity(self):
        scyclomatic = len(self.graph_edge()) - len(self.graph_nodes()) + 2
        return scyclomatic

    def simple_path(self):
        simples = simple_paths(self.graph)
        return simples

    def prim_path(self):
        primes = prime_paths(self.graph, self.first, self.last)
        return primes

    def prime_path_coverage_bruteforce(self):
        prime_path_coverage_bruteforce(self.graph, self.first, self.last)

    def prime_path_coverage_setcoverage(self):
        prime_path_coverage_superset(self.graph, self.first, self.last)

    def draw_cfg(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
