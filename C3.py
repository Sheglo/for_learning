from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
print("Accuracy:", clf.score(X_test, y_test))
