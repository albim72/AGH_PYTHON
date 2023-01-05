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

knn = KNeighborsClassifier(n_neighbors=n_neighbours)
dim_reduction_methods = [("PCA",pca),("LDA",lda),("NCA",nca)]
#wykres

for i, (name,model) in enumerate(dim_reduction_methods):
    model.fit(X_train,y_train)
    knn.fit(model.transform(X_train),y_train)

    acc_knn = knn.score(model.transform(X_test),y_test)

    X_embedded = model.transform(X)

    plt.scatter(X_embedded[:,0], X_embedded[:,1], c=y,s=30,cmap="Set1")
    plt.title("{}, KNN (k={})\nTest accuracy = {:.2f}".format(name,n_neighbours,acc_knn))
plt.show()

