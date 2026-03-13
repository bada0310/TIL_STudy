def check_queen(N):
    ans = 0
    board = [0]*N # idx = row, val = col 
    def is_safe(row,col):
        for i in range(row):
            if board[i] == col or abs(board[i]-col) == abs(i-row):
                return False
        return True
    def dfs(row):
        nonlocal ans
        if row == N:
            ans += 1
            return
         
        for col in range(N):
            if is_safe(row,col):
                board[row] = col
                dfs(row+1)
    dfs(0)
    return ans
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    grid = [[0]*N for _ in range(N)]
    answer= check_queen(N)
    print(f'#{t}',answer)