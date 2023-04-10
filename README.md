# Reduce-Requirements
This module provides a simple way to reduce the number of requirements listed in a Python project's *requirements.txt* file when using PIP. This can be a useful tool for identifying the main requirements of our Python project that call upon other dependencies.

## Installation
First, it's necessary to install the library **pipdeptree** in the project that needs to reduce its *requirements.txt* file. This module extracts all dependencies of the project and generates a tree structure to visualize them.

`pip install pipdeptree`

This package generate a tree of dependencies with the following command:

`pipdeptree -fl > tree.txt`

The *tree.txt* file contains a dependencies tree:

```
root1
 child1_1
 child1_2
  subchild1_2_1
  subchild1_2_2
 child1_3
root2
 child2_1
```

The object is to get all the root dependencies instead any child dependency.

## Usage
Execute the following command:

`python reduce-req.py path/to/project/`

This command creates a *requirements.txt* file with the root dependencies.