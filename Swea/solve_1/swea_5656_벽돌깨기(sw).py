from collections import deque
dx, dy = [0,1,0,-1], [1,0,-1,0]
# 범위내에 존재하는지
def is_range(r,c):
    return 0<= r < H and 0<= c < W
# 터트리기 
def bomb(r,c, curr_grid):
    q = deque([(r,c, curr_grid[r][c])])
    curr_grid[r][c] = 0 # bomb 

    while q:
        cx, cy, delta = q.popleft()

        if delta == 1:
            continue

        for i in range(4):
            for d in range(1,delta):
                nx, ny = cx + dx[i]*d, cy + dy[i]*d
                if is_range(nx,ny) and curr_grid[nx][ny] > 0:
                    q.append((nx,ny,curr_grid[nx][ny]))
                    curr_grid[nx][ny] = 0
# 중력 
def gravity(curr_grid):
    for c in range(W):
        temp = []
        for r in range(H):
            if curr_grid[r][c] > 0:
                temp.append(curr_grid[r][c])
        for r in range(H-1,-1,-1):
            if temp:
                curr_grid[r][c] = temp.pop()
            else:
                curr_grid[r][c] = 0
# N= 될때까지 진행 
def dfs(depth, curr_grid):
    global min_brick
    if min_brick == 0:
        return
    
    if depth == N:
        cnt = sum(1 for row in range(H) for col in range(W) if curr_grid[row][col]>0)
        min_brick = min(min_brick,cnt)
        return
    
    # 넓게 어디로 떨어뜨릴 지 고민
    for c in range(W):
        r = -1
        for i in range(H):
            if curr_grid[i][c] >0:
                r = i
                break
        if r == -1:
            continue
        
        next_grid =[row[:] for row in curr_grid]
        bomb(r,c,next_grid)
        gravity(next_grid)
        dfs(depth+1, next_grid)
    cnt = sum(1 for row in range(H) for col in range(W) if curr_grid[row][col]>0)
    min_brick = min(min_brick,cnt)

T= int(input())
for tc in range(1,T+1):
    N , W , H =map(int,input().split()) # ball, grid (height, width)
    grid = [list(map(int,input().split())) for _ in range(H)]
    min_brick = float('inf')

    dfs(0,grid)
    print(f'#{tc}', min_brick)



