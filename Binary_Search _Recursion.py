
def binary_search(data,target,low,high):
    if low > high :
        return False
    else :
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif  target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)




arr = [2,3,4,10,40]
x = 10

result = binary_search(arr,x,0, len(arr)-1)
print(int(result))
if result >=0 :
   print(int(result))
else:
    print("Element is not present in List ")