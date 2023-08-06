from keras import Model
from keras.layers import Input, Dense, Bidirectional, LSTM
import numpy as np
import pandas as pd

# Function to prepare the data in the required 3D format
def prepare_data(data):
    num_samples = len(data['Mouse #'].unique())
    num_timesteps = 4
    num_features = 7

    data_3d = np.zeros((num_samples, num_timesteps, num_features))
    for i, mouse_id in enumerate(data['Mouse #'].unique()):
        mouse_data = data[data['Mouse #'] == mouse_id].drop(columns=['Mouse #', 'Mouse Category'])
        data_3d[i] = mouse_data.values

    return data_3d

# Sample mouse data (replace this with your actual mouse data)
mouse_data = pd.read_csv("path_to_your_mouse_data.csv")

# Prepare the data in 3D format
data_3d = prepare_data(mouse_data)

# Define and compile the model
def define_model():
    input1 = Input(shape=(4, 7))  # Update input shape to (4, 7) for 4 timesteps and 7 features
    lstm1 = Bidirectional(LSTM(units=32))(input1)
    dnn_hidden_layer1 = Dense(3, activation='relu')(lstm1)
    dnn_output = Dense(1, activation='sigmoid')(dnn_hidden_layer1)
    model = Model(inputs=[input1], outputs=[dnn_output])

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model

# Call the model
model = define_model()

# Assuming Y contains the encoded target variable (0 for normal, 1 for alcoholic)
Y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0])

# Fit the model
model.fit(data_3d, Y, epochs=4, batch_size=2, verbose=1)

# Take a test data to test the working of the model
test_data = np.array([[[0.2, 0.33], [0.2, 0.33], [0.2, 0.33], [0.2, 0.33]]])  # Updated test data with shape (1, 4, 7)

# Predict the sigmoid output [0, 1] for the 'test_data'
pred = model.predict(test_data)
print("predicted sigmoid output => ", pred)
