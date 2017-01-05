import pandas
import numpy as np
import tensorflow as tf



#Fill up empty cells
def cleanUpData(file):
    file["Age"] = file["Age"].fillna(file["Age"].median())
    file["Embarked"] = file["Embarked"].fillna("S")

# Convert text data into numericals
def preprocess(file): 
    cleanUpData(file)

    file.loc[file["Sex"] == "male", "Sex"] = 0
    file.loc[file["Sex"] == "female", "Sex"] = 1

    file.loc[file["Embarked"] == "S", "Embarked"] = 0
    file.loc[file["Embarked"] == "C", "Embarked"] = 1
    file.loc[file["Embarked"] == "Q", "Embarked"] = 2

    return file

#Neural Network Model
def neural_network_model():

    nodes = [25, 25]
    weights = {
        'hidden1' : tf.Variable( tf.random_normal([ip_features, nodes[0]]) ),
        'hidden2' : tf.Variable( tf.random_normal([nodes[0], nodes[1]]) ),
        'out' : tf.Variable( tf.random_normal([nodes[1], op_classes]) )
    }

    biases = {
        'hidden1' : tf.Variable( tf.random_normal([ nodes[0]]) ),
        'hidden2' : tf.Variable( tf.random_normal([nodes[1]]) ),
        'out' : tf.Variable( tf.random_normal([op_classes]) )
    }

    hidden1 = tf.add( tf.matmul(input_placeholder, weights['hidden1']), biases['hidden1'] )
    hidden1 = tf.nn.sigmoid(hidden1)

    hidden2 = tf.add( tf.matmul(hidden1, weights['hidden2']), biases['hidden2'] )
    hidden2 = tf.nn.sigmoid(hidden2)

    output = tf.add( tf.matmul(hidden2, weights['out']), biases['out'] )
    output = tf.nn.softmax(output)
    return output

#Train and Predict
def train_and_predict():
    
    output_prediction = neural_network_model()
    loss = tf.reduce_sum(tf.square(output_prediction - output_placeholder))
    trainer = tf.train.AdamOptimizer()
    optimizer = trainer.minimize(loss)
    test_prediction = tf.arg_max(output_prediction, 1)

    ephocs = 2000

    with tf.Session() as sess :
        sess.run(tf.global_variables_initializer())

        for epoch in range(ephocs):
            epoch_cost = 0;
            i = 0
            while i<len(train_x):
                start = i
                end = i+batch_size
                batch_x = np.array( train_x[start:end] )
                batch_y = np.array( train_y[start:end])

                _, c = sess.run([optimizer, loss], feed_dict={input_placeholder: batch_x, output_placeholder: batch_y} )
                epoch_cost += c*batch_size
                i+=batch_size
            print("Epoch",epoch+1,"completed with a cost of", epoch_cost)


        predictions = test_prediction.eval( feed_dict={input_placeholder: test_x} )
    return predictions



titanic_train = preprocess(pandas.read_csv("Kaggle/Titanic/train.csv"))
titanic_test = preprocess(pandas.read_csv("Kaggle/Titanic/test.csv"))

features = ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch']
ip_features = len(features)
op_classes = 2
batch_size = 128

input_placeholder = tf.placeholder('float', [None, ip_features])
output_placeholder = tf.placeholder('float')

train_x = titanic_train[features]
train_y = titanic_train['Survived']
train_y = np.eye(np.max(train_y) + 1)[train_y]   # Conver to 1 hot Array

test_x = titanic_test[features]
test_y = train_and_predict()


titanic_test = pandas.read_csv("Kaggle/Titanic/test.csv")

submission = pandas.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": test_y
    })

submission.to_csv("Kaggle/Titanic/result.csv", index=False)




