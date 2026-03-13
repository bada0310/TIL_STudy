T = int(input())
 
for t in range(1,T+1):
    N = int(input())
    arr = [0]*200
    for _ in range(N):
        a, b = map(int,input().split())
        if a > b: 
            a, b = b, a
        a, b = (a-1)//2, (b-1)//2
        for i in range(a,b+1):
            arr[i] += 1
    print(f'#{t}',max(arr))