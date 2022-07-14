"""
1. sep
2. end
3. % formatting
4. format() Method
5. f-string

"""

# 오늘은 일요일
print ("오늘은", "일요일")


# naver;kakao;sk;samsung
print("naver", "kakao", "samsung", sep=";")


# 줄바꿈 없이 출력
print("first", end=""); print("second")


# hello! python
s = "hello"
t = "python"
print(s+"!",t)


# % formatting
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# format() Method
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# f-string 
# f-string은 파이썬 3.6부터 지원
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")