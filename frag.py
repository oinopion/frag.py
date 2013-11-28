from lib import wait, alloc


def main():
    big = alloc(100000)
    wait('Wasted big chunk of memory')
    
    small = alloc(1)

    del big
    # import gc; gc.collect(2)
    wait('Freed big chunk of memory')
 
 
if __name__ == '__main__':
    main()

