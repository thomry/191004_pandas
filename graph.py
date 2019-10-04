import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset('anscombe')
print(anscombe)
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

#기본형 선그래프
plt.plot(dataset_1['x'],dataset_1['y'])
plt.show()
#점그래프
plt.plot(dataset_1['x'],dataset_1['y'], 'o')
plt.show()

#그래프 격자 기본틀 생성
fig = plt.figure()
#add_subplot(행크기,열크기)
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)
axes1.plot(dataset_1['x'],dataset_1['y'],'o')
axes2.plot(dataset_2['x'],dataset_2['y'],'o')
axes3.plot(dataset_3['x'],dataset_3['y'],'o')
axes4.plot(dataset_4['x'],dataset_4['y'],'o')
#그래프격자에 제목추가
axes1.set_title('dataset_1')
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')
#기본틀 제목추가
fig.suptitle('Anscombe Data')
#레이아웃조젓
fig.tight_layout()
plt.show()

print('-'*100)
print()

tips = sns.load_dataset('tips')
print(tips.head())
fig = plt.figure()
axes1 = fig.add_subplot(1,1,1)
#x축간격=10 bins= 10
axes1.hist(tips['total_bill'], bins=10)
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')
plt.show()