def comb(depth,curr_sum):
    global min_val
    if curr_sum  >= min_val:
        return
     
    if depth == N: # depth = row
        if curr_sum < min_val:
            min_val = curr_sum 
        return
     
    for col in range(N): # col
        if not visited[col]:
            visited[col] = True
            comb(depth+1,curr_sum + grid[depth][col])
            visited[col] = False
 
 
T= int(input())
 
for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    result = []
    min_val = float('inf')
    visited = [False]*N # col
 
    answer = comb(0,0)
    print(f'#{t}', min_val)