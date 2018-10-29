import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Dropout, Input
from keras.layers import LSTM, concatenate
from keras.models import Model
from keras.layers.embeddings import Embedding
from keras.layers.advanced_activations import ELU
from keras.regularizers import l2
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
from keras.models import load_model
import keras as ks
set_of_all_score_classes = [0, 1, 2, 3]
texts = []
labels_index = {}
labels = []
word_counts = []
sent_counts = []
num_words = 500
nltk.download('punkt')
english_stop_words = set(stopwords.words('english'))

np.random.seed(7)
data = pd.read_table('train.tsv' )
data1 = pd.read_table('train_rel_2.tsv')

data = [data, data1]
data = pd.concat(data)

essay_text = data['EssayText']
essay_score = data['Score1']
essay_set = data['EssaySet']


for x in essay_text:
    word_counts.append(len([i for i in word_tokenize(x) if i not in english_stop_words]))



for x in essay_text:
    sent_counts.append(len(sent_tokenize(x)))


for label in set_of_all_score_classes:
	label_id = len(labels_index)
	labels_index[label] = label_id
	for t in essay_text[data['Score1']==label]:
		texts.append(t)
		labels.append(label_id)




tokenizer = Tokenizer(num_words=num_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
max_response_length = 500
data = pad_sequences(sequences, maxlen=max_response_length)
labels = to_categorical(np.asarray(labels))
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]





word_counts = np.array(word_counts)
word_counts = word_counts[indices]
sent_counts = np.array(sent_counts)
sent_counts = sent_counts[indices]
essay_set = np.array(essay_set)
essay_set = essay_set[indices]
train_size = int(0.85 * len(data))
X_train = data[:train_size]
X_test = data[train_size:]
set_train = essay_set[:train_size]
set_test = essay_set[train_size:]
sent_count_train = sent_counts[:train_size]
sent_count_test = sent_counts[train_size:]
word_count_test = word_counts[train_size:]
word_count_train = word_counts[:train_size]
features_train = np.column_stack((set_train,sent_count_train,word_count_train))
features_test = np.column_stack((set_test,sent_count_test,word_count_test))
y_train = labels[:train_size]
y_test = labels[train_size:]



text_in = Input(shape=(500,), name='text')
embedding = Embedding(output_dim=32, input_dim=num_words, input_length=500)(text_in)
lstm_1 = LSTM(100, return_sequences=True)(embedding)
lstm_2 = LSTM(150)(lstm_1)
features_in = Input(shape=(3,), name='features')
x = concatenate([lstm_2, features_in])
dropout = Dropout(0.2)(x)
D1 = Dense(200, kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01))(dropout)
ED1 = ELU()(D1)
score = Dense(4, activation='softmax', name='score', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01))(ED1)
model = Model(inputs=[text_in, features_in], outputs=[score])
model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])
model.fit([X_train,features_train], y_train, epochs = 200, batch_size=32, validation_split=0.2)
model.save('functional_model6.h5')
#model = load_model('functional_model6.h5')
scores = model.evaluate([X_test,features_test], y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))


def encode_text(text , ques_id):
    token = Tokenizer(num_words=num_words)
    token.fit_on_texts(texts)
    sequences = token.texts_to_sequences([text])
    output = pad_sequences(sequences, maxlen=500)
    sent_countence = len(sent_tokenize(text))
    word_countence = len(word_tokenize(text))
    res = [np.array(output) , np.column_stack((ques_id,sent_countence,word_countence))]
    return model.predict(res)
  .    

to_predict = encode_text('You would need many more pieces of information to replicate the experiment. You would need the type of samples to begin with in the procedure. You would also need to know the amount of vinegar used in each container. You would also need to know exactly how to mass the samples and what types of container to use (plastic for example, might alter the results).' , 1)
print(to_predict)





