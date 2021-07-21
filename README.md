Coding-Test
=============
이것이 취업을 위한 코딩 테스트다 with 파이썬- 문제풀이
-------------
* **CHAPTER 03 그리디**
	+ 그리디란
		- 현재 상황에서 지금 당장 좋은 것만 고르는 방법. 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않음.
	+ 예제
		- 3-1 [거스름돈](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-1.py): '가장 큰 화폐 단위부터' 돈을 거슬러 주기
		- 3-2 [큰 수의 법칙](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-2.py): 반복되는 수열에 대해서 파악하기
		- 3-3 [숫자 카드 게임](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-3.py): 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 찾기
		- 3-4 [1이 될 때까지](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/3-4.py): 최대한 많이 나누기
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
		- 4-1 [상하좌우](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/4-1.py)
		- 4-2 [시각](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/4-2.py)
		- 4-3 [왕실의 나이트](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/4-3.py)
		- 4-4 [게임 개발](https://github.com/parkgr95/Coding_Test/blob/main/Ch03.%EA%B7%B8%EB%A6%AC%EB%94%94/4-3.py)
* * *
* CHAPTER 05 DFS/BFS
