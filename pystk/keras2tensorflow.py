#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import necessary packages.
import argparse
import logging
import os
import os.path as osp
import warnings

from keras import backend as K
from keras.models import load_model
import tensorflow as tf
from tensorflow.python.framework import graph_io
from tensorflow.python.framework.graph_util import convert_variables_to_constants

from config import output_log

# Set necessary environment.
warnings.filterwarnings("ignore")
# Create logger for debugging.
output_log.init_log('./log/update_url')


def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    """  Freezes the state of a session into a pruned computation graph.

    Creates a new computation graph where variable nodes are replaced by
    constants taking their current value in the session. The new graph will be
    pruned so sub-graphs that are not necessary to compute the requested
    outputs are removed.

    :param session: The TensorFlow session to be frozen.
    :param keep_var_names: A list of variable names that should not be frozen,
                         or None to freeze all the variables in the graph.
    :param output_names: Names of the relevant graph outputs.
    :param clear_devices: Remove the device directives from the graph for better portability.

    :return: The frozen graph definition.
    """
    # Fetch graph of session.
    graph = session.graph

    # Set graph as default graph and freeze graph.
    with graph.as_default():
        # Filter variable names which should be frozen.
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        # Set output names.
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        # Set input graph.
        input_graph_def = graph.as_graph_def()
        # Clear devices if not None.
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""

        # Convert variables to constants and freeze the graph.
        frozen_graph = convert_variables_to_constants(session, input_graph_def,
                                                      output_names, freeze_var_names)

        return frozen_graph


def convert_model(input_file_path, target_fold, target_file_name):
    """Convert Keras .h5 model file into Tensorflow .pb model file.

    Freeze session and convert Keras model into Tensorflow model.

    :param input_file_path: The input file path of Keras model file, in .h5.
    :param target_fold: The target fold where the Tensorflow model file is saved in.
    :param target_file_name: The output file name of Tensorflow model file, in .pb.

    :return: None. The output file has been written in function.
    """
    # Load Keras model.
    K.set_learning_phase(0)
    net_model = load_model(input_file_path)
    # Record input and output nodes' names.
    logging.info('The input node name is : %s, and the output node name is : %s' %
                 (net_model.input.name, net_model.output.name))

    # Create session and freeze graph, then save frozen graph into model file.
    output_fold = target_fold + '/tensorflow_model/'
    frozen_graph = freeze_session(K.get_session(), output_names=[net_model.output.op.name])
    graph_io.write_graph(frozen_graph, output_fold, target_file_name, as_text=False)
    logging.info('Saved the constant graph (ready for inference) at %s' %
                 osp.join(output_fold, target_file_name))


def main():
    """The main function to convert Keras model into TensorFlow model.

    :return: Write the TensorFlow model into .pb file.
    """
    # Parse the argument and read into the date.
    # ------------------------------------------
    parser = argparse.ArgumentParser(description='This is script to convert Keras model file.')
    parser.add_argument('-p', required=True, help='The target product.')
    args = parser.parse_args()
    # path = args.p

    # Define related file path, as well as file name.
    input_fold = 'THE/PATH/TO/INPUT/FOLD'
    weight_file = 'XXX.h5'
    output_graph_name = 'XXX.pb'
    output_fold = input_fold + 'tensorflow_model/'
    # Combine path with file name.
    if not os.path.isdir(output_fold):
        os.mkdir(output_fold)
    weight_file_path = osp.join(input_fold, weight_file)

    # Load Keras model.
    K.set_learning_phase(0)
    net_model = load_model(weight_file_path)
    # Record input and output nodes' names.
    logging.info('The input node name is : %s, and the output node name is : %s' %
                 (net_model.input.name, net_model.output.name))

    # Create session and freeze graph, then save frozen graph into model file.
    frozen_graph = freeze_session(K.get_session(), output_names=[net_model.output.op.name])
    graph_io.write_graph(frozen_graph, output_fold, output_graph_name, as_text=False)
    logging.info('Saved the constant graph (ready for inference) at %s' %
                 osp.join(output_fold, output_graph_name))


if __name__ == '__main__':
    main()
