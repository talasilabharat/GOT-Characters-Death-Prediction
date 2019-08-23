import matplotlib.pyplot as plt

lines = [line.rstrip('\n') for line in open('score')]

X = []
Y = []
average = 0.0
for i in lines:
	x,y = i.split(' ')
	X.append(int(x))
	average += float(y)
	Y.append(float(y))

average=average/len(Y)

plt.scatter(X, Y, color='k')
plt.plot(X,[average]*len(Y),color='b')
plt.legend(loc='best')
plt.show()

print(X[0],Y[0])
