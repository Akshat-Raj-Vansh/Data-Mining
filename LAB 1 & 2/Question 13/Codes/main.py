__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import random
import time 

def timeToSort(size):
    L = list(range(size))
    random.shuffle(L)
    begin = time.time()
    L.sort()
    end = time.time()
    print('Time taken to sort a list of {s} elements is {t}'.format(s=size,t= end-begin))


def main():
    for i in range(5000,25001,5000):
        timeToSort(i)

if __name__ == '__main__':
    main()
