__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'


def main():
    D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
    D[8] = 8.8
    print('i.   D: {}'.format(D))
    D.pop(2)
    print('ii.  D: {}'.format(D))
    pos = [x for x in D.keys()].count(6)
    print('iii. Present: {}'.format(pos if pos>0 else 'Not Present'))
    print('iv.  Number of elements in D: {}'.format(len(D.values())))
    sumofDict = sum([x for x in D.values()])
    print('v.   Sum of all values: {}'.format(sumofDict))
    D[3] = 7.1
    print('vi.  D: {}'.format(D))
    print('vii. Clearing all elements in L: {}'.format(D.clear()))


if __name__ == '__main__':
    main()
