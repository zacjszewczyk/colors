#!/usr/bin/python3

# Imports
import sys
import json

# Checking if the script is the main program and not being imported
if __name__ == "__main__":
    # Basic input checking for required number of parameters 
    if len(sys.argv) != 2:
        print("Usage: python3 nb_to_script.py <file_path>")
        sys.exit(1)
    
    # Basic input checking for required file path extension
    file_path = sys.argv[1]
    if (".ipynb" not in file_path):
        print("Error: nb_to_script.py requiures a Jupyter notebook as an input file.")
        sys.exit(1)

    # Clear the output file
    open("output.py", "w").close()
    script_fd = open("output.py", "a")

    # Open the notebook file
    notebook_fd = open(file_path, "r")

    content = json.loads(notebook_fd.read())

    print(content["cells"])

    # Close the files
    script_fd.close()
    notebook_fd.close()