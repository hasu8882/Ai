from sklearn import svm, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt


#데이터 읽기
wine = pd.read_csv("wine.csv",header = 0, sep=';')




#데이터 가공
data = wine.iloc[:,0:11]
label = wine['quality']
transformer = MinMaxScaler()
transformer.fit(data)
data = transformer.transform(data)



#label = np.array(["good" if i>=6 else "bad" for i in label])


#데이터 분할
train_data, test_data, train_label, test_label =  \
    train_test_split(data, label, test_size = 0.2, shuffle = True)

#학습
clf = RandomForestClassifier()
clf.fit(train_data, train_label)

#예측
predict = clf.predict(test_data)

#결과
ac_score = metrics.accuracy_score(test_label, predict)
cl_report = metrics.classification_report(test_label, predict)

print(f"정확도 : {ac_score}")
print(f"리포트 : \n",cl_report)

#그래프데이터 가져오기
table = pd.read_csv("wine.csv", index_col =11, sep=';')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


#그래프 그리기 및 색상
def scatter(lbl, color):
    b = table.loc[lbl]
    ax.scatter(b["alcohol"], b["fixed acidity"], c=color, label=lbl)


scatter(3, "brown")
scatter(4, "purple")
scatter(5, "blue")
scatter(6, "green")
scatter(7, "orange")
scatter(8, "yellow")


#범주 보여주기
ax.legend()
#그래프 저장
plt.savefig("wine-test.png")
