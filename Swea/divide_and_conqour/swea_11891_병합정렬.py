def merge_sort(arr):
    if len(arr)<= 1:
        return arr
    mid = len(arr)// 2   
    left = arr[:mid]
    right = arr[mid:]
 
    left_sort = merge_sort(left)
    right_sort = merge_sort(right)
 
    return merge(left_sort,right_sort)
 
def merge(left,right):
    global cnt 
    result = []
    i, j =0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[-1] > right[-1]:
        cnt += 1
    result += left[i:]
    result += right[j:]
    return result
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    new_arr = merge_sort(arr)
    print(f'#{t}',new_arr[N//2],cnt)