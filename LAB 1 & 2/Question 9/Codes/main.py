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



def main():
    str = []
    for i in range(0, 100):
        print('Generating random strings')
        str.append(''.join(random.choices(string.ascii_letters +
                   string.digits, k=int(np.random.randint(10, 16, 1))))+'\n')
    print(str)
    writeToFile('question9.txt', str)

if __name__ == '__main__':
    main()
