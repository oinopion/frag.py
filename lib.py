import sys
import random


def alloc(num, size=5000):
    return [random_string(size) for i in range(num)]


def random_string(size):
    return random.choice('abcdef') * size
    

def wait(msg):
    sys.stdout.write("%s\n" % msg)
    sys.stdin.readline()

