def dfs(curr_node, cnt, curr_cost):
    global min_cost
     
 
    if curr_cost > min_cost:
        return
    if cnt == N:
        if grid[curr_node][0] != 0:
            min_cost = min(min_cost, curr_cost + grid[curr_node][0])
        return
 
    for next_node in range(N):
        if not visited[next_node] and grid[curr_node][next_node] != 0:
            visited[next_node] = True
            dfs(next_node,cnt +1,curr_cost + grid[curr_node][next_node])
            visited[next_node] = False
 
 
 
T = int(input())
for t in range(1,T+1):
    N = int(input()) # total num 
    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [False]*(N)
 
    dir  = [(1,0),(0,1)]
    min_cost = float('inf')
 
    visited[0] = True # 시작지점 정의 조심!! 
    dfs(0,1,0)
    print(f'#{t}',min_cost)