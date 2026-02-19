import sys
input = sys.stdin.readline
N = int(input())
count = 0
for _ in range(N):
    word = input().strip()
    stack = []
    for i in word:
        if stack and stack[-1] == i:   # stack[-1] == top 
            stack.pop()
        else:
            stack.append(i)
    if not stack: # stack 에 존재하는 원소가 없으면 
        # 아치선이 겹치지 않게 짝이 맞추어진것임으로 count 를 올린다. 
        count += 1

print(count)