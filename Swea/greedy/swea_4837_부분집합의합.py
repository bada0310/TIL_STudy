# 1부터 12까지의 숫자를 원소로 가진 집합 A
# N개의 원소를 갖고 있고, 원소의 합이 K
def comb(depth,start):
    global cnt
    if depth == N:
        if sum(result) == M:
            cnt += 1
            return
    for i in range(start,13):
            result.append(i)
            comb(depth +1,i+1)
            result.pop()

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    # arr = [i for i in range(1,13)]
    result = []
    cnt = 0
    comb(0,1)
    print(f'#{t}', cnt)
