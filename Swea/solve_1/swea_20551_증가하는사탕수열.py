T = int(input())

for t in range(1,T+1):
    a, b, c = map(int,input().split())
    cnt = 0
    if b >= c:
        red = b - (c-1)
        cnt += red
        b = c -1
    if a >= b:
        red = a - (b-1)
        cnt += red
        a = b- 1
        if a<= 0  or b <= 0 or c <= 0:
            cnt = -1
    print(f'#{t}',cnt)
    


        




















# 강사님 필기 
# T = int(input())
# N = int(input())
# grid = [list(map(int,input().split())) for _ in range(N)]

# def find_min(r,c):
#     if r == 0 and c == 0:
#         return grid[0][0]
#     # 위의 답
#     up = left = float('inf')
    
#     if r>0:
#         up = find_min(r-1,c)
#     # 왼쪽의 답
#     if c>0:
#         left = find_min(r,c-1)
#     return min(up,left) + grid[r][c]
# ans = find_min(N-1,N-1)