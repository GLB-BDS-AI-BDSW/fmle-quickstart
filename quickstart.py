import sys
import gzip
import pickle

import tensorflow as tf

def main():
    # Load MNIST dataset
    f = gzip.open('/MNIST/mnist.pkl.gz', 'rb')
    if sys.version_info < (3,):
        data = pickle.load(f)
    else:
        data = pickle.load(f, encoding='bytes')
    f.close()

    (x_train, y_train), (x_test, y_test) = data
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Define model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])

    predictions = model(x_train[:1]).numpy()
    tf.nn.softmax(predictions).numpy()

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()

    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

    # Train model
    model.fit(x_train, y_train, epochs=5)

    # Eval model
    model.evaluate(x_test,  y_test, verbose=2)

if __name__ == '__main__':
    main()