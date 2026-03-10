# DP (점화식 풀이)
N = int(input())
t = []
p = []

for _ in range(1,N+1):
    time, cost = map(int,input().split())
    t.append(time)
    p.append(cost)

dp =[0]*(N+1)
for i in range(N-1,-1,-1):
    if i + t[i] <= N:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])