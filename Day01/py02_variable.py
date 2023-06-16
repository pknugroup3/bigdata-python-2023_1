# 변수 
import sys


number = 100100000000000000000
value = sys.maxsize + 1 # sys.maxsize 파이썬 시스템에서 제공하는 최고숫자

print(number)
print(value + 1)

value2 = 0o12 # 8진수

print(value2)

value3 = 0xFF # 16진수

print(value3)

value2 = 'Hello, python'
print(value2)

value2 = False
print(value2 == False)

# 사칙연산, 수학식
print(14 / 3) # 소수점 나누기
print(14 // 3) # 정수로 나누기
print(2 ** 10) # 승수
print(10 % 3) # 나머지 (3의 배수, 배수들 구할때)