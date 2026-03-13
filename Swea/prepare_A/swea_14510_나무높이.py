T = int(input())
 
for t in range(1,T+1):
    N  = int(input())
    arr = list(map(int,input().split()))
     
    top_tree = max(arr)
    odd = 0
    even = 0 
     
    for i in range(N):
        diff = top_tree - arr[i]
        if diff > 0: 
            odd += diff%2
            even += diff//2
    while even > odd+1:
        even -= 1
        odd += 2
    if odd > even:
        time = odd * 2 - 1
    else:
        time = even * 2
         
    print(f'#{t}',time)