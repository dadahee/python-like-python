# Sequence Types
## sequence 멤버를 하나로 이어붙이기 : join()


### 문제
문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 `['1', '100', '33']` 인 경우, solution 함수는 `'110033'`을 리턴하면 됩니다.

</br>
</hr>

### 제한 조건
- mylist의 길이는 100 이하인 자연수입니다.
- mylist의 원소의 길이는 100 이하인 자연수입니다.

</br>
</hr>

# 풀이

### 내 코드
```python
def solution(mylist):
    return "".join(mylist)
```

### 다른 풀이
```python
answer = ''
def solution(mylist):
    for i in mylist:
        answer += i
    return answer
```

</br>
</hr>

# 결론

### 내장함수
1. `.join()` 메서드
   - `str_obj.join(li_obj)`: `li_obj`의 각 원소(*반드시 string 타입*)를 `str_obj` 간격의 `string`으로 이어붙여 리턴
   - 예제
    ```python
    >>> li = list("hello")
    >>> ":".join(li)
    'h:e:l:l:o'
    ```
2. `.split()` 메서드
   - `str_obj`.split(`s`): `s`를 기준으로(default: `space`) `str_obj`를 쪼개어 리스트로 리턴  
   - 예제  

    ```python
    >>> words = "he llo, wor ld!"
    >>> words.split()
    ['he', 'llo,', 'wor', 'ld!']
    >>> words.split(",")
    ['he llo', ' wor ld!']
    ```

[참고: 초보몽키 블로그, 리스트 메서드](https://wayhome25.github.io/python/2017/02/26/py-14-list/)