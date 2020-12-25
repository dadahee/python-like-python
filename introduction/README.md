# 문제

### 내용
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다.  mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

</br>  

### 제한 조건
- mylist의 길이는 100 이하인 자연수입니다.
- mylist 각 원소의 길이는 100 이하인 자연수입니다.

</br>  

### 예시
| input | output |  
| ------ | ------ |
| [[1], [2]] | [1,1] |  
| [[1, 2], [3, 4], [5]] | [2,2,1] |  


</br>  

<hr>

# 풀이

</br>

### 내 풀이
```python
def solution(mylist):
    return [ len(x) for x in mylist ]
```

</br>

### 다른 방법
```python
def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        answer.append(len(mylist[i]))
    return answer
```
</br>  

### 강의 풀이

```python
def solution(mylist):
    return list(map(len, mylist))
```


</br>
<hr>

# 결론
1. 내장 함수를 잘 활용해서 직관적이고 단순하고 짧은 코드를 작성하자
2. 용어: iterable, sequence, unpacking
3. 