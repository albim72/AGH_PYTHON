import tensorflow as tf

!pip install imageio

!pip install git+https://github.com/tensorflow/docs
  
import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from tensorflow.keras import layers
import time

from IPython import display

(train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()
train_images = train_images.reshape(train_images.shape[0],28,28,1).astype('float32')
train_images = (train_images-127.5)/127.5

BUFFER_SIZE = 60000
BATCH_SIZE = 256
