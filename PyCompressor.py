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
import gzip

class Worker:

    def __init__(self, path):
        self.path = path
        self.is_done = False
        self.start_size = 0
        self.end_size = 0

    def compress(self):
        x = self.path
        if (os.path.exists(x)):
            if (os.path.isfile(x)):
                self.start_size = os.stat(x).st_size
                with open(x, "rb") as to_compress:
                    with gzip.open(x + ".gz", "wb") as compressed:
                        compressed.writelines(to_compress)
                self.end_size = os.stat(x + ".gz").st_size
                self.is_done = True
            else:
                raise Exception("Null... path doesn't point to a file")
        else:
            raise Exception("Null... path doesn't exist")

global worker

def compress(path):
    global worker
    worker = Worker(path)
    worker.compress();

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
