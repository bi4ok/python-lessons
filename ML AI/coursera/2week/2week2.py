import pandas
import sklearn
import sklearn.datasets
from numpy import linspace
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsRegressor


data = sklearn.datasets.load_boston()
X = data.data
y = data.target

X = sklearn.preprocessing.scale(X)

kf = KFold(5, shuffle=True, random_state=42)


def test_accuracy(kf, X, y):
    scores = list()
    p_range = linspace(1, 10, 200)
    for p in p_range:
        model = KNeighborsRegressor(p=p, n_neighbors=5, weights='distance')
        scores.append(cross_val_score(model, X, y, cv=kf, scoring='neg_mean_squared_error'))

    return pandas.DataFrame(scores, p_range).max(axis=1).sort_values(ascending=False)


accuracy = test_accuracy(kf, X, y)
top_accuracy = accuracy.head(1)
print(accuracy)