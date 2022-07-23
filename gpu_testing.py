
import tensorflow as tf
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
print(f"Tensorflow version: {tf.__version__}")
print(f"Keras Version: {tf.keras.__version__}")
print("GPU is", "available" if tf.config.list_physical_devices('GPU') else "NOT AVAILABLE")

