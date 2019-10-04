import pandas as pd
import random, xlwt, openpyxl

scientists = pd.read_csv('scientists.csv')
ages = scientists['Age']
print(ages.max())
print('-'*50)
print()

#나이 평균넘은 리스트 boolean
print(ages[ages > ages.mean()])
print('-'*50)
print()

#ages 스칼라
print(ages+ages)
print('-'*50)
print()

#nan
print(ages+pd.Series([1,100]))
print('-'*50)
print()

#index역순정렬
print(ages.sort_index(ascending=False))
print('-'*50)
print()

#vector와 vector의 연산은 일치하는 인덱스 끼리 수행합니다.
print('vector 연산')
print((ages*2) == (ages+ages.sort_index(ascending=False)))
print('-'*50)
print()

#age열에서 age열의 평균보다 높은 행만 출력
print(scientists[ages > ages.mean()])
print('-'*50)
print()

#broadcasting
print(scientists*2)
print('-'*50)
print()

#태어난날, 죽은날을 datetime 자료형으로 바꾸어 format속성지정해 날짜형식지정후 얼마나 살다갔는지 계산해보기
born_datetime = pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'],format='%Y-%m-%d')
scientists['born_dt'],scientists['died_dt']=(born_datetime,died_datetime)
#print(scientists.head())
scientists['age_days_dt'] = (scientists['died_dt']-scientists['born_dt'])
print(scientists)
print('-'*50)
print()

#series, dataframe의 data 섞기
random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])
print('-'*50)
print()


#dataframe의 columns delete
print(scientists.columns)
scientists_dropped = scientists.drop(['Age'],axis=1)
print(scientists_dropped.columns)
scientists_dropped2 = scientists.drop(['Died'],axis=1)
print(scientists_dropped2.columns)
print('-'*50)
print()

#pickle
names = scientists['Name']
names.to_pickle('scientists_names_series.pickle')
scientists_names_from_pickle = pd.read_pickle('scientists_names_series.pickle')
print(scientists_names_from_pickle)

#csv,tsv,excel
names.to_csv('scientist_names_series.csv')
scientists.to_csv('scientists_df.tsv',sep='\t')
names_df = names.to_frame()
names_df.to_excel('scientists_names_series_df.xls')
names_df.to_excel('scientists_names_series_df.xlsx')
