
def linear_sum(S,n):
    if n == 0:
        return 0
    else :
        return linear_sum(S,n-1)+ S[n-1]



S = [1,2,3,4,5,19,20]
print(linear_sum(S,7))


print(type(S))