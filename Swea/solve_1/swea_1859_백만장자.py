# 시계열 뒤에세 부터 찾기 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    min_val = float('inf')
    ans= 0
    max_val = 0

    for i in range(N-1,-1,-1):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            ans += max_val - arr[i]
    print(f'#{tc}',ans)

    