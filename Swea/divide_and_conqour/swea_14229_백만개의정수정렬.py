def quick_select(arr,k):
    pivot = arr[len(arr)//2]
     
    left = [x for x in arr if x < pivot]
    mid = [ x for x in arr if x ==pivot]
    right = [ x for x in arr if x > pivot]
 
    if k < len(left):
        return quick_select(left,k)
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return quick_select(right,k-len(left)-len(mid))
 
arr = list(map(int,input().split()))
print(quick_select(arr,500000))