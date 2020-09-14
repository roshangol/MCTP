from code_coverage import cfg_coverage

example1 = cfg_coverage('./example_dot/Digraph.gv', 1, 2)

# print(example1.graph_nodes())
# print(example1.graph_edge())
# print(example1.simple_path())
# print(len(example1.simple_path()))
# print(example1.prime_path())
# print(len(example1.prime_path()))
# print(example1.cyclomatic_complexity())
# print(example1.edge_pair())
example1.draw_cfg()

"""
# choose one of two method for compute minimum number of path to cover the graph 
tp, tr = example1.prime_path_coverage_bruteforce()
tp, tr = example1.prime_path_coverage_setcoverage()
for i in range(len(tp)):
    print(tp[i], "-->", tr[i], "\n")
"""
