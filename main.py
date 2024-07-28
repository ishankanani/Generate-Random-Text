from __future__ import absolute_import, division, print_function, unicode_literals 

import numpy as np 
import tensorflow as tf 

from keras.models import Sequential 
from keras.layers import Dense, Activation 
from keras.layers import LSTM 

from keras.optimizers import RMSprop 

from keras.callbacks import LambdaCallback 
from keras.callbacks import ModelCheckpoint 
from keras.callbacks import ReduceLROnPlateau 
import random 
import sys  
# network's learnings 
def generate_text(length, diversity): 
	# Get random starting text 
	start_index = random.randint(0, len(text) - max_length - 1) 
	generated = '' 
	sentence = text[start_index: start_index + max_length] 
	generated += sentence 
	for i in range(length): 
			x_pred = np.zeros((1, max_length, len(vocabulary))) 
			for t, char in enumerate(sentence): 
				x_pred[0, t, char_to_indices[char]] = 1.

			preds = model.predict(x_pred, verbose = 0)[0] 
			next_index = sample_index(preds, diversity) 
			next_char = indices_to_char[next_index] 

			generated += next_char 
			sentence = sentence[1:] + next_char 
	return generated 

print(generate_text(500, 0.2)) 

