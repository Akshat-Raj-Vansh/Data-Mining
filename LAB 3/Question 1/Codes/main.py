__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import random
import string
import os


def generateRandomLines():
    text = []
    for i in range(0, 20000):
        text.append(''.join(random.choices(
            string.ascii_letters+string.digits, k=20))+'\n')
    return text


def writeToFile(filename):
    file = open(filename.encode('unicode_escape'), 'w+')
    randomString = generateRandomLines()
    file.writelines(randomString)
    file.close()

def readFile(filename):
    file = open(filename.encode('unicode_escape'), 'r+')
    file.close()

def main():
    directory = os.getcwd()
    directory = directory[:directory.rfind("\\")]
    filename = directory+'\Files\textfile'
    for i in range(1, 501):
        writeToFile(filename+str(i)+'.txt')


if __name__ == '__main__':
    main()
