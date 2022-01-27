__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import numpy as np
        
def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if x%i==0: return False
        return True
    return False


def main():
    L = np.random.randint(100, 901, 100)
    print('L: ',L)
    
    print('i.  All odd numbers: ')
    _odd = list(filter(lambda x: x%2!=0, L))
    _count = len(_odd)
    print('     Count: ', _count)
    print('     List: ', _odd)
    
    print('ii. All odd numbers: ')
    _even = list(filter(lambda x: x%2==0, L))
    _count = len(_even)
    print('     Count: ', _count)
    print('     List: ', _even)
    
    print('iii. All prime numbers: ')
    _primes = list(filter(lambda x: isPrime(x), L))
    _count = len(_primes)
    print('     Count: ', _count)
    print('     List: ', _primes)
  
    
if __name__ == '__main__':
    main()
