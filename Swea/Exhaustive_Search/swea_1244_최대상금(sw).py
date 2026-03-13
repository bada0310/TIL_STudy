def perm(depth):
    global max_num
 
    curr_val = int("".join(map(str,arr)))
 
    if (depth,curr_val) in visited:
        return
     
    visited.add((depth, curr_val))
    if depth == chance:
        if curr_val > max_num:
            max_num = curr_val
        return
     
    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
 
            perm(depth+1)
 
            arr[i], arr[j] = arr[j], arr[i]
#실행부 
T = int(input())
 
for t in range(1,T+1):
    a, b = input().split()
    N = len(a)
    result = []
    visited = set()
    arr = list(map(int,a))
    chance = int(b)
    max_num = 0 
     
    perm(0)
    print(f'#{t}',max_num)