import tensorflow as tf
import keras.applications 
from keras.utils import multi_gpu_model
import numpy as np
batch_size=64
num_samples = batch_size*5
height = 224
width = 224
num_classes = 1000
n_gpus=8
# Instantiate the base model (or "template" model).
# We recommend doing this with under a CPU device scope,
# so that the model's weights are hosted on CPU memory.
# Otherwise they may end up hosted on a GPU, which would
# complicate weight sharing.
print("Build model")
with tf.device('/cpu:0'):
    model = keras.applications.Xception(weights=None,
                        input_shape=(height, width, 3),
                        classes=num_classes)
# Replicates the model on 8 GPUs.
# This assumes that your machine has 8 available GPUs.

if n_gpus>1:
    print("Replicate model on %d gpus"%(n_gpus))
    parallel_model = multi_gpu_model(model, gpus=n_gpus)
    
else:
    print("Using only 1 gpu")
    parallel_model=model

parallel_model.compile(loss='categorical_crossentropy',
                            optimizer='rmsprop')
# Generate dummy data.
print("Generate random data")
x = np.random.random((num_samples, height, width, 3))
y = np.random.random((num_samples, num_classes))
# This `fit` call will be distributed on 8 GPUs.
# Since the batch size is 256, each GPU will process 32 samples.
print("Begin fitting")
parallel_model.fit(x, y, epochs=2, batch_size=batch_size)
# Save model via the template model (which shares the same weights):
model.save('my_model.h5') 