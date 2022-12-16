import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.set_printoptions(precision=3,suppress=True)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration','Model Year','Origin']

raw_dataset = pd.read_csv(url,names=column_names,na_values="?",comment="\t", sep=" ",skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()

dataset.isna().sum()

dataset = dataset.dropna()

dataset['Origin'] = dataset['Origin'].map({1:'USA',2:'Europe',3:"Japan"})
dataset = pd.get_dummies(dataset,columns=['Origin'], prefix = '',prefix_sep='')
dataset.tail()

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
sns.pairplot(train_dataset[['MPG','Cylinders','Displacement','Weight']],diag_kind='kde')

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

normalizer = tf.keras.layers.Normalization(axis=-1)

normalizer.adapt(np.array(train_features))
print(normalizer.mean.numpy())

first = np.array(train_features[:1])

with np.printoptions(precision=2, suppress=True):
    print(f'Pierwszy element - {first}\n')
    print(f'Znormalizowany: {normalizer(first).numpy()}')

#regresja liniowa z jedną zmienną
horsepower = np.array(train_features['Horsepower'])
horspower_normalizer = layers.Normalization(input_shape=[1,],axis=None)
horspower_normalizer.adapt(horsepower)

horsepower_model = tf.keras.Sequential([
    horspower_normalizer,
    layers.Dense(units=1)
])

horsepower_model.summary()
horsepower_model.predict(horsepower[:10])
horsepower_model.compile(
    optimizer = tf.optimizers.Adam(learning_rate=0.1),
    loss = 'mean_absolute_error'
)
%%time
history = horsepower_model.fit(
    train_features['Horsepower'],
    train_labels,
    epochs=100,
    verbose=0,
    validation_split = 0.2
)
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()
def plot_loss(history):
    plt.plot(history.history['loss'],label='loss')
    plt.plot(history.history['val_loss'],label='val_loss')
    plt.ylim([0,10])
    plt.xlabel('Epoch')
    plt.ylabel('Error[MPG]')
    plt.legend()
    plt.grid(True)
plot_loss(history)
test_results = {}

test_results['horsepower_model'] = horsepower_model.evaluate(
    test_features['Horsepower'],
    test_labels,verbose=0
)
x = tf.linspace(0.0,250,251)
y = horsepower_model.predict(x)
