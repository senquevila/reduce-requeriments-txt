"""
Install package: pip install pipdeptree
Generate tree view: pipdeptree -fl > req.txt

"""

import sys
import os
import subprocess

EXCLUDED_APPS = [
    "pipdeptree",
    "pip"
    " "
]


def read_file(file_path: str) -> list:
    '''
    Create a list of packages in the given directory that not contain
    EXCLUDED_APPS (space are ignored too).
    '''
    result = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            can_insert = True
            for app in EXCLUDED_APPS:
                if line.startswith(app):
                    can_insert = False
                    break
            if can_insert:
                result.append(line)
    return result

def main():
    tree_output = "tree.txt"
    # find the path
    path = sys.argv[1]
    # execute the command
    subprocess.call(["cd",  path])
    subprocess.call(["python3", "-m", "pip", "install", "pipdeptree"])
    subprocess.call(['pipdeptree', '-fl'], stdout=open(tree_output, 'w'), stderr=subprocess.STDOUT)
    # extract the data from tree file
    data = read_file(f"{path}/{tree_output}")
    # create a new file
    new_file = os.path.join(path, "requirements.txt")
    # write the result
    with open(new_file, "w") as f:
        f.writelines(data)
    # remove the tree file
    subprocess.call(["rm", os.path.join(path, tree_output)])
    print("Success")

if __name__ == '__main__':
    main()
