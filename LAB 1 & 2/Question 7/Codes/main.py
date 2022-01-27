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
    D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
    writeToFile('question7.txt', [(', '.join([str(x), str(D[x])])) for x in D])

if __name__ == '__main__':
    main()
