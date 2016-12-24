import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
import cv2

fileList = [f for f in listdir("Competitive Coding/Test_Data/Reshaped Images") if isfile(join("Competitive Coding/Test_Data/Reshaped Images", f))]

ip_pixels = 128*128
op_pixels = 128*128
train_images = []
train_masks= []
test_images = []
test_image_shapes = []

for i in range(164):
    image = cv2.imread("Competitive Coding/Train_Data/train-"+str(i)+".jpg", cv2.IMREAD_GRAYSCALE)
    #image = np.divide(image, 255)
    image = np.reshape(image, (1, ip_pixels) )
    train_images.append(image)

    mask = cv2.imread("Competitive Coding/Train_Data/train-"+str(i)+"-mask.jpg", cv2.IMREAD_GRAYSCALE)
    #mask = np.divide(mask, 255)
    mask = np.reshape(mask, (1, op_pixels) )
    train_masks.append(mask)
    

for i in range(len(fileList)):
    image = cv2.imread("Competitive Coding/Test_Data/Reshaped Images/"+fileList[i], cv2.IMREAD_GRAYSCALE)
    #image = np.divide(image, 255)
    test_image_shapes.append(image.shape)
    test_images.append(image)
    

n_nodes_hl = [5000, 5000, 5000]
input_placeholder = tf.placeholder(shape=[1, ip_pixels], dtype=tf.float32)
output_placeholder = tf.placeholder(shape=[1, op_pixels], dtype=tf.float32)


def neural_network_model():
    
    hidden1_layer = { 'weights' : tf.Variable( tf.random_normal([ip_pixels, n_nodes_hl[0]]) ),
                       'biases' : tf.Variable( tf.random_normal([n_nodes_hl[0]]) )
                    }

    hidden2_layer = { 'weights' : tf.Variable( tf.random_normal([n_nodes_hl[0], n_nodes_hl[1]]) ),
                       'biases' : tf.Variable( tf.random_normal([n_nodes_hl[1]]) )
                    }

    #hidden3_layer = { 'weights' : tf.Variable( tf.random_normal([n_nodes_hl[1], n_nodes_hl[2]]) ),
    #                   'biases' : tf.Variable( tf.random_normal([n_nodes_hl[2]]) )
    #                }

    output_layer = { 'weights' : tf.Variable( tf.random_normal([n_nodes_hl[1], op_pixels]) ),
                       'biases' : tf.Variable( tf.random_normal([op_pixels]) )
                    }

    l1 = tf.add( tf.matmul(input_placeholder, hidden1_layer['weights']), hidden1_layer['biases'] )
    l1 = tf.nn.sigmoid(l1)

    l2 = tf.add( tf.matmul(l1, hidden2_layer['weights']), hidden2_layer['biases'] )
    l2 = tf.nn.sigmoid(l2)

    #l3 = tf.add( tf.matmul(l2, hidden3_layer['weights']), hidden3_layer['biases'] )
    #l3 = tf.nn.sigmoid(l3)

    output = tf.add( tf.matmul(l2, output_layer['weights']), output_layer['biases'] )
    output = tf.nn.sigmoid(output)

    return output

#Define Neural Network Model
output_prediction = neural_network_model()
loss = tf.reduce_sum( tf.square(output_prediction - output_placeholder) )
trainer = tf.train.AdamOptimizer()
optimizer = trainer.minimize(loss)


with tf.Session() as sess :

    sess.run(tf.initialize_all_variables())

    # Train Neural Net
    print("\nTraining Neural Net ... ")
    ephocs = 10
    for epoch in range(ephocs):
        epoch_loss = 0
        for i in range(len(train_images)):
            _, l = sess.run([optimizer, loss], feed_dict={input_placeholder: train_images[i], output_placeholder: train_masks[i]} )
            epoch_loss += l 
            print(i)
        print("Epoch",epoch,"completed with a cost of", epoch_loss)


    # Predict Masks
    print("\nPredicting Test Data ... ")
    for i in range(len(test_images)):

        px = 0
        py = 0
        mask_prediction = np.zeros(test_image_shapes[i])

        while py < test_image_shapes[i][0]:

            partial_image = test_images[i][py:py+128, px:px+128]
            partial_image = np.reshape(partial_image, (1, ip_pixels))
            
            partial_mask_prediction = sess.run([output_prediction], feed_dict={input_placeholder: partial_image} )
            partial_mask_prediction = np.multiply(np.round(partial_mask_prediction), 255)

            mask_prediction[py:py+128, px:px+128] = np.reshape(partial_mask_prediction, (128, 128))
            px+=128
            if px >= test_image_shapes[i][1]:
                px = 0
                py += 128

        fileName = fileList[i][:-4]+"-mask.jpg"
        cv2.imwrite( "Competitive Coding/Test_Data/Predicted Masks/"+fileName, mask_prediction )

    print("\nDone ...")

