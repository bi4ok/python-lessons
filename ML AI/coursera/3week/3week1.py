import pandas
from sklearn.svm import SVC

svmdata = pandas.read_csv('svm-data.csv', header=None)
y = svmdata[0]
X = svmdata.loc[:, 1:]

klas = SVC(kernel='linear', C=100000, random_state=241)
klas.fit(X, y)

opor = klas.support_
print(opor)