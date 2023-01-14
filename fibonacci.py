def fib(n):
    if 0<=n<=1:
        return n
    n1,n2=1,0
    #result=None
    for f in range(n-1):
        result=n2+n1
        n2=n1
        n1=result
    return result
for i in range(36):
    print(i, fib(i))

        
    