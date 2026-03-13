# 탐색 방향의 교차 여부
def binary_search(target,data,N):
    global cnt 
    start = 0
    end = N-1
    flag = 0 # 1= left 2= right 
     
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            cnt += 1
            return
        elif data[mid] < target:
            if flag == 1:
                break
            start = mid +1
            flag = 1
        elif data[mid] > target:
            if flag ==2:
                break
            end = mid -1
            flag = 2
    return
 
T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split())) # N 
    B = list(map(int,input().split())) # M 
    A.sort()
    cnt = 0
 
    for i in range(M):
        binary_search(B[i],A,N)
    print(f'#{t}',cnt)