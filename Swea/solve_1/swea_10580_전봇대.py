# 교차점 발생
# 새로운 선이 
# 1. 기존의 선보다 시작점 up 도착점 down
# 2. 기존의 선보다 시작점 dow 도착점 up
# 새로운 선이 들어오면 , 기존의 모든 선들과 비교
# 완탐
# O(n^2)

T= int(input())

for tc in range(1,T+1):
    N =int(input())
    wires = []
    ans = 0 # 교차점 
    for _ in range(N):
        s, e = map(int,input().split())

        for pre_s, pre_e in wires:
            if s < pre_s and e > pre_e:
                ans += 1
            if s > pre_s and e < pre_e:
                ans += 1
        wires.append((s,e))
    print(f'#{tc}', ans)
