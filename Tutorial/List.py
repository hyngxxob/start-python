
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