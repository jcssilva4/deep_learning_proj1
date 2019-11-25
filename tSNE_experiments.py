import numpy as np

#t-SNE
from sklearn.manifold import TSNE #i think we should use this after the dataset generation

# importing python plotting libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
from IPython.display import Image, display

latentVecDim = 3
tau = 5

datasetFile = open("latent_data_sets/ldim" + str(latentVecDim) + "_tau" + str(tau) +"_basisLS.txt","r")
#initialize X, Y
X = []
Y = []
#read data set
for L in datasetFile:
	XY = L.split('\t')
	X.append([float(z) for z in XY[0:len(XY)-1]]) # get feature values for object L
	y = XY[len(XY)-1].split('\n')
	Y.append(int(y[0])) # get object L label

# separate different types of entries
regular_data = []
global_outliers = []
local_outliers = []
index = 0

for data_entry in Y:
	if data_entry == 0: #regular
		regular_data.append(X[index])
	if data_entry == 1: #global
		global_outliers.append(X[index])
	if data_entry == 2: #local
		local_outliers.append(X[index])
	index += 1


regular_data = np.array(regular_data)
global_outliers = np.array(global_outliers)
local_outliers = np.array(local_outliers)

# init the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection = '3d')

print(global_outliers)

# plot reconstruction error scatter plot
#regular_data = regular_data []

ax.scatter(regular_data[0:1000, 0], regular_data[0:1000, 1], regular_data[0:1000, 2], c='C0', marker="o", label='regular', edgecolors='w', linewidth=0.5) # plot regular transactions
ax.scatter(global_outliers[:, 0], global_outliers[:, 1], global_outliers[:, 2], c='C1', marker="x", label='global', edgecolors='w', s=60) # plot global outliers
ax.scatter(local_outliers[:, 0], local_outliers[:, 1], local_outliers[:, 2], c='C3', marker="x", label='local', edgecolors='w', s=60) # plot local outliers
ax.set_xlabel("z1")
ax.set_ylabel("z2")
ax.set_zlabel("z3")
# add plot title
ax.set_title('Prior Latent Space Distribution $p(z)$');
plt.show()