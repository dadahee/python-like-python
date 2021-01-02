# Python-like-Pyhon
### [프로그래머스] 파이썬을 파이썬답게 강의 공부 & 정리
파이썬스러운 단순하고 직관적인 코드를 작성해보자.  

_2020-12-26~_

</br>
<hr>

### 내장 함수
- [divmod(a, b)]() / int, 몫과 나머지
- [list()]() / introduction, 리스트 원소수 세기 & iterable, 모든 멤버의 type 변환하기
- [map()]() / introduction, n진법으로 표기된 string을 10진법 숫자로 변환하기 & iterable, 모든 멤버의 type 변환하기
- [enumerate()]() / int, n진법으로 표기된 string을 10진법 숫자로 변환하기
- [int()]() / int, n진법으로 표기된 string을 10진법 숫자로 변환하기
- [sum()]() / int, n진법으로 표기된 string을 10진법 숫자로 변환하기
- 문자열 클래스
  - [정렬 메서드 .ljust(), .center(), .rjust()]() / str, 문자열 정렬하기
  - [.format()]() / 문자열 정렬하기
  - [.join()]() / sequence types, sequence 멤버를 하나로 이어붙이기
  - [.split()]() / sequence types, sequence 멤버를 하나로 이어붙이기
- string 모듈
  - [string 상수 모음(알파벳 대소문자, 숫자)]() / str, 알파벳
- [sorted()]() / iterable, 원본을 유지한채, 정렬된 리스트 구하기
- [zip()]() / iterable, 2차원 리스트 뒤집기(transpose)

</br>
<hr>

### 용어집
1. `iterable` : 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체. 
    - 예) list, str, tuple, dict
2. `sequence` : interable의 하위 카테고리. 인덱스(int 타입)를 통해, 원소에 접근할 수 있는 iterable.
    - 예) list, str, tuple 

</br>
<hr>

### 개념
1. [packing과 unpacking]() / int, 몫과 나머지
2. [인수(Argument)와 인자(parameter)]() / int, 몫과 나머지
3. [인자의 종류와 비교(위치vs키워드vs가변)]() / int, 몫과 나머지
4. [iterable vs iterator]() / int, n진법으로 표기된 string을 10진법 숫자로 변환하기
5. [단순 복제 vs 얕은 복사(shallow copy) vs 깊은 복사(deep copy)]() / iterable, sorted() vs .sort()
6. [sorted() vs .sort()]() / iterable, sorted() vs .sort()

</br>
<hr>

### 아이디어
1. string 역순 결과 얻기: `[::-1]` / int, n진법으로 표기된 string을 10진법 숫자로 변환하기
2. key, value 리스트로 딕셔너리 생성하기: `dict(zip(...))` / iterable, 2차원 리스트 뒤집기

</br>
<hr>


### 수강 기록
1. introduction / 2020.12.26
2. int 다루기 / 2020.12.26
3. str 다루기 / 2021.1.1(알파벳), 2021.1.2(문자열 정렬하기)
4. iterable 다루기 / 2021.1.2(원본 유지하며 정렬된 리스트 구하기, 2차원 리스트 뒤집기), 2021.1.
5. Sequcne Type 다루기 / 2021.1.2(sequence 멤버를 하나로 이어붙이기)
6. itertools & collections 모듈