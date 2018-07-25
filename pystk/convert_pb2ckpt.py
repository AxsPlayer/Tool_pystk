#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import necessary packages.
import tensorflow as tf


def convert_model(pb_file_path, ckpt_file_path):
    """Convert .pb model file into .ckpt model file.

    In Tensorflow, there are several kinds of model files. One mission
    is to convert .pb model file into .ckpt model file.

    :param pb_file_path: The file path of .pb model.
    :param ckpt_file_path: The file path of .ckpt model.

    :return: None. The result model file is saved in function.
    """
    # Create graph in Tensorflow and start converting.
    with tf.Graph().as_default():
        output_graph_def = tf.GraphDef()
        # Start importing model.
        with open(pb_file_path, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            # tensors = tf.import_graph_def(output_graph_def, name="test")
        saver = tf.train.Saver()
        # Create Tensorflow's session.
        with tf.Session() as sess:
            # Initialize variable.
            init = tf.global_variables_initializer()
            sess.run(init)
            op = sess.graph.get_operations()
            # Print operation.
            for m in op:
                print(m.values())
            # Save model into .ckpt file.
            saver.save(sess, ckpt_file_path)
