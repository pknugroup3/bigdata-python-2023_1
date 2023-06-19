# Q1, 2, 3, 6 11

# Q1
score = { 'korean' : 80 , 'english' : 75, 'math': 55 }

print(score.keys())
total = 0

for item in score.keys():
    total = total + score.get(item)

print("평균 : ",total/3)
print(f'홍길동의 평균 점수는 {total/3} 입니다.')


# Q2
num1 = 13

print("홀수? : ",num1%2==1)

# Q3
pin = "881120-1068234"
# yyyymmdd = pin[:6]
# num = pin[7:] 
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]


print("yyyymmdd : ",yyyymmdd)
print("num : ",num)

# Q6
list1 =[1, 3, 5, 4, 2]
list1.sort()
print("list1 : ", list1)
list1.sort(reverse=True)
print("list1 : ", list1)

# Q11
list2 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
list2Set = set(list2)
list3 = list(list2Set)
print("list3 : ", list3)