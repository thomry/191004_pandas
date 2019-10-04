import pandas as pd

df = pd.read_csv('gapminder.tsv',sep='\t')

country_df = df['country']

#lifeExp 열을 연도별로 그룹화하여 평균계산 코드
print(df.groupby('year')['lifeExp'].mean())

#lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여 한번에 계산
multi_group_var = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
print(multi_group_var)

import matplotlib.pyplot as plt

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
global_yearly_life_expectancy.plot()
