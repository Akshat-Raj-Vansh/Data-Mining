__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import numpy as np


def findAverage(data):
    avg = sum(data)/len(data)
    return avg


def main():
    D = {'Akshat': {'Physics': 95, 'Chemistry': 91, 'Maths': 99, 'Computer': 92, 'English': 88},
         'Raj': {'Physics': 80, 'Chemistry': 92, 'Maths': 100, 'Computer': 95, 'English': 87},
         'Vansh': {'Physics': 92, 'Chemistry': 95, 'Maths': 92, 'Computer': 99, 'English': 90}}
    print('Marks of each Student:')
    print(D)
    A ={}
    for i in range(0,len(D)):
        A[list(D.keys())[i]]=findAverage(list((list(D.values())[i]).values()))
    print('Average Marks of each Student:')
    print(A)
    minAvg = np.min(list(A.values()))
    maxAvg = np.max(list(A.values()))
    print('Minimum average marks is of: {}'.format(list(A.keys())[list(A.values()).index(minAvg)]))
    print('Maximum average marks is of: {}'.format(list(A.keys())[list(A.values()).index(maxAvg)])) 
if __name__ == '__main__':
    main()
