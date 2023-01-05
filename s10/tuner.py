import tensorflow as tf
from tensorflow import keras
!pip install -q -U keras_tuner
import keras_tuner as kt

(img_train, label_train), (img_test,label_test)= keras.datasets.fashion_mnist.load_data()
from tensorflow.python import train
img_train = img_train.astype('float32')/255.0
img_test = img_test.astype('float32')/255.0
