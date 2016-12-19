import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

#res = x1*x2
res = tf.mul(x1, x2)

print(res)

with tf.Session() as sess:
    print(sess.run(res))
