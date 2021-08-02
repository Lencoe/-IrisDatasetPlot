#import libraries needed

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# used informtion from chartio.com/learn/charts/what-is-a-scatter-plot/
# used w3schools.com/python/matplotlib_scatter.asp
# also used https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html

# Set the shape for 12 subplots

fig, subs = plt.subplots(4,3,figsize=(8,8))  


iris = load_iris() # load the iris datset
data = np.array(iris['data']).astype(np.float64)  # set variable load from iris
targets = np.array(iris['target']).astype(np.float64) # set variable target from iris
 
colors = {0:'r',1:'b',2:"g"} # set colors with each target => 0,, 1, 2
cols = np.array([colors[target] for target in targets]) # Compute colors array using target


# our first row with 3 colums

subs[0][0].scatter(data[:,0], data[:,1], c=cols)
subs[0][1].scatter(data[:,0], data[:,2], c=cols)
subs[0][2].scatter(data[:,0], data[:,3], c=cols)

# secont row contain 3 colums

subs[1][0].scatter(data[:,1], data[:,0], c=cols)
subs[1][1].scatter(data[:,1], data[:,2], c=cols)
subs[1][2].scatter(data[:,1], data[:,3], c=cols)

# row 3 with 4 columns

subs[2][0].scatter(data[:,2], data[:,0], c=cols)
subs[2][1].scatter(data[:,2], data[:,1], c=cols)
subs[2][2].scatter(data[:,2], data[:,3], c=cols)

#Row row 4 with 3 columns

subs[3][0].scatter(data[:,3], data[:,0], c=cols)
subs[3][1].scatter(data[:,3], data[:,1], c=cols)
subs[3][2].scatter(data[:,3], data[:,2], c=cols)

plt.show() # show the plot

