import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

n_neighbours = 3
random_state = 0

X,y = datasets.load_digits(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.5, stratify=y,random_state=random_state
)

dim = len(X[0])
n_classes = len(np.unique(y))

pca = make_pipeline(StandardScaler(),PCA(n_components=2,random_state=random_state))

lda = make_pipeline(StandardScaler(), LinearDiscriminantAnalysis(n_components=2))

nca = make_pipeline(StandardScaler(), NeighborhoodComponentsAnalysis(n_components=2,random_state=random_state))
