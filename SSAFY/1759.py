# 최소 한 개의 모음(a, e, i, o, u)
# 최소 두 개의 자음으로 구성되어 있다고 알려져 있다
# 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된
def permatation(arr,r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return
        
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                chosen.pop()
                used[i]= 0
    generate([], used)
 
N, M = map(int,input().split()) # 암호의 길이  / 전체 문자 갯수
arr = list(input().split())
gather = ['a','e','i','o','u']
must_have = []
non_have = []
for i in arr:
    if i in gather:
        must_have.append(i)
    else:
        non_have.append(i)

for r in range(len(must_have)):
    permatation(must_have,i)
for k in range()

