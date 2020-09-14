##  Python Graph Coverage Tool

One of the popular method that use for structural software testing is coverage based code testing.
<br> when we use control flow graph for path coverage the code under test we need to extract path exist in CFG.But the main problem of path coverage criteria is loop in the code.
<b>Jeff offutt</b> introduce the prime path criteria in this [book](https://cs.gmu.edu/~offutt/softwaretest/).
In [article]() which implement in [website](https://cs.gmu.edu:8443/offutt/coverage/GraphCoverage) introduce the new method that minimize the execution path's count which cover the all prime path's.
<br><b>This package extract different information from CFG.<b>
 

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
.\venv\Scripts\activate   # for windows
pip install -r requirement.txt
```

## Usage

For using this package in your code

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
Input of this class is dot file that show cfg, first and last node and output return diffrent parameters.

## Article

Li, N., Li, F., & Offutt, J. (2012, April). Better algorithms to minimize the cost of test paths. In 2012 IEEE Fifth International Conference on Software Testing, Verification and Validation (pp. 280-289).

## License
[MIT]()
