# 함수

'''
private void 
'''

def add(x,y)->any: # int등 가능
    result  = x + y
    return result


def minus(x, y):
    return x-y


print(add(3,5.2)) # -> int 여도 실수로 나옴
print(minus(3,5))

print(add('Hello','World')) # 입력 파라미터에 제약이 없지만 문제가 생길지도?

def plus(x,y):
    print(x+y)

plus(3,5.4)

print(None) # == null

def add_many(*args): #C/C++ pointer 처럼 보이지만
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5))
print(add_many(3,6,9,12,15))


# print(add_many("life","is","short","you","need python")) # add_many의 result를 result=''으로 바꿔야 실행됨 근데 바꾸면 위에 숫자가 안됨

#키워드 매개변수 -> 결과가 딕셔너리
def print_kwargs(**kwargs):
    return kwargs

result =print_kwargs(a=1) # {'a': 1}
print(result['a'])
res = print_kwargs(name='Hugo', age= 45) #{'name': 'Hugo', 'age': 45}
print(res['name'])
print(res.get('name'))


def mult (x,y):
    return x*y

def div(x,y):
    return x//y

a=10
b=7
print(add(a,b))
print(minus(a,b))
print(mult(a,b))
print(div(a,b))

# add, minus, mult, div 함수 네개가 할 일을 하나의 함수로 처리
def all_calc(x,y):
    return (x+y, x-y, x*y, x/y) #-> 튜플 사용

print(all_calc(601, 45))

#리턴값을 튜플로 처리하면 리턴을 한꺼번에 여러개 할 수 있음
(res_add, res_min, res_mul, res_div) = all_calc(601,45)


#함수 기본 값
def introduce_myself(name, age, man=True)->None:
    print(f'나의 이름은 {name} 입니다.')
    print(f'나이는 {age}세 입니다.')
    if man:
        print(f'나는 남자입니다.')
    else:
        print(f'나는 여자입니다.')

introduce_myself('abc',100)

introduce_myself(man=False, name='애슐리', age=40) #파라미터 명을 지정하면 순서에 상관없음

val = 1  # 전역변수

def valtest (val): #지역변수
    val+=1
    return val

res = valtest(val)
print(val)
print(res)

def valtest2():
    global val # 전역변수 val을 함수 내에서 잠시 가져다 사용
    val+=10

valtest2()
print(val)

# lambda 함수
# javascript jQuery
# 익명함수
# $(document).ready = function() { 익명함수
# }
# $(document).ready () =>{     lambda함수
# }

adds = lambda a, b: a + b
# 동일 기능
# def add(x,y)->any: # int등 가능
#     result  = x + y
#     return result


print(adds(6,8))

print(abs(-3)) #절대값
print(all([1,2,3,5,7,0])) #반복문으로 할수 있는지 -> 사실상 0이 있는지 없는지