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

</br>

<hr>

# 결론
1. `divmod` ? `unpacking`? `packing`? 이게 뭔데?
   - `divmod`:
   - `unpacking`:
   - `packing`:
   - 
2. 가독성이나, 팀의 코드 스타일에 따라서, 분리하여 작성할 때가 더 좋을 수도 있습니다. 또한, divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.

둘의 퍼포먼스 차이에 관련해서는 Stack Overflow 질문을 참고해주세요