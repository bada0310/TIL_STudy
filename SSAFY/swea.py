def in_order(idx):
    if idx > N:
        return
    in_order(idx*2) # 재귀로 호출  # left 
    print(tree_val[idx], end = '')
    in_order(idx*2 +1)# 재귀로 호출  # right 

for t in range(1, T+1):
    N = int(input())
    tree_val = [0]*(N+1)
    for _ in range(N): 
        data= input().split() # idx, val, child, node 
        node_idx = int(data[0])
        node_val = data[1]
        child = list(map(int,data[2:]))
        tree_val[node_idx] = node_val
    in_order(1)
    print()
