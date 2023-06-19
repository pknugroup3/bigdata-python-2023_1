# 변수 

a = 1 
b = 'python'
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))

#문자열은 할당, copy 동일/ 리스트 할당, copy 다름
a = b

print(id(a))
print(id(b))
print(a is b)

from copy import copy

a = copy(c)
print(id(a))
print(id(c))
print(c is a)


(a, b) = ('python',5)

print(a, b)

[c, d ]= ['python', 7] # 이렇게는 많이 안씀

print([c,d])
print(c,d)
print(c)
print(d)