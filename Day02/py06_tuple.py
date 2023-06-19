#튜플
#리스트와 유사하지만 추가, 수정, 삭제 불가능 immutable

l1 = [1, 2, 3] # list
t1 = (1, 2, 3) # tuple

l1.append(4) # 리스트는 11개 함수 존재 -> 수정 가능

# del t1[0] 예외 발생
print(t1[2])
print(t1[:2+1]) # -> (1, 2) 마지막 값의 인덱스 +1까지 해야함

t2 = (5, 6, 7)
t3 = t1 + t2 # -> 새로운 튜플을 최초에 만드는 연산이기 때문에 가능

print("t3 : ", t3)


def calc(x, y):
    # 사칙연산 모두 다 처리
    add = x + y
    minus = x - y
    mult = x * y
    div = x / y

    return(add, minus, mult, div)


#값을 한꺼번에 여러개 리턴 받을수 있음(java, C#, python 동일)
(res1, res2, res3, res4) = calc(5, 8)

print("res1~4 : ", res1, res2, res3, res4)

