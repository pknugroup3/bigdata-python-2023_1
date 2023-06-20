#파일 입출력
# DB open / close Network open / close File open / close
import os
cur_path = os.getcwd() # 현재 파이썬 경로
# print(cur_path)

filename ='./Day03/sample.txt' 
# filename ='file:' 
# filename ='C:\\Source\\bigdata-python-2023\\Day03\\test.txt' #절대 경로
f = open(filename, mode='wt',encoding='utf-8') # 텍스트 파일 생성 (default ascii code )

f.write('하이하이 \n')
f.write('하이하이 ')
# print(f.readline())

f.close() #무조건 닫아줘야함
print(f'{filename}파일이 생성 되었습니다.')

fr = open(filename,mode='r',encoding='utf-8')
while True: #무한 루프
    line = fr.readline() # 한줄씩 읽기
    if not line: break; #읽을 줄이 없으면 빠져나감
    print(line, end='')


fr.close()
