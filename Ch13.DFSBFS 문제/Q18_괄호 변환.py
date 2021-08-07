# 0804
# 괄호 변환
# idea: 구현

# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # u가 올바른 괄호 문자열이면, v를 함수로 수행한 결과를 붙혀 반환
    if proper(u):
        answer += u + solution(v)
    # u가 올바른 괄호 문자열이 아니면,
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer