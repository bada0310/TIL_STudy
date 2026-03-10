N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
min_diff = float('inf')

V =[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        V[i][j] = grid[i][j] + grid[j][i]

def dfs(idx, team_a):
    global min_diff
    team_b = []
    if len(team_a) == N//2:
        team_b = [i for i in range(N) if i not in team_a]
        
        sum_a = 0
        sum_b = 0
        
        for i in range(N//2):
            for j in range(i+1, N//2):
                sum_a += V[team_a[i]][team_a[j]]
                sum_b += V[team_b[i]][team_b[j]]
        
        min_diff = min(min_diff, abs(sum_a-sum_b))
        return
    
    for i in range(idx, N):
        team_a.append(i)
        dfs(i+1, team_a)
        team_a.pop() # 백트래킹 
dfs(0, [])
print(min_diff)