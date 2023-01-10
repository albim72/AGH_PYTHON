import os
import tensorflow as tf
from tensorflow import keras

(train_images, train_labels), (test_images,test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1,28*28)/255.0
test_images = test_images[:1000].reshape(-1,28*28)/255.0

def create_model():
  model = tf.keras.models.Sequential([
      keras.layers.Dense(512,activation='relu',input_shape=(784,)),
      keras.layers.Dropout(0.2),
      keras.layers.Dense(10)
  ])

  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.metrics.SparseCategoricalAccuracy()])
  return model

model = create_model()
model.summary()
#użycie wołania zwrotnego w punkcie kontrolnym (checkpoint)

checkpoint_path = 'training_1/cp.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
model.fit(train_images,
          train_labels,
          epochs=10,
          validation_data = (test_images,test_labels),
          callbacks=[cp_callback])
os.listdir(checkpoint_dir)

model = create_model()
loss, acc = model.evaluate(test_images,test_labels,verbose=2)
print(f"model niewytrenowoany:accuracy {(100*acc):5.2f}")

model.load_weights(checkpoint_path)
loss, acc = model.evaluate(test_images,test_labels,verbose=2)
print(f"model niewytrenowoany:accuracy {(100*acc):5.2f}")

#opcje oddzwaniania do punktu kontrolnego

checkpoint_path = 'training_2/cp-{epoch:04d}.ckpt'
checkpoint_dir=os.path.dirname(checkpoint_path)

batch_size = 32

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath = checkpoint_path,
    verbose=1,
    save_weights_only = True,
    save_freq = 5*batch_size
)

model = create_model()
model.save_weights(checkpoint_path.format(epoch=0))

model.fit(train_images,
          train_labels,
          epochs=50,
          batch_size=batch_size,
          callbacks = [cp_callback],
          validation_data=(test_images,test_labels),
          verbose=0
          )

os.listdir(checkpoint_dir)
latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)
#ręczne zapisywanie wag
model.save_weights('./checkpoints/my_chceckpoint')

#reset modelu i załadowanie najnowszego punktu kontrolnego

model = create_model()
model.load_weights('./checkpoints/my_chceckpoint')
loss, acc = model.evaluate(test_images,test_labels,verbose=2)
print(f"model niewytrenowoany:accuracy {(100*acc):5.2f}")

model = create_model()
model.fit(train_images,train_labels,epochs=5)

!mkdir -p saved_model
model.save('saved_model/my_model')
!ls saved_model
!ls saved_model/my_model
