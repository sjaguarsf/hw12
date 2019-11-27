#!/usr/bin/env python3

import concurrent.futures
import math
import os
import threading
import sys

def encode_pathname():
    pool = concurrent.futures.ThreadPoolExecutor()
    for i in range(len(sys.argv)):

if __name__=="__main__":
    inputs = range(1,10)
    pool = concurrent.futures.ThreadPoolExecutor()
    print(list(pool.map(math.log, inputs)),
        list(zip(inputs,pool.map(math.log,inputs))))


