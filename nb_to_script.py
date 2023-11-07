#!/usr/bin/python3

# Imports
import sys
import json

# Checking if the script is the main program and not being imported
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 nb_to_script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    if (".ipynb" not in file_path):
        print("Error: nb_to_script.py requiures a Jupyter notebook as an input file.")
        sys.exit(1)

    fd = open(file_path, "r")

    
    
    fd.close()