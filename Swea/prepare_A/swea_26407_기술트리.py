from collections import deque
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    tree =[[] for _ in range(N+1)] # tree= {}
    indgree =[0]*(N+1) # 진입차수 계산 
     
    for i in range(1,N+1):
        arr = list(map(int,input().split()))
        count = arr[0]
         
        if count > 0:
            parents = arr[1:]
            for p in parents:
                tree[p].append(i)
                indgree[i] += 1
    q = deque()
    for i in range(1,N+1):
        if indgree[i] ==0:
            q.append((i,1))
 
    learn_cnt = 0
    max_turn = 0
     
    while q:
        curr, turn = q.popleft()
        learn_cnt += 1
        max_turn =max(max_turn,turn)
         
        for next in tree[curr]:
            indgree[next] -=1
            if indgree[next] == 0:
                q.append((next,turn+1))
                 
    if learn_cnt == N:
        ans = max_turn
    else:
        ans = -1
    print(f'#{t}',ans)