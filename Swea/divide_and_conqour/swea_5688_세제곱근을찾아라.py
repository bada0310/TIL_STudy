def solve(n):
    start = 1
    end = n
    while start <= end:
        mid = (start + end)//2
        mid_3 = mid **3
        if mid_3 == n:
            return mid
        elif mid_3 < n:
            start = mid +1
        elif mid_3 > n:
            end = mid -1
    return -1
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    ans = solve(N)
    print(f'#{t}',ans)