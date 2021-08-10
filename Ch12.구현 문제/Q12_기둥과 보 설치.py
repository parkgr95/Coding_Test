# 0803
# 기둥과 보 설치
# idea: 전형적인 시뮬레이션 문제다. 조건에 따라 코드를 만든다.
def possible(answer):
    for x, y, stuff in answer:
        # 기둥일 때
        if stuff == 0:
            # 바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥 위라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보일 때
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, op = frame
        # 삭제하는 경우
        if op == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        # 설치하는 경우
        if op == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))