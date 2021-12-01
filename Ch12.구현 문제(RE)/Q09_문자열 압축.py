def solution(s):
    ans = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        tmp = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if s[j:j+i] != tmp:
                compressed += str(cnt) + tmp if cnt > 1 else tmp
                tmp = s[j:j+i]
                cnt = 1
            else:
                cnt += 1
        compressed += str(cnt) + tmp if cnt > 1 else tmp
        ans = min(ans, len(compressed))
    return ans

print(solution("aabbaccc"))