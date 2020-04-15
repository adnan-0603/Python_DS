###when a fucntion makes two recursive ,we say it uses binary recursion .

def binary_sum(S,start,stop):
    if start >= stop :
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start +stop) // 2
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop)

