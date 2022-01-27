__author__ = 'Akshat Raj Vansh'
__version__ = '0.1.0'
__license__ = 'MIT'


import random
import string


def randomString():
    print('i. 100 random strings whose length is between 6 to 8: ')
    for i in range(1,101):
        str = ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice([6,7,8])))
        print(str,end= ' ')
        if i%10==0:
            print('')
       
def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if x%i==0: return False
        return True
    return False

def divisibleBy7and9(x):
    if x%7 ==0 and x %9 ==0: return True
    return False

def printPrime():
    print('ii. All Prime numbers between 600 to 800: ')
    for i in range(600, 801):
        if isPrime(i): print(i, end=' ')
    
def printNumbers():
    print('iii. All Numbers between 100 and 1000 that are divisible by 7 and 9: ')
    for i in range(100, 1001):
        if divisibleBy7and9(i): print(i, end=' ')
        
def main():
#    randomString()
#    printPrime()   
    printNumbers()
  
    
if __name__ == '__main__':
    main()
