#author --> Adnan chowdhury

def good_fibonacci(n):
    if n <=1 :
        return(n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b,a)

for n in range(1,11):
    print(n, ":" ,good_fibonacci(n))