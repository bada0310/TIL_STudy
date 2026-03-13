def is_range(r,c, N):
    return 0<= r < N and 0<= c < N 
 
# 중복이지만 나눠서 저장해줘야 함 
def dfs(r,c):
    global min_num
    stack = [(r,c,grid[r][c])] # curr_num 
    dist[r][c] = grid[r][c] 
 
    while stack:
        curr_x, curr_y, curr_num= stack.pop()
 
        if curr_num > dist[curr_x][curr_y]: # greedy
            continue
 
        for dx, dy in dir:
            nx, ny = curr_x + dx ,curr_y + dy
            if is_range(nx,ny,N):
                next_num = curr_num + grid[nx][ny]
                if next_num < dist[nx][ny]:
                    dist[nx][ny] = next_num
                    stack.append((nx,ny,next_num))
 
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    num = 0
 
    dfs(0,0)
    print(f'#{t}',dist[N-1][N-1])