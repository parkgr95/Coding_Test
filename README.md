Coding-Test
=============
이것이 취업을 위한 코딩 테스트다 with 파이썬- 문제풀이
-------------
* **CHAPTER 03 그리디**
	+ 그리디란
		- 현재 상황에서 지금 당장 좋은 것만 고르는 방법. 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않음.
	+ 예제
		- 3-1 [거스름돈](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-1.py)
		- 3-2 [큰 수의 법칙](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-2.py)
		- 3-3 [숫자 카드 게임](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-3.py)
		- 3-4 [1이 될 때까지](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-4.py)
	+ 정당성
		- 그리디 알고리즘은 탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있으면 매우 효과적이고 직관적이다.
		- 그리디 알고리즘 문제에서는 문제풀이를 위한 아이디어를 떠올리고 정당한 지 검토할 수 있어야 답을 도출할 수 있다.
		- ex) 거스름돈의 정당성 : 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없음헌
* * *
* **CHAPTER 04 구현**
	+ 구현이란
		- 피지컬을 요구하는 문제
		- 완전 탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
		- 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계식 차례대로 직접 수행하는 문제 유형
	+ 파이썬에서의 구현
		- 메모리 사용량 제한보다 더 적은 크기의 메모리를 사용해야 한다.
		- 알고리즘 문제를 풀 때는 시간 제한과 데이터의 개수를 먼저 확인한 뒤 어느 정도의 시간 복잡도의 알고리즘으로 작성해야 풀 수 있을 것인지 예측할 수 있어야 한다.
		- Pyp3를 이용하자
	+ 예제
		- 4-1 [상하좌우](https://github.com/parkgr95/Coding_Test/blob/main/Ch04.%EA%B5%AC%ED%98%84/4-1.py)
		- 4-2 [시각](https://github.com/parkgr95/Coding_Test/blob/main/Ch04.%EA%B5%AC%ED%98%84/4-2.py)
		- 4-3 [왕실의 나이트](https://github.com/parkgr95/Coding_Test/blob/main/Ch04.%EA%B5%AC%ED%98%84/4-3.py)
		- 4-4 [게임 개발](https://github.com/parkgr95/Coding_Test/blob/main/Ch04.%EA%B5%AC%ED%98%84/4-4.py)
* * *
* **CHAPTER 05 DFS/BFS**
	+ 자료구조
		- 데이터를 표현하고 관리하고 처리하기 위한 구조. 그중 스택과 큐는 자료구조의 기초 개념으로 다음의 두 핵심적인 함수로 구성된다.
		- 삽입(Push): 데이터를 삽입한다
		- 삭제(Pop): 데이터를 삭제한다.
	+ 스택
		- 선입후출(First In Last Out) or 후입선출(Last In First Out)
	+ 큐
		- 선입선출(First In First Out)
	+ 재귀 함수
		- 자기 자신을 다시 호출하는 함수. 종료 조건을 꼭 명시해야 한다.
		- 수학의 점화식(재귀식)을 소스코드로 옮겼기에 반복문을 이용하는 것에 비해 더 간결한 형태이다.
	+ 그래프
		- 노드(Node) 와 간선(Edge)로 표현된다. 다음과 같이 크게 2가지 방식으로 표현할 수 있다.
		- 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식.
		- 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식.
	+ DFS(Depth First Search)
		- 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.
		- 동작 과정
			1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
			2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
			3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
	+ BFS(Breadth First Search)
		- 너비 우선 탐색. 가까운 노드부터 탐색하는 알고리즘. 
		- 동작 과정
			1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
			2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
			3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
	+ 예제
		- 5-1 [스택](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-1.py)
		- 5-2 [큐](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-2.py)
		- 5-3 [재귀 함수](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-3.py)
		- 5-4 [재귀 함수 종료](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-4.py)
		- 5-5 [2가지 방식으로 구현한 팩토리얼 예제](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-5.py)
		- 5-6 [인접 행렬 방식](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-6.py)
		- 5-7 [인접 리스트 방식](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-7.py)
		- 5-8 [DFS](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-8.py)
		- 5-9 [BFS](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-9.py)
		- 5-10 [음료수 얼려 먹기](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-10.py)
		- 5-11 [미로 ](https://github.com/parkgr95/Coding_Test/blob/main/Ch05.DFSBFS/5-11.py)
* * *
* **CHAPTER 06 정렬**

* * * 
* **CHAPTER 07 이진 탐색**
