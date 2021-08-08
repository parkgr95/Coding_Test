# 0808
# 실패율
# idea: 정렬 함수 사용
def solution(N, stages):
    ans = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        ans.append((i, fail))
        length -= count

    answer = sorted(ans, key=lambda t: -t[1])
    answer = [i[0] for i in answer]
    return answer