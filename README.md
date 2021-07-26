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
	+ 순차 탐색(Sequential Search)
		- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
		- 시간 복잡도: O(N)
	+ 이진 탐색(Binary Search)
		- 찾으려는 데이터와 중간점(시작점과 끝점의 가운데) 위치에 있는 데이터를 반복적으로 비교하여 확인하는 방법.
		- 배열 내부의 데이터가 정렬되어 있으면 매우 빠르게 데이터를 찾을 수 있는 알고리즘. 탐색 범위를 절빤씩 좁혀가며 데이터를 탐색한다.
		- 시간 복잡도: 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어드므로, 시간 복잡도가 O(logN)이다.
		- 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야하는 알고리즘을 떠올리자!
	+ 이진 탐색 트리
		- 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다.
		- 특징:
			1. 부모 노드보다 왼쪽 자식 노드가 작다.
			2. 부모 노드보다 오른쪽 자식 노드가 크다.
	+ 예제
		- 7-1 [순차 탐색](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-1.py)
		- 7-2 [재귀 함수로 구현한 이진 탐색](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-2.py)
		- 7-3 [반복문으로 구현한 이진 탐색](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-3.py)
		- 7-4 [한 줄 입력받아 출력](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-4.py)
		- 7-5 [부품 찾기(이진 탐색)](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-5.py)
		- 7-6 [부품 찾기(계수 정렬)](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-6.py)
		- 7-7 [부품 찾기(집합 자료형)](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-7.py)
		- 7-8 [떡볶이 떡 만들기](https://github.com/parkgr95/Coding_Test/blob/main/Ch07.%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/7-8.py)
* * * 
* **CHAPTER 08 다이나믹 프로그래밍**
	+ 다이나믹 프로그래밍(Dynamic Programming)이란
		- 메모리 공간을 더 사용하여 연산 속도를 비약적으로 증가시킨 방법. 동적 계획법이라고도 한다.
		- 2가지 방식(탑다운, 보텀업)이 존재한다.
			1. 탑다운(Top-Down) 방식: 큰 문제를 해결하기 위해 작은 문제를 호출. 재귀 함수를 이용해서 다이나믹 프로그래밍 소스코드를 작성. '메모이제이션 기법'이 자주 사용됨.
			2. 보텀업(Bottom-Up) 방식: 작은 문제부터 차근차근 답을 도출. 반복문을 이용해서 소스코드를 작성. 다이나믹 프로그래밍의 전형적인 형태. 결과 저장용 리스트인 'DP 테이블'이 사용됨
		- 다음 조건을 만족할 때 사용할 수 있다.
			1. 큰 문제를 작은 문제로 나눌 수 있다.
			2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
	+ 메모이제이션(Memoization)
		- 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법을 의미.
		- 캐싱(Caching)이라고도 한다.
		- 탑다운 방식에 국한되어 사용된다.
	+ 문제에서의 다이나믹 프로그래밍
		- 완전 탐색 알고리즘으로 접근했을 때 시간이 오래 걸리면 문제들의 중복 여부를 확인하여 다이나믹 프로그래밍을 적용할 수 있는 지 확인해보자.
		- 단순히 재귀 함수로 작성한 뒤에 (탑다운) 메모이제이션을 적용할 수 있느면 코드를 개선해보자. ex) 피보나치 수열
		- 탑다운 방식보다는 보텀업 방식으로 구현하자.
		- 재귀적인 소스 코드에서 'recursion depth(재귀 함수 깊이)'와 관련도니 오류가 발쌩할 땐, sys 라이브러리에 setrecursionlimit() 함수를 호출하여 재귀 제한을 완하할 수 있다.
	+ 예제
		- 8-1 [피보나치 함수](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-1.py)
		- 8-2 [피보나치 수열(재귀적)](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-2.py)
		- 8-3 [호출되는 함수 확인](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-3.py)
		- 8-4 [피보나치 수열 소스코드(반복적)](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-4.py)
		- 8-5 [1로 만들기](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-5.py)
		- 8-6 [개미 전사](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-6.py)
		- 8-7 [바닥 공사](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-7.py)
		- 8-8 [효율적인 화폐 구성](https://github.com/parkgr95/Coding_Test/blob/main/Ch08.%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/8-8.py)
		- * * * 
* **CHAPTER 09 최단 경로**
	+ 다익스트라 최단 경로 알고리즘이란
		- 다익스트라(Dijkstra) 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
		- '음의 간선'(=0보다 작은 값을 가지는 간선)이 없을 때 정상적으로 동작한다.
		- 알고리즘의 원리:
			1. 출발 노드를 설정한다.
			2. 최단 거리 테이블을 초기화한다.
			3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
			4. 해당 노듣를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다. <- 1차원 리스트(=최단 거리 테이블)에 저장 및 갱신
			5. 위 과정에서 3과 4번을 반복한다. <- 그리디 알고리즘
		- 알고리즘 구현 방법
			1. 간단한 다익스트라 알고리즘: O(V^2)의 시간 복잡도를 가진다. 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)한다. 전체 노드의 개수가 5,000개 이하일 경우 사용하자.
			2.개선된 다익스트라 알고리즘: 최악의 경우에도 O(ElogV)의 시간 복잡도를 가진다. 힙(Heap) 자료구조를 사용한다. 우선순위 큐를 이용해서 시작 노드로부터 '거리'가 짧은 노드 순서대로 큐에서 나올 수 있게 한다.:sparkles: 
	+ 힙(Heap)
		- 우선순위 큐(Priority Queue)를 구현하기 위하여 사용하는 자료구조
		- 우선순위 큐: 우선순위가 가장 높은 데이터를 가장 먼저 삭제
		- heapq 라이브러리 사용. 첫 번째 원소를 기준으로 우선순위를 설정한다. 최소 힙에 기반한다.
		- 시간복잡도: 삽입O(NlogN) + 삭제O(NlogN) = O(NlogN)
	+ 플로이드 워셜 알고리즘이란
		- 플로이드 워셜 알고리즘(Floyd-Warshall Algorithm)은 모든 지점에서 다른 모든 지접까지의 최단 경로를 모두 구해야하는 경우에 사용할 수 있는 알고리즘이다.
		- O(N^3)의 시간 복잡도를 가진다.
		- 다익스트라 알고리즘과의 차이
			1. 2차원 리스트에 최단 거리 정보를 저장한다.
			2. 점화식에 맞게 2차원 리스트를 갱신하는 다이나믹 프로그래밍이다. 점화식: Dab = min(Dab, Dak+Dkb)
		 
