import fibo
import sys
''' This fibo.py should be in the same directiory '''

def prn_fibo(n):
    fl=fibo.fib(n)
    print(fl)

if __name__ == '__main__':
    if len(sys.argv) >1 :
        prn_fibo(int(sys.argv[1]))
        print(sys.argv[0])
    else:
        prn_fibo(100)
