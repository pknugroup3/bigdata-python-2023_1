# 입출력
import datetime # 날짜를 모듈 가져옴


birth_year = 1998 #int(input('출생 년도를 입력하세요 > ')) # 키보드 입력 -> 무조건 String

print(f'당신의 출생 년도는 {birth_year}년도 입니다')

curr_year = datetime.datetime.now().year # datetime.datetime.now() -> yyyy-MM-dd hh:mm:ss.ms
#print(curr_year)
age = curr_year-birth_year
print(f'당신의 나이는 {age}세 입니다.')

a = 123 
a = [3, 6, 9]
print(a)

print('Life' 'is' 'short')
print('Life' + 'is' + 'short')
print('Life' , 'is' , 'short')
print('Life' , 1.234 , True)

print(range(10))

for i in range(10):
    if i == (len(range(10))-1):
            print(i,end='\n') #end 엔터를 없앨 때
    else:
        print(i, end=', ')


print('life','is','short',sep='&')

pi = 3.13159265359

print(f'PI = {pi:.4f}') # format String
print(f'PI = {pi:10.2f}')