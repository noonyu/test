#coding:utf-8
#两层简单神经网络（全连接）
import tensorflow as tf

#定义输入和参数
#用placeholder定义输入 (sess.run喂多组数据）
x = tf.placeholder(tf.float32,shape=(1, 2))
#x = tf.constant([[0.7,0.5]])
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

#定义输入和参数
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

#用会话计算结果
with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print "y in tf3_4.py is:\n",sess.run(y,feed_dict={x: [[0.7,0.5]]})
	print "w1:\n",sess.run(w1)
	print "w2:\n",sess.run(w2)
