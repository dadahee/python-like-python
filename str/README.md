# 문제
## n진법으로 표기된 string을 10진법 숫자로 변환하기

</br>
<hr>

### 내용
base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

</br>
<hr>

### 입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

</br>
<hr>

### 출력 설명
base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.

</br>
<hr>

### 제한 조건
- base는 10 이하인 자연수입니다.
- num은 3000 이하인 자연수입니다.

</br>
<hr>

### 예시 
| input	| output |
| ------ | ----- |
| 12 3 | 5 |
| 444 5	| 124 |


</br>
<hr>

# 풀이

### 내 코드
```python
num, base = map(int, input().strip().split(' '))
print(sum(map(lambda x: int(x[1]) * base ** x[0] , enumerate(str(num)[::-1]))))
```
1. 진수 변환을 위해서는 num의 각 자리마다 값을 확인하고 base에 따른 자릿수 값을 곱해주어야 한다. 또한 이 곱을 저장하여 최종 결과를 리턴해야 한다. => 비록 숫자 계산이지만, `int` 대신 `string`를 사용하기로 결심. `string`은 인덱싱을 통해 `num`에 자릿수 단위로 바로 접근할 수 있어 더 용이한 구조라 생각했다. 또한 인덱싱을 사용하면 원본 객체 손실이 없다. `int` 타입에서는 해당 자릿수의 수를 불러오려면 나누기 연산이 필수인데, 이 때 원본 값의 손실 방지를 위해 변수를 하나 더 써야 함.
2. num의 해당 자리의 수 * ( base ** 자릿수 ) 계산
   1. 오른쪽부터 0, 1, 2... 순으로 자릿수를 카운트해야 한다. => 음수 인덱싱 등 계산이 번거로우므로 아예 string을 역순으로 만들어 왼쪽부터 인덱싱 해야겠다 생각. => string 객체에 `[::-1]` 슬라이싱 방법을 사용하여 역순 리턴하게 하였다.
   2. `enumerate()` 함수를 사용하여 자릿수와 자릿수의 값을 tuple 쌍으로 묶은 iterable 객체를 리턴하게 하였다.
   3. 각 자릿수마다 반복하므로 `map()` 함수를 사용하였고, lambda 함수로 계산식을 지정.
3. `sum()`: 자릿수마다 반복한 결과를 더한 최종 결과를 리턴.
   - 각각의 값들이 저장되어 묶인 `map()` 함수의 리턴값, 즉 `iterable` 객체를 인수로 받는다.

</br>
<hr>

### 다른 방법
```python
num, base = map(int, input().strip().split(' '))
answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
print(answer)
```
`enumerate()`로부터 `for each`문을 통해 인덱스와 값을 바로 뽑아냈다!

</br>
<hr>

### 강의 풀이
```python
num, base = map(int, input().strip().split(' '))
print(int(num, base))
```
허무할 정도로 간단한 코드. 상호 진수 변환 때 시간 단축하기 좋은 것 같다!


</br>
<hr>

# 결론

### 내장 함수
1. `int()` 내장 함수
    - `int(n, b=10)`: `str` 타입의 base가 `b`인 숫자 `n`을 10진수로 변환.  
    - 입력: `str` 타입의 숫자 객체
    - 출력: base가 `b`인 숫자 `n`을 10진수로 변환한 결과
    - int() 함수는 진법 변환도 지원한다고 강의에는 나와 있는데, 늘 최종 결과는 늘 10진수이므로 `진법 인식` 정도로 보는 것이 어떨까 한다.
2. `enumerate()` 내장 함수
   - 입력: `iteration`을 지원하는 객체(`sequence`, `iterator` 등), 시작 인덱스(default=0)
   - 출력: `( count값, 이터러블 객체의 count번째 요소값 )`들로 이루어진 `enumerate` 타입 객체
   - `enumerate(iterable, start=0)`: count값이 start부터인 `(인덱스, 값)` tuple pair 목록으로 이루어진 `enumerate` 리턴
3. `map()` 내장 함수
   - 입력: `iterable 각 요소에 대해 적용할 함수`, `iterable` 객체
   - 출력: `iterable` 객체에 각 함수를 적용하여 연산한 결과(`iterator`)
   - `map(func, iterable)`: `iterable` 객체의 각 요소에 대해 `func`를 적용한 `iterator`를 리턴
4. `sum()` 내장함수
   - `sum(iterable, start=0)`: `start` 객체의 값에 `iterable` 객체의 모든 요소의 합을 더하여 리턴
   - 예) `sum([1,2,3,4,5], 3)` == `18`

5. `iter()` 내장함수
    - 입력: `object`
    - 출력: `iterator` 객체

### 아이디어
1. `[::-1]` 슬라이싱
    - `str_obj[::-1]`을 통해 기존 객체를 역순 리턴한 결과를 얻을 수 있다.
    - 즉, `'1234[::-1]'` == `'4321'` (단순 `역순` 결과)
    - != `sorted('1234', reverse=True)` (내림차순 `정렬`)


### 개념
6. `iterable` vs `iterator`
   - `iterable`: 반복 가능한 객체
     - 예) list, str, set, tuple, range
   - `iterator`: 값을 차례대로 꺼낼 수 있는 객체. 즉, `next()` 메소드로 데이터를 순차적으로 호출 가능한 객체. 더이상 불러올 데이터가 없을 경우 `StopIteration` 예외 발생.
   - `iterable` vs `iterator`
     - `iterable` 객체는 모두 `iterator`인가? `No!`
   - [참고자료](https://wikidocs.net/16068)