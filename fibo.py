def fib(n):
    a,b=0,1
    result= []

    while a <n:
        result.append(a)
        a,b=b,a+b
    return result

if __name__=='__main__':
    import sys
    n=10#int(sys.argv[1])
    l=fib(n)
    print(l)
