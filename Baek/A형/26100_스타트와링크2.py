# 못풂.. 비트마스킹? 써야함

import sys
input = sys.stdin.readline

# def pair(team):
#     score = 0
#     for i in range(2):
#         for j in range(2):
#             score += grid[team[i]][team[j]]
#     return score

def comb(depth,start):
    global min_abs
    if depth == N//2:
        score_a = 0
        score_b = 0

        for r in range(N):
            for c in range(N):
                if visited[r] and visited[c]:
                    score_a += grid[r][c]  
                elif not visited[r] and not visited[c]:
                    score_b += grid[r][c]  
        
        diff = abs(score_a - score_b)
        if diff < min_abs:
            min_abs = diff
        return
    
    for i in range(start,N):
        visited[i] =True
        comb(depth+1, i+1)
        visited[i] = False
        if min_abs == 0:
            return
        

N = int(input())
grid =[list(map(int,input().split())) for _ in range(N)]
min_abs = float('inf')
visited = [False]*N
visited[0] = True # 방문 배열로 확인하기 

comb(1,1)
print(min_abs)
    