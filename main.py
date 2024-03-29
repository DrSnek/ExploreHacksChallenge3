  
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from assist import *

data = pd.read_csv("test.csv")
data = data[['Fancy Words', 'Distance']]
matrix = np.array(data.values, "float")

X = matrix[:, 0]
y = matrix[:, 1]
X = X / (np.max(X))

m = np.size(y)
X = X.reshape([len(X), 1])
x = np.hstack([np.ones_like(X), X])

theta = np.zeros([2, 1])
theta, J = gradient(x, y, theta, m)

plt.plot(X, y, 'k' , marker="," )
plt.plot(X, x @ theta, '-')
plt.ylabel("Distance")

plt.xlabel('Fancy Words')
plt.title('Fancy Words vs Distance')
plt.show()
print("The final cost comes as " + str(computeCost(x, y, theta, m))) 


#final cost = 756.4073367032673