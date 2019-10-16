import pandas
import sklearn.metrics as metrics

df = pandas.read_csv('classification.csv', header=None)

x = df[0]
y = df.loc[:, 1:]
print(int(y[1][1]) == 0)
tp = 0
tn = 0
fp = 0
fn = 0
for i in range(1, 201):
    if y[1][i] == x[i]:
        if int(x[i]) == 1:
            tp += 1
        elif int(x[i]) == 0:
            tn += 1
    else:
        if int(y[1][i]) == 1:
            fp += 1
        elif int(x[i]) == 1:
            fn += 1

print(tp, fp, fn, tn)
x1 = []
y1 = []
for j in y[1][1:]:
    y1.append((int(j)))
for i in x[1:]:
    x1.append(int(i))
print(len(x1), len(y1))
acc = metrics.accuracy_score(x1, y1)
pr = metrics.precision_score(x1, y1)
rec = metrics.recall_score(x1, y1)
f1 = metrics.f1_score(x1, y1)

print(acc, pr, rec, f1)
df2 = pandas.read_csv('scores.csv')
print(df2.columns[1:])
for clf in df2.columns[1:]:
    print(df2[clf])
