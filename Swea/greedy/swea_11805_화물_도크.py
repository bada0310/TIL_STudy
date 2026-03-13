T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        start, end = map(int,input().split())
        arr.append((end,start)) #  end,start
    arr.sort()
    cnt = 0
    time = 0
    for end, start in arr:
        if start >= time:
            cnt += 1
            time = end
    print(f'#{t}',cnt)

    # while time < 24:
    #     time += 1
    #     for i in range(len(arr)):
    #         while len(dock) < dock_len:
    #             dock.append(arr[i])
    #             cnt += 1

    #         if len(dock) == dock_len:
    #             for d in range(dock_len):
    #                 if dock[d][1] == time:
    #                     dock.pop(d)
    #                 else:
    #                     continue
    




