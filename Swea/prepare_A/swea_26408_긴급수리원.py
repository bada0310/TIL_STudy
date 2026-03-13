def length(result):
    # result = [(r, c),(r, c),(r, c)]
    curr_x = curr_y = 0
    dist = 0
 
    for val,r,c in result:
        dist += (abs(curr_x -r) + abs(curr_y - c))
        curr_x, curr_y = r,c
    return dist
 
def perm(depth):
    global min_dist
 
    if depth == K:
        dist = length(result)
        min_dist = min(dist, min_dist)
        return min_dist
     
    for i in range(K):
        if not visited[i]:
            val, r, c = arr[i]
            if val <0:
                if not any(v == -val for v , r_pos, c_pos in result):
                    continue
            visited[i] = True
            result.append(arr[i])
 
            perm(depth+1)
 
            result.pop()
            visited[i] =False
 
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    min_dist = float('inf')
    arr = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                arr.append((grid[i][j], i,j))
    K = len(arr)
    visited = [False]*K
    result = []
    perm(0)
 
    print(f'#{t}',min_dist)