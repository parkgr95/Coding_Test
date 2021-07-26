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
	+ 정렬이란
		- 데이터를 특정한 기준에 따라서 순서대로 나열하는 것.
	+ 선택 정렬(Selection Sort)
		- 데이터가 무작위로 여러 개 있을 때, 매번 '가장 작은 데이터를 선택해' 순서대로 앞에 있는 데이터와 바꾸는 과정을 반복하는 정렬
		- 시간 복잡도: N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보낸다. 또한 매번 가장 작은 수를 찾기 위해서 비교 연산이 필요하다. 따라서 연산 횟수는 <br>
		N + (N-1) + (N-2) + ... + 2 = N * (N+1) / 2 = (N^2 + N) / 2 <br>
		이고 시간 복잡도는 O(N^2)이다.
	+ 삽입 정렬
		- 특정한 데이터를 적절한 위치에 삽입하는 정렬. 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다. 또한, 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적인 정렬이다. 
		- 시간 복잡도: 시간 복잡도는 O(N^2)이나, 최선의 경우(=데이터가 거의 정렬되어 있는 상태라면) O(N)의 시간 복잡도를 가진다.
	+ 퀵 정렬
		- 기준(=피벗, Pivot)을 설정한 다음 기준보다 큰 수와 작은 수를 교환하는 정렬을 수행한 이후에, 피벗으로 기준으로 왼쪾 리스트와 오른쪽 리스트에서 각각 다시 정렬을 수행행하는 정렬이다.
		- 시간 복잡도: 평균 시간 복잡도는 O(NlogN)이다. 최악의 경우(=리스트의 가장 왼쪽 데이터를 피벗으로 삼을 때, '이미 데이터가 정렬되어 있는 상태'라면) 시간 복잡도는 O(N^)이다.
	+ 계수 정렬
		- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
		- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때, 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다. 즉, 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수는 없다.
		- 비교 기반의 정렬 알고리즘이 아닌 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다.
		- 시간 복잡도: 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대값의 크기를 K라고 할 때, 계수 정렬의 시간 복잡도는 O(N+K)이다.
		- 공간 복잡도: O(N+K)이다.
	+ 정렬 라이브러리
		- 문제에서 별도의 요구가 없다면 단순히 정렬해야 하는 상황에서는 기본 정렬 라이브러리를 사용하고, 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬을 사용하자.
		- 시간 복잡도: 항상 최악의 경우에도 시간 복잡도는 O(NlogN)이다.
	+ 예제
		- 6-1 [선택 정렬](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-1.py)
		- 6-2 [파이썬 스와프(Swap)](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-2.py)
		- 6-3 [삽입 정렬](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-3.py)
		- 6-4 [퀵 정렬](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-4.py)
		- 6-5 [파이썬의 장점을 살린 퀵 정렬](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-5.py)
		- 6-6 [계수 정렬](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-6.py)
		- 6-7 [sorted](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-7.py)
		- 6-8 [sort](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-8.py)
		- 6-9 [정렬 라이브러리에서 key를 활용](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-9.py)
		- 6-10 [위에서 ](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-10.py)
		- 6-11 [성적이 낮은 순서로 학생 출력하기](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-11.py)
		- 6-12 [두 배열의 원소 ](https://github.com/parkgr95/Coding_Test/blob/main/Ch06.%EC%A0%95%EB%A0%AC/6-12.py)

* * * 
* **CHAPTER 07 이진 탐색**

* * * 
* **CHAPTER 08 다이나믹 프로그래밍**
