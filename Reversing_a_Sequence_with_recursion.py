
def reverse(S,start,stop):
    if start < stop - 1:
        S[start],S[stop-1] = S[stop-1],S[start]
        reverse(S,start+1,stop-1)



S=[9,8,7,6,5,4,3,2,1]
print(reverse(S,3,7))