import heapq
def is_range(r,c,N):
    return 0<= r < N and 0<= c < N 
 
def dijkstra(N, grid):
    inf = float('inf')
    dist = [[inf]*N for _ in range(N)]
 
    pd = []
    heapq.heappush(pd,(0,0,0))
    dist[0][0] =0
 
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
 
    while pd:
        curr_val, curr_x, curr_y = heapq.heappop(pd)
        if curr_x == N-1 and curr_y == N-1:
            return curr_val
         
        if curr_val > dist[curr_x][curr_y]:
            continue
 
        for dx, dy in dir:
            nx, ny = curr_x + dx, curr_y + dy
            if is_range(nx,ny,N):
                next_val = curr_val + grid[nx][ny]
 
                if next_val < dist[nx][ny]:
                    dist[nx][ny] = next_val
                    heapq.heappush(pd,(next_val,nx,ny))
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().strip())) for _ in range(N)]
    # visited = [[False]*N for _ in range(N)]
    # visited[0][0]
    # sr =sc =0 # S 
    # er= ec = N-1 # E
    ans = dijkstra(N,grid)
    print(f'#{t}',ans)