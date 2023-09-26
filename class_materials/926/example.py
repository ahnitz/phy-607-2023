import time
import numpy

def do_other_stuff():
    time.sleep(0.1) 

def do_stuff():
    v = numpy.zeros(10000000)
    for i in range(10):
        v += v

for i in range(10):
    do_stuff()
    do_other_stuff()
