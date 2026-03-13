def dfs(idx, change):
    global min_change
 
    if change > min_change:
        return
    if idx + arr[idx] >= N-1:
        if change < min_change:
            min_change = change
        return
    for i in range(arr[idx],0,-1):
        dfs(idx + i, change +1)
         
T = int(input())
for t in range(1,T+1):
    N, *arr = map(int,input().split())
    result = []
    min_change = float('inf')
    dfs(0,0)
    print(f'#{t}',min_change)