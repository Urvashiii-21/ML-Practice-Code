from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
logreg = LogisticRegression()
scores = cross_val_score(logreg, iris.data, iris.target, cv = 3)
print("three cross - validation scores: {}".format(scores))
print("Average cross - validation score : {:.2f}".format(scores.mean()))

scores = cross_val_score(logreg, iris.data, iris.target, cv = 5)
print("five cross - validation scores: {}".format(scores))
print("Average cross - validation score : {:.2f}".format(scores.mean()))
