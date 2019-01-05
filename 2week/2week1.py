import pandas
import sklearn
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

import sys
sys.path.append("..")

df = pandas.read_csv('wine.data', header=None)
y = df[0]
X = df.loc[:, 1:]

kf = KFold(5, shuffle=True, random_state=42)
print(kf)


def test_accuracy(kf, X, y):
    scores = list()
    k_range = range(1, 51)
    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        scores.append(cross_val_score(model, X, y, cv=kf, scoring='accuracy'))

    return pandas.DataFrame(scores, k_range).mean(axis=1).sort_values(ascending=False)


X = sklearn.preprocessing.scale(X)
accuracy = test_accuracy(kf, X, y)

top_accuracy = accuracy.head(1)
print(top_accuracy.index[0])
print(top_accuracy.values[0])