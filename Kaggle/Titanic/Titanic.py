import pandas
import numpy as np
import tensorflow as tf

titanic_train = pandas.read_csv("Kaggle/Titanic/train.csv")
titanic_test = pandas.read_csv("Kaggle/Titanic/test.csv")

ip_features = 7
op_classes = 2
batch_size = 32

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

    nodes = [25]
    
    
    hidden1_layer = { 'weights' : tf.Variable( tf.random_normal([ip_features, nodes[0]]) ),
                       'biases' : tf.Variable( tf.random_normal([nodes[0]]) )
                    }

    output_layer = { 'weights' : tf.Variable( tf.random_normal([nodes[0], op_classes]) ),
                       'biases' : tf.Variable( tf.random_normal([op_classes]) )
                    }

    l1 = tf.add( tf.matmul(data, hidden1_layer['weights']), hidden1_layer['biases'] )
    l1 = tf.nn.relu(l1);

    output = tf.add( tf.matmul(l1, output_layer['weights']), output_layer['biases'] )
    return output

def train_neural_network_and_make_prediction():

    prediction = neural_network_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction, y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    ephocs = 1000

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

        pred_y=tf.arg_max(tf.nn.softmax(prediction), 1)
        predictions = pred_y.eval(feed_dict={x:test_x})
    return predictions

preprocess(titanic_train, [0, 2, 7, 9])
preprocess(titanic_test, [0, 2, 7, 9])

train_x = np.array(titanic_train)[:,:7]

temp_y = np.array(titanic_train)[:,7]
train_y = []
for e in temp_y:
    if e==0:
        train_y.append([1, 0])
    else:
        train_y.append([0, 1])

test_x = np.array( titanic_test )

test_y = train_neural_network_and_make_prediction()

print(test_y)

titanic_test = pandas.read_csv("Kaggle/Titanic/test.csv")

submission = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": test_y
    })

submission.to_csv("Kaggle/Titanic/result.csv", index=False)




