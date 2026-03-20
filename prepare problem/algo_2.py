
T = int(input())

#dfs 탐색
def dfs(cur_node, cur_val, cur_weight):
    global answer
    #종료 조건: 현재 무게가 k를 넘은 경우
    if cur_weight > K:
        return
    #갱신 조건: 현재 가치가 현재 정답보다 큰경우
    if cur_val >= answer:
        answer = cur_val

    #왼쪽 자식이 있을 경우
    if left[cur_node] != -1:
        dfs(left[cur_node], cur_val, cur_weight)
        dfs(left[cur_node], cur_val+nodes[left[cur_node]][1], cur_weight+nodes[left[cur_node]][0])
    #오른쪽 자식이 있을 경우
    if right[cur_node] != -1:
        dfs(right[cur_node], cur_val, cur_weight)
        dfs(right[cur_node], cur_val+nodes[right[cur_node]][1], cur_weight+nodes[right[cur_node]][0])

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    #부모 값을 저장할 리스트
    parent = [-1] * (N+1)
    #왼쪽 자식을 저장할 리스트
    left = [-1] * (N+1)
    #오른쪽 자식을 저장할 리스트
    right = [-1] * (N+1)
    #시작 노드
    root = -1
    #무게, 가치
    nodes =[(0,0) for _ in range(N+1)]
    for _ in range(N):
        r, w, v, p = map(int, input().split())
        if p == 0:
            root = r
        else:
            parent[r] = p
        nodes[r] = (w, v)
    #parent 배열을 돌면서 왼쪽, 오른쪽 자식 관계 저장
    for i in range(N+1):
        if parent[i] != -1:
            if left[parent[i]] != -1:
                right[parent[i]] = i
            else:
                left[parent[i]] = i
    answer = 0
    #시작 방의 보물을 가져가지 않았을 때
    dfs(root, 0, 0)
    #시작 방의 보물을 가져갔을 때
    dfs(root, nodes[root][1], nodes[root][0])
    print(f'#{test_case} {answer}')