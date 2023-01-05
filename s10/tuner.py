import tensorflow as tf
from tensorflow import keras
!pip install -q -U keras_tuner
import keras_tuner as kt

(img_train, label_train), (img_test,label_test)= keras.datasets.fashion_mnist.load_data()
