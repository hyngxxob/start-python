"""
1. String Indexing
2. String slicing
3. replace()
4. split()
5. strip()
6. upper()
7. lower()
8. capitalize()
9. endswith()
10. startswith()
11. rstrip()

"""



### String Indexing ###
# p t
letters = 'python'
print(letters[0],letters[2])



### String slicing ###
# 2210
license_plate = "24가 2210"
print(license_plate[-4:])

# 시작인덱스:끝인덱스:오프셋
# 홀홀홀
string_A = "홀짝홀짝홀짝"
print(string_A[::2])

# 문자열 거꾸로 출력
# NOHTYP
string_B = "PYTHON"
print(string_B[::-1])

# 문자열 치환
# 010 1111 2222
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))

# 문자열 다루기
# kr
url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[-1])

string_C = 'abcdfe2a354a32a'
print(string_C.replace("a","A"))

# 문자열 좌우 공백 제거
# strip()
data = "   삼성전자    "
data1 = data.strip()
print(data1)