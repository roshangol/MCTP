##  Python Graph Coverage Tool


## Requirement

- python3

 
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

Input of this class is dot file that show cfg and first and last node and return diffrent parameters.

```python
from code_coverage import cfg_coverage 
    
    sample = cfg_coverage('your file.dot', first node, last node)
    sample.graph_node()
    sample.graph_edge()
    sample.node_coverage()
    sample.edge_coverage()
    sample.simple_path()
    sample.prime_path()
    sample.prime_path_coverage()
```


## License
[MIT]()
