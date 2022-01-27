__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'

import numpy as np
        
def main():
    L1 = np.random.randint(10, 31, 10)
    L2 = np.random.randint(10, 31, 10)
    print('L1: ',L1)
    print('L2: ',L2)
    print('Minimum in L1: ', np.min(L1))
    print('Minimum in L2: ', np.min(L2))
    print('Maximum in L1: ', np.max(L1))
    print('Maximum in L2: ', np.max(L2))
    print('Sum of both the lists: ', L1+L2)
  
    
if __name__ == '__main__':
    main()
