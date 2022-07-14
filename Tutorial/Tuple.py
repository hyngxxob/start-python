"""

#### 파이썬 튜플은 순서가 있지만 수정 불가능한 자료구조이다.

1. 튜플을 List로 변환
2. List를 튜플로 변환
3. 튜플 언팩킹
4. range 함수

"""

# 튜플을 List로 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
# ('삼성전자', 'LG전자', 'SK Hynix')
print(interest)
data = list(interest)
# ['삼성전자', 'LG전자', 'SK Hynix']
print(data)


# List를 튜플로 변환
interest2 = ['삼성전자', 'LG전자', 'SK Hynix']
data2 = tuple(interest2)
# ('삼성전자', 'LG전자', 'SK Hynix')
print(data2)


# 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
# apple banana cake
print(a, b, c)


# range 함수
data = tuple(range(2, 100, 2))
print( data )