
from faker import Faker 
import pandas as pd

dummy = Faker('ko-KR')
print(dummy.name())
print(dummy.address())
print(dummy.company())

dummy_data = [(dummy.name(), dummy.postcode(), dummy.address(),
            dummy.phone_number(), dummy.email()) for i in range(10000) ]

df = pd.DataFrame(data=dummy_data, columns=['이름','우편번호','주소','전화번호','이메일'])

# print(dummy_data)
df.to_csv('./Day04/dummy_members2.csv',index=False, encoding='utf-8')
print('csv 생성')
