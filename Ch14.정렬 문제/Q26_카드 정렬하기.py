# 0808
# 카드 정렬하기
# idea: 우선 순위 큐 사용
import heapq
import sys

heap = []
for i in range(int(sys.stdin.readline().rstrip())):
    heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

ans = 0
while len(heap) != 1:
    f = heapq.heappop(heap) # 가장 작은 값
    s = heapq.heappop(heap) # 그 다음 작은 값
    num = f + s
    ans += num
    heapq.heappush(heap, num)

print(ans)