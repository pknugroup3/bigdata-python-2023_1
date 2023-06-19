#리스트 계속
a = [1, 2, 3]
print(a)

# 자료구조 stack 에 있는 pop 기능 구현
print(a.pop())
print(a)

a.append(10)
print(a)

print(a.count(3)) # 리스트 안에 값이 몇개 있는지


# 리스트 확장 a = 1, 2, 10
a.extend([5, 3, 2])
print(a)

print("2 갯수 : %d" %(a.count(2)))
print("a : ", a)