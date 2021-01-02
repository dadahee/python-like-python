# 문제
## 알파벳

</br>
<hr>

### 내용
입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

</br>
<hr>

### 입력
```
0
```

</br>
<hr>

### 출력
```
abcd...(중간생략)..xyz
```

</br>
<hr>

### 입력
```
1
```

</br>
<hr>

### 출력
```
ABCD...(중간생략)..XYZ
```

</br>
<hr>

# 풀이

### 내 코드
```python
num = int(input().strip())
alpha = "abcdefghijklmnopqrstuvwxyz"
if num: print(alpha.upper())
else: print(alpha)
```
소문자만 상수로 직접 타이핑하고 대문자는 `upper()` 메소드를 사용하여 출력

</br>
<hr>

# 결론

### string 모듈
```python
import string
...
string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```

### 아이디어
- 알파벳 대소문자에 대해 순회하며 검사하는 코드를 작성할 때 유용할 것 같다.
- 프로젝트 등에서 활용하면 가독성이 높아져서 좋을듯.
- 바로바로 활용할 수 있도록 체화하자 !