__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import time
import os
import random
import string


def encodeString(word):
    return word.encode('unicode_escape')


def updateFile(filename):
    file = open(encodeString(filename), 'r')
    originalText = file.read()
    file.close()
    file = open(encodeString(filename), 'w+')
    originalText = originalText.splitlines(keepends=True)
    updatedText = [x.upper() for x in originalText]
    file.writelines(updatedText)
    file.close()


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


def rollback():
    directory = os.getcwd()
    directory = directory[:directory.rfind("\\")]
    filename = directory+'\Files\\textfile'
    for i in range(1, 501):
        writeToFile(filename+str(i)+'.txt')


def writeResults(result):
    file = open('result.csv', 'w+')
    row_out = []
    res_out = []
    for row in result:
        row_out.append(','.join(x for x in row))
    for res in row_out:
        res_out.append('\n'.join(x for x in row_out))    
    file.writelines(res_out)
    file.close()

def main():
    directory = os.getcwd()
    directory = directory[:directory.rfind("\\")]
    filename = directory+'\Files\\textfile'

    table = [['No. of Files', 'Time Taken (sec)']]
    for j in range(1, 6):
        rollback()
        begin = time.time()
        for i in range(1, j * 100 + 1):
            updateFile(filename+str(i)+'.txt')
        end = time.time()
        table.append([str(j*100), str(end-begin)])
        print('Finished updating {n} files in {t} seconds'.format(n=j*100, t= end-begin))
    writeResults(table)


if __name__ == '__main__':
    main()
