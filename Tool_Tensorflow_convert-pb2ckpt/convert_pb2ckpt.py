import tensorflow as tf

pb_file_path = 'THE/PATH/TO/PBFILE'
ckpt_file_path = 'THE/PATH/TO/CKPTFILE'

with tf.Graph().as_default():
    output_graph_def = tf.GraphDef()
    print('starting importing model.')
    with open(pb_file_path, "rb") as f:

        output_graph_def.ParseFromString(f.read())
        tensors = tf.import_graph_def(output_graph_def, name="test")
        print('--------')
        print tensors
    print('create saver')
    saver = tf.train.Saver()

    with tf.Session() as sess:
        print('initialize variable')
        init = tf.global_variables_initializer()
        sess.run(init)
        op = sess.graph.get_operations()
        print('start operate.')
        for m in op:
            print(m.values())
        saver.save(sess, ckpt_file_path)
