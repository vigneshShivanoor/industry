import numpy as np
import keras.models
from keras.models import model_from_json
# from tensorflow.keras.models import Sequential
import tensorflow as tf


def init(): 
	json_file = open('lc.json','r')
	loaded_model_json = json_file.read()
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights("lc.h5")
	print("Loaded Model from disk")
	loaded_model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	graph = tf.compat.v1.get_default_graph()

	return loaded_model,graph
init()