import pandas as pd

s = pd.Series(['banana',42])
print(s)

#데이터프레임 만들기 딕셔너리 전달
scientists = pd.DataFrame(
    data = {'Occupation' : ['Chemist','Statistician'],
            'Born'       : ['1920-07-25','1876-06-13'],
            'Died'       : ['1958-04-16','1937-10-16'],
            'Age'        : [37,61]},
    index = ['Roaline Franklin','William Gosset'],
    columns = ['Occupation','Born','Age','Died']
)
print(scientists)

#순서가 보장된 dataframe 만들기 ordereddict 사용해보기
from collections import OrderedDict
scientists2 = pd.DataFrame(OrderedDict([
    ('Name',['Roaline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])
])
)
print(scientists2)

