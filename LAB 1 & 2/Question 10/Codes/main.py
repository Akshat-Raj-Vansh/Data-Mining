__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'


import string
import numpy as np
import random


def writeToFile(filename, data):
    print('Writes the output to the file')
    file = open(filename, 'w+')
    for x in data:
        file.write(x)
    print(data)
    file.close()


def isPrime(x):
    if x > 1:
        for i in range(2, int(x**(1/2))+1):
            if x % i == 0:
                return False
        return True
    return False


def main():
    primes = []
    for i in range(600, 801):
        print('Finding prime numbers')
        if isPrime(i):
            primes.append(str(i)+'\n')
    print(primes)
    writeToFile('question10.txt', primes)


if __name__ == '__main__':
    main()
