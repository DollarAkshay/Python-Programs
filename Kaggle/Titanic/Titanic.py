import pandas
import numpy as np
import tensorflow as tf

titanic_train = pandas.read_csv("Kaggle/Titanic/train.csv")
titanic_test = pandas.read_csv("Kaggle/Titanic/test.csv")

ip_features = 7
op_classes = 1
batch_size = 128

x = tf.placeholder('float', [None, ip_features])
y = tf.placeholder('float')

#Fill up empty cells
def cleanUpData(file):
    
    file["Age"] = file["Age"].fillna(file["Age"].median())
    file["Embarked"] = file["Embarked"].fillna("S")

# Convert text data into numericals
def preprocess(file, columns_to_ignore):

    file.drop(file.columns[columns_to_ignore], axis=1, inplace=True)

    cleanUpData(file)

    file.loc[file["Sex"] == "male", "Sex"] = 0
    file.loc[file["Sex"] == "female", "Sex"] = 1

    file.loc[file["Embarked"] == "S", "Embarked"] = 0
    file.loc[file["Embarked"] == "C", "Embarked"] = 1
    file.loc[file["Embarked"] == "Q", "Embarked"] = 2

    return file

def neural_network_model(data):
    
    hidden1_layer = { 'weights' : tf.Variable( tf.random_normal([ip_features, 20]) ),
                       'biases' : tf.Variable( tf.random_normal([20]) )
                    }

    hidden2_layer = { 'weights' : tf.Variable( tf.random_normal([20, 20]) ),
                       'biases' : tf.Variable( tf.random_normal([20]) )
                    }

    hidden3_layer = { 'weights' : tf.Variable( tf.random_normal([20, 20]) ),
                       'biases' : tf.Variable( tf.random_normal([20]) )
                    }

    output_layer = { 'weights' : tf.Variable( tf.random_normal([20, op_classes]) ),
                       'biases' : tf.Variable( tf.random_normal([op_classes]) )
                    }

    l1 = tf.add( tf.matmul(data, hidden1_layer['weights']), hidden1_layer['biases'] )
    l1 = tf.nn.relu(l1);

    l2 = tf.add( tf.matmul(l1, hidden2_layer['weights']), hidden2_layer['biases'] )
    l2 = tf.nn.relu(l2);

    l3 = tf.add( tf.matmul(l2, hidden3_layer['weights']), hidden3_layer['biases'] )
    l3 = tf.nn.relu(l3);

    output = tf.transpose(tf.add( tf.matmul(l3, output_layer['weights']), output_layer['biases'] ))
    return output

def train_neural_network(x):

    model = neural_network_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(model, y) )
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    ephocs = 10

    with tf.Session() as sess :
        sess.run(tf.global_variables_initializer())
        for epoch in range(ephocs):
            epoch_cost = 0

            i = 0
            while i< len(titanic_train) :
                start = i
                end = i+batch_size
                batch_x = np.array( train_x[start:end] )
                batch_y = np.array( train_y[start:end] )

                _, c = sess.run( [optimizer, cost], feed_dict={x: batch_x, y: batch_y} )
                epoch_cost += c
                i+=batch_size
            print("Epoch",epoch+1,"completed with a cost of", epoch_cost)

def make_prediction(x, test_data):
    
    with tf.Session() as sess :
        sess.run(tf.global_variables_initializer())
        prediction = sess.run(y, feed_dict={x: test_data})
        return prediction


preprocess(titanic_train, [0, 2, 7, 9])
preprocess(titanic_test, [0, 2, 7, 9])

print(titanic_train)

train_x = np.array(titanic_train)[:,:7]
print(train_x)

train_y = np.array(titanic_train)[:,7]
print(train_y)

test_x = np.array( titanic_test )
print(test_x)

train_neural_network(x)

test_y = make_prediction(x ,test_x)

print(test_y)




