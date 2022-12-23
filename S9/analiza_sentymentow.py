import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses

url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset = tf.keras.utils.get_file("aclImdb_v1",url,untar=True, cache_dir='.', cache_subdir='')
dataset_dir = os.path.join(os.path.dirname(dataset),'aclImdb')

os.listdir(dataset_dir)

train_dir = os.path.join(dataset_dir,'train')
os.listdir(train_dir)


sample_file = os.path.join(train_dir,'pos/1181_9.txt')
with open(sample_file) as f:
    print(f.read())
remove_dir = os.path.join(train_dir,'unsup')
shutil.rmtree(remove_dir)

batch_size = 32
seed = 42

raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split = 0.2,
    subset = 'training',
    seed= seed
)

for text_batch, label_batch in raw_train_ds.take(1):
  for i in range(3):
    print("Recenzja",text_batch.numpy()[i])
    print("Etykieta",label_batch.numpy()[i])
print("Etykieta 0 oznacza recenzję: ", raw_train_ds.class_names[0])
print("Etykieta 1 oznacza recenzję: ", raw_train_ds.class_names[1])

raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split = 0.2,
    subset = 'validation',
    seed= seed
)
raw_test_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/test',
    batch_size=batch_size
)
#Przygotowanie zbioru danycb do szkolenia. Standaryzcja, tokenizacja i wektoryzacja.

from tensorflow._api.v2.strings import lower
def custom_standarization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(lowercase,'<br />',' ')
  return tf.strings.regex_replace(stripped_html,'[%s]' %re.escape(string.punctuation),'')

from tensorflow.python.ops.array_ops import sequence_mask
from prompt_toolkit import output
#tworzenie warstwy wektoryzacji
max_features = 10000
sequence_length = 250

vectorize_layer = layers.TextVectorization(
    standardize = custom_standarization,
    max_tokens = max_features,
    output_mode = 'int',
    output_sequence_length = sequence_length
)
