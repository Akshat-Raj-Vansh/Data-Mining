__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'


def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


def main():
    L = [11, 12, 13, 14]

    L.extend([50, 60])
    print('i.   L: {}'.format(L))

    L = [x for x in L if [11, 13].count(x) == 0]
    print('ii.  L: {}'.format(L))

    L.sort(reverse=False)
    print('iii. L: {}'.format(L))

    L.sort(reverse=True)
    print('iv.  L: {}'.format(L))

    pos = L.count(13) if L.count(13) != 0 else 'Not Present'
    print('v.   Position of 13: {}'.format(pos))

    print('vi.  Length of L: {}'.format(len(L)))

    print('vii. Sum of all elements: {}'.format(sum(L)))

    odd = [x for x in L if x % 2 != 0]
    print('viii.Sum of all ODD numbers in L: {}'.format(sum(odd)))

    even = [x for x in L if x % 2 == 0]
    print('ix.  Sum of all EVEN numbers in L: {}'.format(sum(even)))

    print('x.   Sum of all PRIME numbers in L: {}'.format(sum(x for x in L if isPrime(x))))

    print('xi.  Clearing all elements in L: {}'.format(L.clear()))

    del L


if __name__ == '__main__':
    main()
