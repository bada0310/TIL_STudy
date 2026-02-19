def backtrack(row):
    global answer
    if row == N:
        answer += 1
        return
    for col in range(N):
        if not columns[col] and not diag1[row+col] and not diag2[col-row+N-1]:
            columns[col] = True
            diag1[row+col] = True
            diag2[col-row+N-1] = True
            backtrack(row + 1)
            columns[col] = False
            diag1[row+col] = False
            diag2[col-row+N-1] = False
 
for t in range(1, 1+int(input().strip())):
    N = int(input().strip())
    answer = 0
    columns = [False] * N
    diag1 = [False] * (2*N-1)   # row + col
    diag2 = [False] * (2*N-1)   # col - row + N - 1
     
    backtrack(0)
    print(f'#{t}', answer)