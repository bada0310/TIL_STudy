# 연속인 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상
# 들어오는 숫자가 중요하지 않음 그냥 안에 존재하면 됌 

T = int(input())

for t in range(1,T+1):
    arr = list(map(int,input().split()))
    play1 = []
    play2 = []
    ans = 0 

    for i in range(len(arr)):
        if i%2 == 0:
            play1.append(arr[i])
            play1.sort()
            if len(play1) >= 3:
                for k in range(len(play1)-2):
                    if play1[k] == play1[k+1] == play1[k+2]:
                        ans = 1
                        break
                    if play1[k]+1 in play1 and play1[k]+2 in play1:
                        ans = 1
                        break
        else:
            play2.append(arr[i])
            play2.sort()
            if len(play2) >= 3:
                for k in range(len(play2)-2):
                    if play2[k] == play2[k+1] == play2[k+2]:
                        ans = 2
                        break
                    if play2[k]+1 in play2 and play2[k]+2 in play2:
                        ans = 2
                        break
        if ans != 0:
            break                 

    print(f'#{t}',ans)

        
