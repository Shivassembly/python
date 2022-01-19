''' To determine prime number in a 1000
'''
prime =[]
for n in range(2,1000):
    for i in range(2,n):
        if n%i == 0:
            print(n,' euals ', i ,' * ' ,n//i)
            break
    else:
        print(n,'.. is PRIME number')
        prime.append(n)

print(prime)
