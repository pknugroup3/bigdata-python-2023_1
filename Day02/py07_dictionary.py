#딕셔너리

iron_man = {'name': 'Tony Stark', 'address': 'New York', 'armer': 'Repulser Arm'} # json과도 일치

print(iron_man)

# 아래 두개 결과 동일
print(iron_man.get('name'))
print(iron_man['name'])

d1 = {1 : 'a', 1 : 'b'}
print(d1) # 키값 중복 X

d2 = {1: 'test', 2: 'test'}
print(d2)

print(iron_man.keys())

for item in iron_man.keys():
    print(item)

print(iron_man.values())    
print(iron_man.items())    