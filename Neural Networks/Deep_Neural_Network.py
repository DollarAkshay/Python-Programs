import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

n_nodes_hl = [500, 500, 500]

n_classes = 10
batch_size = 100

x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

def neural_network_model(data):
    
    hidden1_layer = { 'weights' : tf.Variable( tf.random_normal([784, n_nodes_hl[0]]) ),
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

    ephocs = 10

    with tf.Session() as sess :

        sess.run(tf.global_variables_initializer())

        for epoch in range(ephocs):
            epoch_cost = 0;
            for _ in range(int(mnist.train.num_examples/batch_size)):
                ex, ey = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: ex, y: ey} )
                epoch_cost += c
            print("Epoch",epoch,"completed with a cost of", epoch_cost)

        correct = tf.equal( tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print("Accuracy :", accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))


train_neural_network(x)