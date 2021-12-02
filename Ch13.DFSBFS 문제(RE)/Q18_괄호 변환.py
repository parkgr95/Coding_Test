def balanced(s):
    res = 0
    for i, v in enumerate(s):
        if v == '(':
            res += 1
        else:
            res -= 1
        if res == 0:
            return i + 1
    return len(s)

def proper(s):
    res = 0
    for c in s:
        if c == '(':
            res += 1
        else:
            res -= 1
            if res < 0:
                return False
    return True

def reverse(s):
    res = ""
    for c in s:
        if c == '(':
            res += ')'
        else:
            res += '('
    return res

def solution(p):
    answer = ''
    if p == '' or proper(p):
        return p
    u, v = p[:balanced(p)], p[balanced(p):]
    if proper(u):
        answer += u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += reverse(u[1:-1])
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))