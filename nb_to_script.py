#!/usr/bin/python3

# Imports
import sys
import json
import argparse

# Function to validate the file extension
def validate_file_extension(file_path, extension):
    """
    Validate that the provided file has the specified extension.

    This function performs a basic check to ensure that the file identified
    by "file_path" has the required file extension "extension".
    
    Parameters:
    file_path (string): Path to the target file.
    extension (string): Required filename extension

    Returns:
    Raises ValueError if file path does not end in extension. Otherwise,
    no error.
    """
    if not file_path.endswith(extension):
        raise ValueError(f"Error: {file_path} must end with {extension}.")

# Checking if the script is the main program and not being imported
if __name__ == "__main__":
    # Setup the argparse module
    parser = argparse.ArgumentParser(description="Convert .ipynb file to .py file.")
    parser.add_argument("input_file", help="Input file path (must end with .ipynb)")
    parser.add_argument("output_file", help="Output file path (must end with .py)")

    args = parser.parse_args()

    # Validate file extensions
    try:
        validate_file_extension(args.input_file, ".ipynb")
        validate_file_extension(args.output_file, ".py")
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Clear the output script
    open(args.output_file, "w").close()
    script_fd = open(args.output_file, "a")
    
    # Write the shebang statement
    script_fd.write("#!/usr/bin/python3\n\n")
    
    # Open the notebook file
    notebook_fd = open(args.input_file, "r")

    # Load the notebook
    content = json.loads(notebook_fd.read())

    # Iterate through the cells
    for cell in content["cells"]:
        if (cell["cell_type"] == "markdown"):
            script_fd.write("# ".join(cell["source"]))
            script_fd.write("\n")
        if (cell["cell_type"] == "code"):
            script_fd.write("".join(cell["source"]))
            script_fd.write("\n\n")

    # Close the files
    script_fd.close()
    notebook_fd.close()