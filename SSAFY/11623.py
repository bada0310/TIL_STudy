# - 가장 위에 있는 카드를 가져와서 버린다.
# - 그 다음, 가장 위에 있는 카드를 가장 아래에 있는 카드 밑으로 옮긴다.
# from collections import deque
# 두쌍씩 움직인다. 굳이 모든 연산을 거쳐야 할 필요가 있는가? 

# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
    
#     if N == 1:
#         answer = 1
#     else:
#         k= 1
#         while k * 2 <= N:
#             k *= 2
#         if N == k:
#             answer = N
#         else:
#             answer = (N - k) * 2
#     print(f"#{t} {answer}")

from collections import deque

T = int(input())
for t in range(1, T+1):
    N = int(input())
    q = deque(list(range(1,N+1)))
    while q:
        temp = q.popleft()
        q.rotate(-1)
    print(f"#{t} {temp}")

        
    