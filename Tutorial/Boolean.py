"""

자료형의 참과 거짓은 다음과 같다.

"python"    →   True
""          →   False
[1, 2, 3]   →   True
[]          →   False
()          →   False
{}          →   False
1           →   True
0           →   False
None        →   False

"""
    
# bool() 함수를 사용하여 자료형의 참과 거짓을 식별할 수 있다.

# True
print(bool('python'))

a = ""
# False
print(bool(a))


print(id(a))