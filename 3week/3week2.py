import pandas
import numpy
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold, cross_val_score, GridSearchCV

newsgroups = datasets.fetch_20newsgroups(
                    subset='all',
                    categories=['alt.atheism', 'sci.space']
             )

X = newsgroups.data
y = newsgroups.target

print(newsgroups)

vectorizer = TfidfVectorizer()
vectorizer.fit_transform(X)

grid = {'C': numpy.power(10.0, range(-5, 6))}
cv = KFold(n_splits=5, shuffle=True, random_state=241)
model = SVC(kernel='linear', random_state=241)
gs = GridSearchCV(model, grid, scoring='accuracy', cv=cv)
gs.fit(vectorizer.transform(X), y)
for i in gs.grid_scores_:
    print(i.mean_validation_score, i.parameters)

C = gs.best_params_.get('C')
print(C)
model = SVC(kernel='linear', random_state=241, C=C)
model.fit(vectorizer.transform(X), y)

words = vectorizer.get_feature_names()
coef = pandas.DataFrame(model.coef_.data, model.coef_.indices)
print(coef)
top_words = coef[0].map(lambda w: abs(w)).sort_values(ascending=False).head(10).index.map(lambda i: words[i])
top_words.sort()
print(top_words)

