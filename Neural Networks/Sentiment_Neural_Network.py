import tensorflow as tf
import numpy as np
from Create_FeatureSet import create_featuresets_and_labels

train_x, train_y, test_x, test_y = create_featuresets_and_labels('Neural Networks/pos.txt', 'Neural Networks/neg.txt') 

n_nodes_hl = [500, 500, 500]

n_classes = 2
batch_size = 100

x = tf.placeholder('float', [ None, len(train_x[0]) ] )
y = tf.placeholder('float')

def neural_network_model(data):
    
    hidden1_layer = { 'weights' : tf.Variable( tf.random_normal([len(train_x[0] ), n_nodes_hl[0]]) ),
                       'biases' : tf.Variable( tf.random_normal([n_nodes_hl[0]]) )
                    }

    hidden2_layer = { 'weights' : tf.Variable( tf.random_normal([n_nodes_hl[0], n_nodes_hl[1]]) ),
                       'biases' : tf.Variable( tf.random_normal([n_nodes_hl[1]]) )
                    }

    hidden3_layer = { 'weights' : tf.Variable( tf.random_normal([n_nodes_hl[1], n_nodes_hl[2]]) ),
                       'biases' : tf.Variable( tf.random_normal([n_nodes_hl[2]]) )
                    }

    output_layer = { 'weights' : tf.Variable( tf.random_normal([n_nodes_hl[2], n_classes]) ),
                       'biases' : tf.Variable( tf.random_normal([n_classes]) )
                    }

    l1 = tf.add( tf.matmul(data, hidden1_layer['weights']), hidden1_layer['biases'] )
    l1 = tf.nn.relu(l1);

    l2 = tf.add( tf.matmul(l1, hidden2_layer['weights']), hidden2_layer['biases'] )
    l2 = tf.nn.relu(l2);

    l3 = tf.add( tf.matmul(l2, hidden3_layer['weights']), hidden3_layer['biases'] )
    l3 = tf.nn.relu(l3);

    output = tf.add( tf.matmul(l3, output_layer['weights']), output_layer['biases'] )
    return output

def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction, y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    ephocs = 20

    with tf.Session() as sess :

        sess.run(tf.global_variables_initializer())

        for epoch in range(ephocs):
            epoch_cost = 0;
            i = 0
            while i<len(train_x):
                start = i
                end = i+batch_size
                batch_x = np.array( train_x[start:end] )
                batch_y = np.array(train_y[start:end])

                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y} )
                epoch_cost += c
                i+=batch_size
            print("Epoch",epoch+1,"completed with a cost of", epoch_cost)

        correct = tf.equal( tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print("Accuracy :", accuracy.eval({x:test_x, y:test_y})*100,"%")

train_neural_network(x)