from lib import wait, alloc
import guppy
hpy = guppy.hpy


def main():
    big = alloc(100000)
    wait('Wasted big chunk of memory')
    print hpy().heap()
    
    small = alloc(1)

    del big
    print hpy().heap()
    wait('Freed big chunk of memory')
 
 
if __name__ == '__main__':
    main()

