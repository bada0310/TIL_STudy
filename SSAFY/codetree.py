n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
node_count = 0
for r in range(n):
    for c in range(n):
        start = grid[r][c]
        count = 0
        for i in range(4):
            
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < n and 0<= nc < n:
                if grid[nr][nc] == 1:
                    count += 1
                if count >= 3:
                    node_count += 1
print(node_count)   