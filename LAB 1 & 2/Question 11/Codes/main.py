__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import time

def isPrime(x):
    if x>1:
        for i in range(2, int(x**(1/2))+1):
            if x % i == 0 : return False
        return True
    return False

def main():
    start = time.time()
    print('Prime numbers between 1 to 1000')
    for i in range(1, 1001):
        if isPrime(i):
            print(i, end=',')
    end = time.time()
    print('\nTime taken by the program: {}'.format(end-start))


if __name__ == '__main__':
    main()
