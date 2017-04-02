import csv 
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

data = open("microsoftdata.csv","r")
reader = csv.reader(data)

X = []
y = []
Xtest = []
ytest = []
count = 0
threshold = int(718 * .7)

for line in reader:
	
	if (line[1] != "close" and (not math.isnan(float(line[2])))):
		t = [float(line[1]), int(float(line[2]))]
		label = line[3]
		if (count < threshold):
			y.append(int(label))
			X.append(t)
		else:
			Xtest.append(t)
			ytest.append(int(label))
		count+=1
		
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X, y)

ypred = []
for k in Xtest:
	ypred.append(clf.predict(k))

print confusion_matrix(ytest, ypred)

print(clf.score(Xtest, ytest))		
		


	
	

