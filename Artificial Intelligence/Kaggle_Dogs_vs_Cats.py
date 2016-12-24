
import glob
import os
import PIL

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf



def resize_image(img, size):
    # Resize
    n_x, n_y = img.size
    if n_y > n_x:
        n_y_new = size
        n_x_new = int(size * n_x / n_y + 0.5)
    else:
        n_x_new = size
        n_y_new = int(size * n_y / n_x + 0.5)

    img_res = img.resize((n_x_new, n_y_new), resample=PIL.Image.BICUBIC)

    # Pad the borders to create a square image
    img_pad = PIL.Image.new('RGB', (size, size), (128, 128, 128))
    ulc = ((size - n_x_new) // 2, (size - n_y_new) // 2)
    img_pad.paste(img_res, ulc)

    return img_pad


def getImage(fileList):
    imageList = [PIL.Image.open(fileName) for fileName in fileList]
    imageList = [np.array(resize_image(image, SIZE)) for image in imageList]
    return np.array(imageList)


def conv2d(x, filter_weights, stride):
    return tf.nn.conv2d(input=x, filter=filter_weights, strides=[1, stride, stride, 1], padding='SAME')

def maxpool2d(x, stride):
  return tf.nn.max_pool(value=x, ksize=[1, stride, stride, 1], strides=[1, stride, stride, 1], padding='SAME')

def relu(x):
    return tf.nn.relu(x)

def convolutional_neural_network():
    
    weights = {
        # 3x3x3 conv => 1x1x8
        'conv1': tf.Variable(tf.random_normal([3, 3, 3, 8])),
        # 5x5x8 conv => 1x1x16
        'conv2': tf.Variable(tf.random_normal([5, 5, 8, 16])),
        # 3x3x16 conv => 1x1x32
        'conv3': tf.Variable(tf.random_normal([3, 3, 16, 32])),
        # 32 FC => output_features
        'out': tf.Variable(tf.random_normal([(SIZE//16)*(SIZE//16)*32, output_features]))
    }

    biases = {
        'conv1': tf.Variable(tf.random_normal([8])),
        'conv2': tf.Variable(tf.random_normal([16])),
        'conv3': tf.Variable(tf.random_normal([32])),
        'out': tf.Variable(tf.random_normal([output_features]))
    }
    conv1 = tf.add(conv2d(input_placeholder, weights['conv1'], 1), biases['conv1'])
    relu1 = relu(conv1)
    pool1 = maxpool2d(relu1, 4)

    conv2 = tf.add(conv2d(pool1, weights['conv2'], 1), biases['conv2'])
    relu2 = relu(conv2)
    pool2 = maxpool2d(relu2, 2)

    conv3 = tf.add(conv2d(pool2, weights['conv3'], 1), biases['conv3'])
    relu3 = relu(conv3)
    pool3 = maxpool2d(relu3, 2)

    pool3 = tf.reshape(pool3 , shape=[-1, (SIZE//16)*(SIZE//16)*32])

    output = tf.add(tf.matmul(pool3, weights['out']), biases['out'])
    return output


def train_neural_network():
    
    output_prediction = convolutional_neural_network()
    loss = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(output_prediction, output_placeholder) )
    trainer = tf.train.AdamOptimizer()
    optimizer = trainer.minimize(loss)
    test_prediction = tf.argmax(tf.nn.softmax(output_prediction), 1)

    with tf.Session() as sess :
        sess.run(tf.initialize_all_variables())

        # Train Neural Net
        print("\nTraining Neural Net ... ")
        ephocs = 200
        for epoch in range(ephocs):
            epoch_loss = 0
            i = 0
            while i < len(train_files):
                train_images = getImage( train_files[i:i+BATCH_SIZE] ) 
                _, l = sess.run([optimizer, loss], feed_dict={input_placeholder: train_images, output_placeholder: train_labels[i:i+BATCH_SIZE]} )
                epoch_loss += l 
                print(i)
                i+=BATCH_SIZE
            print("Epoch",epoch+1,"completed with a cost of", epoch_loss)


        # Predict Test Data
        test_labels = np.array([])
        i = 0
        while i < len(test_files):
            test_images = getImage(test_files[i:i+BATCH_SIZE] ) 
            partial_labels = test_prediction.eval(feed_dict={input_placeholder : test_images})
            partial_labels = [ [i+k+1, partial_labels[k]] for k in range(len(partial_labels)) ]
            test_labels = np.append(test_labels, partial_labels)
            print(i)
            i+=BATCH_SIZE

        # Saving Prediction in CSV    
        test_labels = np.reshape(test_labels, (-1, 2))
        np.savetxt("/home/dollarakshay/Documents/Machine Learning Data/Dogs vs Cats/prediction.csv", 
            test_labels, delimiter=',', header='id,label', fmt='%.0f', newline='\n', comments='')

        

SIZE = 112
BATCH_SIZE = 64
input_features = [None, SIZE, SIZE, 3]
output_features = 2
input_placeholder = tf.placeholder('float', input_features)
output_placeholder = tf.placeholder('float', [None, output_features])

#Train Data
TRAIN_DIR = '/home/dollarakshay/Documents/Machine Learning Data/Dogs vs Cats/train'
train_cats = sorted(glob.glob(os.path.join(TRAIN_DIR, 'cat*.jpg')))
train_dogs = sorted(glob.glob(os.path.join(TRAIN_DIR, 'dog*.jpg')))
train_files = train_cats + train_dogs
print(len(train_files))
train_labels = [([0, 1] if 'dog' in file else [1, 0]) for file in train_files]


## Test Data
TEST_DIR = '/home/dollarakshay/Documents/Machine Learning Data/Dogs vs Cats/test'
test_files = sorted(glob.glob(os.path.join(TEST_DIR, '*.jpg')))
train_neural_network()