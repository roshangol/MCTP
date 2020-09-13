##  Python Graph Coverage Tool


## Requirement

- python3
- networkx
- pydot
- matplotlib
 
## Installation
For install the required packege:

```bash
virtualenv venv
source ./venv/bin/activate  # for linux
.\\venv\\Scripts\\activate   # for windows
pip install -r requirement.txt
```

## Usage

For using this package in your code

Input of this class is dot file that show cfg, first and last node and output return diffrent parameters.

```python
from code_coverage import cfg_coverage

example1 = cfg_coverage('./example_dot/Digraph.gv', 1, 2)
print(example1.graph_nodes())
print(example1.graph_edge())
print(example1.simple_path())
print(len(example1.simple_path()))
print(example1.prime_path())
print(len(example1.prime_path()))
print(example1.cyclomatic_complexity())
print(example1.edge_pair())
example1.draw_cfg()
# choose one of two method for compute minimum number of path to cover the graph 
tp, tr = example1.prime_path_coverage_bruteforce()
tp, tr = example1.prime_path_coverage_setcoverage()
for i in range(len(tp)):
    print(tp[i], "-->", tr[i], "\n")
```

## Article
Li, N., Li, F., & Offutt, J. (2012, April). Better algorithms to minimize the cost of test paths. In 2012 IEEE Fifth International Conference on Software Testing, Verification and Validation (pp. 280-289). IEEE.

## License
[MIT]()
