import os
import linecache
import time
from SSDB import SSDB
import json

ssdb = SSDB('127.0.0.1', 8888)

print("start")
start = time.perf_counter()
cache_data = linecache.getlines("/usr/local/access.log")

for line in range(len(cache_data)):
    ssdb.request('set', str(line).encode(), '0'.encode())
end = time.perf_counter()
print("read: %f s" % (end - start))

print("ok")