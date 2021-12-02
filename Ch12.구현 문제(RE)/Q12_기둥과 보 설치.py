def possible(answer):
    for x, y, a in answer:
        if not a:  # 기둥
            # 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있는 경우
            if not y or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        if a:  # 보
            # 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결 되어 있는 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b, in build_frame:
        if not b:  # 삭제
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        if b:  # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))