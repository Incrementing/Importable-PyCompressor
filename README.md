# PyCompressor (Importable)
Importable version of my PyCompressor project.

# About
PyCompressor (Importable) is an importable version of my PyCompressor project.<br>
This was created so that the compressor can be used from within other scripts/projects and not just as a stand-alone UI.<br>
_**Tested On:** Windows 7 and Ubuntu 14.04._

# Usage
Below is an example showing this script in action.
```python
import PyCompressor # Import the script.

PyCompressor.compress("path/to/file.txt", "optional/output/path/argument") # Compress a file.
start = PyCompressor.get_start_size() # Get the size (in bytes) of the file before it's been compressed.
end = PyCompressor.get_end_size() # Get the size (in bytes) of the file after it's been compressed.
in_ = PyCompressor.get_file_input() # Get the path of the origin file.
out = PyCompressor.get_file_output() # Get the path of the compressed file.

print("File has been compressed.\nStart Size: " + str(start) + "\nEnd Size: " + str(end) + "\nInput: " + in_ + "\nOutput: " + out) # Print the results.
```
<br>The output of this code would look something like this...
```shell
File has been compressed.
Start Size: 2455
End Size: 850
Input: input.txt
Output: output.gz
```

# Dependencies
None. You just need Python installed on your system (see below).<br>
<br>
**Windows:**<br>
Go to the Python download page for Windows systems ([here](https://www.python.org/downloads/windows/)).<br>
Download the version you want.<br>
Run the installer file.<br>

**Ubuntu:**<br>
_(Most new version of ubuntu should have python pre-installed)._<br>
sudo apt-get install pythonVERSION_NUMBER_HERE<br>

**Other:**<br>
You can learn how to install python on other systems [here](https://google.com/).
