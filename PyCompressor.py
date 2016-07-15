'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import os
import time
import gzip
import hashlib

class StrWorker:

    def __init__(self, str_, output):
        if (output == "none"):
            output = hashlib.sha224(repr(time.time())).hexdigest() + ".gz"

        to_check = output.strip(output.split("/")[len(output.split("/")) - 1])
        if (not to_check.endswith("/")):
            to_check += "/"
        if (not os.path.exists(to_check)):
            raise Exception("Null... path doesn't exist")
        if (not len(output.split("/")[len(output.split("/")) - 1].split(".")) >= 2):
            if (not output.endswith("/")):
                output += "/"
            output += hashlib.sha224(repr(time.time())).hexdigest() + ".gz"

        self.str = str_
        self.path = "N/A"
        self.output = output
        self.is_done = False
        self.start_size = "N/A"
        self.end_size = 0

    def compress(self):
        with gzip.open(self.output, "wb") as compressed:
            compressed.writelines(self.str)
        self.end_size = os.stat(self.output).st_size
        self.is_done = True

class FileWorker:

    def __init__(self, path, output):
        if (output == "none"):
            output = path + ".gz"

        to_check = output.strip(output.split("/")[len(output.split("/")) - 1])
        if (not to_check.endswith("/")):
            to_check += "/"
        if (not os.path.exists(to_check)):
            raise Exception("Null... path doesn't exist")
        if (not len(output.split("/")[len(output.split("/")) - 1].split(".")) >= 2):
            if (not output.endswith("/")):
                output += "/"
            output += path.split("/")[len(path.split("/")) - 1] + ".gz"

        self.str = "N/A"
        self.path = path
        self.output = output
        self.is_done = False
        self.start_size = 0
        self.end_size = 0

    def compress(self):
        x = self.path

        if (os.path.exists(x)):
            if (os.path.isfile(x)):
                self.start_size = os.stat(x).st_size
                with open(x, "rb") as to_compress:
                    with gzip.open(self.output, "wb") as compressed:
                        compressed.writelines(to_compress)
                self.end_size = os.stat(self.output).st_size
                self.is_done = True
            else:
                raise Exception("Null... path doesn't point to a file")
        else:
            raise Exception("Null... path doesn't exist")

global worker

def compress(path, output="none"):
    global worker
    path = path.replace("\\", "/")
    output = output.replace("\\", "/")
    worker = FileWorker(path, output)
    worker.compress()

def compress_str(str, output="none"):
    global worker
    output = output.replace("\\", "/")
    worker = StrWorker(str, output)
    worker.compress()

def get_start_size():
    global worker
    try:
        worker.is_done
    except:
        raise Exception("Incomplete... file hasn't been compressed yet")
    return worker.start_size

def get_end_size():
    global worker
    try:
        worker.is_done
    except:
        raise Exception("Incomplete... file hasn't been compressed yet")
    return worker.end_size

def get_file_input():
    global worker
    try:
        worker.is_done
    except:
        raise Exception("Incomplete... file hasn't been compressed yet")
    return worker.path

def get_file_output():
    global worker
    try:
        worker.is_done
    except:
        raise Exception("Incomplete... file hasn't been compressed yet")
    return worker.output

def get_str_input():
    global worker
    try:
        worker.is_done
    except:
        raise Exception("Incomplete... file hasn't been compressed yet")
    return worker.str
