__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'


def writeToFile(filename, data):
    print('Writes the output to the file')
    file = open(filename, 'w+')
    for x in data:
        file.write(x)
        file.write('\n')
    print(data)
    file.close()


def main():
    L={"One","Two","Three","Four","Five"}
    writeToFile('question8.txt', [(', '.join([x, str(len(x))])) for x in L])

if __name__ == '__main__':
    main()
