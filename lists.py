from __future__ import print_function
from lib import wait, alloc


def process(jobs):
    buffer = []
    for i in range(1, jobs):
        strings = alloc(i)
        buffer.extend(strings)
        print(sum(map(len,buffer)))
    return buffer


def main():
    big = process(500)
    wait('Wasted big chunk of memory')
    
    del big
    import gc; gc.collect(2)
    wait('Freed big chunk of memory')
 
 
if __name__ == '__main__':
    main()

