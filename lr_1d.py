import numpy as np
import matplotlib.pyplot as plt

#load that data
X = []
Y = []
for line in open('data_1d.csv'):
    x,y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# turn X and Y into numpy array
X = np.array(x)
Y = np.array(y)

plt.scatter(X, Y)
plt.show()