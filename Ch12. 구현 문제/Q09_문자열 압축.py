# 0731
# 문자열 압축
# idea: 각 단위마다 압축된 문자열의 길이를 비교해 가장 짧은 문자열의 길이를 출력한다.
def solution(s):
    answer = len(s)
    # 단위
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer