
def recursion(n):
    if n == 0:
        return 1
    else:
        result = n * recursion(n-1)
        print(result)
        return result

print(recursion(5))