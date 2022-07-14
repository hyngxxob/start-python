"""

### 파이썬 리스트는 순서가 있고 수정 가능한 자료구조입니다.

1. append()
2. insert(인덱스, 원소)
3. del
4. List 합집합
5. List max(), min()
6. List sum()
7. List len()s
8. List Sliing
9. List join()
10. List split()
11. List sort(), sorted()

"""

# append()
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)


# insert(인덱스, 원소)
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

# del
del movie_rank[3]
print(movie_rank)

del movie_rank[2]
del movie_rank[2]
print(movie_rank)


# List 합집합
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)


# List 최댓값, 최솟값 구하기
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))


# List 합 출력
nums = [1, 2, 3, 4, 5]
print(sum(nums))


# List 데이터 개수 출력
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))


# List 평균 출력
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))


price = ['20180728', 100, 130, 140, 150, 160, 170]
# 1번 요소부터 출력
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 홀수 출력
print(nums[::2])

# 짝수 출력
print(nums[1::2])

# 역출력
print(nums[::-1])

# 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# ['삼성전자', 'LG전자']
print(interest[0:2])


# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
# List 요소 줄바꿈 출력
print("\n".join(interest))


string = "삼성전자/LG전자/Naver"
# ['삼성전자', 'LG전자', 'Naver']
print(string.split("/"))


# 리스트 정렬 - 오름차순 출력
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

data2 = sorted(data)
print(data2)