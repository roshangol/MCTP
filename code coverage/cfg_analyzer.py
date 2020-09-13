import networkx as nx
import matplotlib.pyplot as plt


class cfg_coverage:

    def __init__(self, file_path_name, first_node, last_node):

        self.graph = nx.drawing.nx_pydot.read_dot(file_path_name)
        self.alll = []
        self.node_coverages = []
        self.edge_coverages = []
        self.simple_pathes = []
        self.prime_pathes = []
        self.paths = []
        self.req = []
        self.first = str(first_node)
        self.last = str(last_node)

    def graph_nodes(self):
        # This function return all nodes in your cfg
        return self.graph.nodes()

    def graph_edge(self):
        # This function return all edges in your cfg
        return self.graph.edges()

    def edge_pair(self):
        edges = []
        self.pairs = []
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
        pass

    def prime_path_coverage_bruteforce(self):
        pass

    def prime_path_coverage_setcoverage(self):
        pass