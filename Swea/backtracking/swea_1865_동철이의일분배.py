def comb(depth, curr_val):
    global max_val
    if curr_val <= max_val: #pruning
        return
    if depth == N:
        if curr_val > max_val:
            max_val = curr_val
        return
     
    for col in range(N):
        if not visited[col]:
            visited[col] =True
            comb(depth+1,curr_val*grid[depth][col]/100)
            visited[col] =False
 
T= int(input())
 
for t in range(1,T+1):
    N =int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    # result = []
    max_val = 0
    visited = [False]*N
 
    comb(0,1)
    print(f'#{t} {max_val*100:.6f}')