# 문제
## 몫과 나머지

</br>

### 내용
숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

</br>

### 입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.

</br>

### 출력 설명
a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

</br>

### 제한 조건
a, b는 자연수입니다.

</br>

### 입력 예
`5 3`

</br>

### 출력 예
`1 2`

</br>

<hr>  

# 풀이

### 내 코드
```python
a, b = map(int, input().strip().split(" "))
print(str(a//b) + " " + str(a%b))
```

</br>

### 다른 방법
```python
a, b = map(int, input().strip().split(" "))
print(a//b, a%b)
```

</br>

### 강의 풀이
```python
a, b = map(int, input().strip().split(" "))
print(*divmod(a, b))
```
그렇지만 위의 방법이 언제나 더 좋은 것은 아니다!  
개념을 익혀두고, 활용할 수 있다는 것만 알아두면 좋을 듯하다.

> 코드 설명  
> 1. divmod(a, b) => ( a//b, a%b )
> 2. `unpacking`: divmod(a, b) 리턴값에 * 키워드를 사용하여 `print()` 함수의 인수로 준다. => 즉, 튜플쌍을 풀어서(`unpacking`) 가변 인자를 받는 `print()` 함수에 전달한다. => 값이 띄어쓰기 되어 최종 출력!
>> 예) a = 15, b = 4일 때  
>> `divmod(a, b)`: `(3, 3)`
>> `print(*divmod(a, b))`: `3 3`

</br>

<hr>

# 결론
1. `divmod()` 내장함수
   - 입력: 복소수가 아닌 두 수 `a, b`
   - 출력: a를 b로 나눈 몫과 나머지 페어, 즉 `( a // b, a % b )`. 실수인 경우, `( Math.floor(a / b, a % b ))`

2. `unpacking` vs `packing`
   - `unpacking`: 패킹된 변수에서 여러개의 값을 꺼내오는 것
     - 인수에 *, ** 키워드 사용 -> 하나의 객체를 해체 후 여러 값을 추출하여 함수의 인자로 던져준다.
      ```python
      >>> print(*[1,2,3])
      1 2 3
      ```
   - `packing`: 하나의 변수에 여러 개의 값을 넣는 것
     - 인자(매개변수)에 *, ** 키워드 사용 -> 즉, 가변(혹은 키워드) 인자(매개변수, parameter)를 사용하여 하나의 객체로 받아 유연한 프로그래밍
     ```python
     def func(*numbers):
       result = 0
       for number in numbers:
         result += number
       return result
     ```
   - 활용: 두 변수의 값을 swap할 때, 함수에서 여러 값을 리턴할 때, 함수 가변 인자 등
   - 요약: 함수 `선언부`의 `*args`는 `packing`, 함수 `호출부`의 `*args`는 `unpacking`

3. `인자` vs `인수`
   - `인자(parameter)`: 함수 정의 시 외부로부터 받아오는 임의의 값 (== 매개변수)
   - `인수(argument)`: 함수 호출 시 사용되는 값

4. `위치 인자` vs `키워드 인자` vs `가변 인자`
   - `위치 인자(positional parameter`: 일반적으로 선언하는 인자
   - `가변 인자(variable parameter)`: 인자의 개수가 정해져있지 않을 때 주로 사용.
     - 가변 위치인자(`*args`): 임의의 수의 위치 인자를 tuple 타입 변수로 저장
     - 가변 키워드인자(`**kwargs`): 임의의 수의 키워드 인자를 dict 타입 변수로 저장.
   - `키워드 인자(keyword parameter)`: `para=default` 형식으로 기본값이 선언된 인자. 호출 시 입력값이 있으면 위치 인자로 처리되고, 없으면 default 값으로 처리된다. 즉, `default parameter`
     - 어서와 파이썬 웅앵! 공부 뇌피셜: 위치 인자보다 앞에 올 수 없다. 위치인자 -> 키워드 인자순으로 위치.  
   - 비교
      ``` python
      def func(arg, kwarg, *args, **kwargs):
        return ...
      ```
      arg: 위치인자, kwarg: 키워드 인자, args: 가변 인자, kwargs: 가변 키워드 인자
     
5. 항상 `divmod()`가 옳은 것은 아니다.
   - 가독성이나, 팀의 코드 스타일에 따라서, 분리하여 작성할 때가 더 좋을 수도 있다.
   - divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느리지만, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르다.