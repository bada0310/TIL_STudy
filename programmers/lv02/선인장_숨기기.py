## m * n grid base / w * h detact area
## 1 ≤ m, n ≤ 500,000 ## 1 ≤ h, w ≤ 500,000
## 1. m* n 사이즈의 grid 를 만들고 drops 에 떨어진 순서대로 표시한다.
## 2. 그리고 bfs 로 탐색하면서 영역 내의 값이 젤 크도록 찾아본다. -> 이거도 쓸필요가 없다? 
## 3. 찾는 순서는 좌상단 기준, 아예 w*H 모든 영역이 다 -1 이거나 아니면 양수인 가장 큰 숫자가 있도록? 하기? 이게 어려움

### 1차 시간 초과-> prunning 필요해보임-> 이것도 아니었음 이분탐색과 누적합을 하랜다?
### 그게 뭔데 

#### 2차원 누적합 (마법의 $O(1)$ 탐색)
def solution(M, N, H, W, drops): 
    grid = [[int(1e9)]*N for _ in range(M)]
    order = 1 
    for di, dj in drops: 
        grid[di][dj] = order
        order += 1 # 비가 내리는 순서 기록하기 

    max_safe_time = -1
    answer = [0,0]
    for i in range(0,M-H+1):
        for j in range(0,N-W+1):
            curr_min_time = int(1e9)

            for r in range(i, i+H):
                row_min = min(grid[r][j:j+W])
                curr_min_time = min(curr_min_time, row_min) # 슬라이싱으로 빠르게
                pass 
                # for c in range(j, j+W):
                #     if grid[r][c] != -1: # -1 이 아니라면(비가 내렸다면?)
                #         curr_min_time = min(curr_min_time, grid[r][c]) # 시간 업데이트 가장 작은 시간으로 
                #         pass
    # 최종 조건 비교  
            # 1.(비를 안맞은 경우) 아예 모두가 -1 인 경우가 존제한다면 그것이 답
            if curr_min_time == int(1e9):
                return [i,j]
            # 2.(비를 맞은 경우) 숫자가 가장 큰 경우, max_safe_time 과 answer 를 갱신 
            elif curr_min_time > max_safe_time:
                max_safe_time = curr_min_time
                answer = [i,j]
    
    
    return answer
## --------------------------------------------------------------
# 이분 탐색 및 누적합 
## 4 중 for 문은 너무 시간 복잡도가 크다 
### 질문 방식을 뒤집어 보자-> 애당초에 H*W 인 자리가 존재해? -> O / X 
### 누적합으로 위 질문의 답이 존재하는지 확인 
def solution(M, N, H, W, drops): 
    grid = [[int(1e9)]*N for _ in range(M)]
    order = 1 
    for x, y in drops: # 비 표시하기 
        grid[x][y] = order
        order += 1 

    def check(T):
        # 1. 크기가 (M+1) x (N+1)인 0으로 채워진 누적합 배열 P 준비
        P = [[0]*(N+1) for _ in range(M+1)]
        # 2. 누적합 계산
        for r in range(1, M+1):
            for c in range(1, N+1):
                is_danger = 1 if grid[r-1][c-1] <= T else 0 
                P[r][c] = is_danger + P[r-1][c] + P[r][c-1] - P[r-1][c-1]
        # 3. H*W 영역 구역합 게산 
        for i in range(M-H+1):
            for j in range(N-W+1):
                area_sum = P[i+H][j+W] - P[i][j+W] - P[i+H][j] + P[i][j]
                if area_sum == 0:
                    return [i, j]
        return None
    ## 선언 
    ## 이분 탐색 
    left = 0
    right = len(drops)
    answer = [0,0]

    while left <= right:
        mid = (left + right) // 2
        result = check(mid)

        if result is not None:
            answer =result
            left = mid + 1
        else:
            right = mid - 1
    return answer 

        
    

    
