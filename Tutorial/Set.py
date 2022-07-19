s1 = set([1,2,3])
# {1, 2, 3}
print(s1)

l1 = list(s1)
# [1, 2, 3]
print(l1)
# 1
print(l1[0])

a1 = set([1,2,3,4,5,6])
a2 = set([4,5,6,6,7,8])

#### 교집합
# {4, 5, 6}
print(a1&a2)
# {4, 5, 6}
print(a1.intersection(a2))


#### 합집합
# {1, 2, 3, 4, 5, 6, 7, 8}
print(a1|a2)
# {1, 2, 3, 4, 5, 6, 7, 8}
print(a1.union(a2))


#### 차집합
# {1, 2, 3}
print(a1-a2)
# {1, 2, 3}
print(a1.difference(a2))


a3 = set([1, 2, 3])
#### 집합(set) 자료형 값 1개 추가하기(add)
a3.add(4)
# {1, 2, 3, 4}
print(a3)


a4 = set([1, 2, 3])
#### 집합(set) 자료형 값 여러개 추가하기(update)
a4.update([4, 5, 6])
# {1, 2, 3, 4, 5, 6}
print(a4)

a5 = set([1, 2, 3])
#### 집합(set) 자료형 특정 값 제거하기(remove)
a5.remove(2)
# {1, 3}
print(a5)