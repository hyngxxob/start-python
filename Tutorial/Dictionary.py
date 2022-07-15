# 기본적으로 데이터 언팩킹은 좌변의 변수와 우변 데이터 개수가 같아야 한다.
# 하지만 star expression(*)을 사용하면 변수의 개수가 달라도 데이터 언팩킹을 할 수 있다.
# 불필요하게 필요 이상의 나머지 데이터를 언팩킹 할 필요 없다.

"""

1. 별 표현식
2. 빈 딕셔너리 생성
3. 딕셔너리 구성
4. 딕셔너리 요소 추가
5. 딕셔너리 요소 수정
6. 딕셔너리 요소 삭제

"""
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score_1, _, _= scores
print(valid_score_1)

_, _, *valid_score_2 = scores
print(valid_score_2)

_, *valid_score_3, _ = scores
print(valid_score_3)

# 빈 딕셔너리 생성
temp = { }

# 딕셔너리 구성
ice = { "메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
print(ice)

# 딕셔너리 요소 추가
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

print("메로나 가격 :", ice["메로나"])

# 딕셔너리 요소 수정
ice["메로나"] = 2000
print(ice)


# 딕셔너리 요소 삭제
del ice["메로나"]
print(ice)


# 딕셔너리 생성 및 딕셔너리 인덱싱
inventory = { "메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
print(inventory)
print(inventory["메로나"][0], "원")
print(inventory["메로나"][1], "개")

inventory["월드콘"] = [500, 7]
print(inventory)


# 딕셔너리 keys() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())

# 딕셔너리 values() 메서드
print(icecream.values())

# 딕셔너리 values() 내 int 값을 sum()으로 더함
print(sum(icecream.values()))


# 딕셔너리 update 메서드 : 딕셔너리 추가
new_product = {'팥빙수' : 2700, '아맛나' : 1000}
icecream.update(new_product)
print(icecream)
