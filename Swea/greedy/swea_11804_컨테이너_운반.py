# 각 트럭에 대해서, 최대 적재량까지 적재하기 (max_val)
# 트럭당 한 개의 컨테이너를 운반 할 수 있음

T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split()) # N =box M =Truck
    arr = list(map(int,input().split())) # box_weight
    truck = list(map(int,input().split())) # truck_weight
    truck.sort(reverse=True)
    arr.sort(reverse=True)
    ans = 0 
    box_idx = 0
    truck_idx = 0
    result = []
    while box_idx < N and truck_idx < M:
        if arr[box_idx] <= truck[truck_idx]:
            ans += arr[box_idx]
            truck_idx += 1
            box_idx += 1
        else:
            box_idx += 1
    print(f'#{t}',ans)

    

