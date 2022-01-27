__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'


def main():
    S1= {10, 20, 30, 40, 50, 60}
    S2= {40, 50, 60, 70, 80, 90}
    
    S1.update({55,66})
    print('i.   S1: {}'.format(S1))
    S1.difference_update([10,30]) 
    print('ii.  S1: {}'.format(S1))
    pos = [x for x in S1].count(40)
    print('iii. Present: {}'.format("Present" if pos>0 else 'Not Present'))
    print('iv.  Union of S1 and S2: {}'.format(S1.union(S2)))
    print('v.   Intersection of S1 and S2: {}'.format(S1.intersection(S2)))
    print('vi.  S1-S2: {}'.format(S1-S2))
    
if __name__ == '__main__':
    main()
