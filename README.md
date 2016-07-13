# PyCompressor (Importable)
Importable version of my PyCompressor project.

# About
PyCompressor (Importable) is an importable version of my PyCompressor project.
This was created so that the compressor can be used from within other scripts/projects and not just as a stand-alone UI.

# Usage
Below is an example showing this script in action.
```python
import PyCompressor # Import the script

PyCompressor.compress("path/to/file.txt") # Compress a file
start = PyCompressor.get_start_size() # Get the size (in bytes) of the file before it's been compressed.
end = PyCompressor.get_end_size() # Get the size (in bytes) of the file after it's been compressed.

print("File has been compressed.\nStart Size: " + str(start) + "\nEnd Size: " + str(end)) # Print the results.
```
