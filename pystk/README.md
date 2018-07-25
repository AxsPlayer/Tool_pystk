# Keras2tensorflow

## Motivation.
In some situation, you would use Keras to train the model, but in engineer environment, what would be used is Java Based Tensorflow. Therefore, the Keras model should be converted into Tensorflow model. This project aims to convert Keras model file into Tensorflow model file.

## Usage.
Modify the input file path and output file path in the script, according to your specific situation.

Then, run the script, with following script:

	python keras2tensorflow.py


# Check url format
Normal Url's Format Inspector

This Tool is designed to inspect the format of url whether it's normal or not using Regular Expression.

## Why this tool?
In some situation, you need to filter out or crawl URLs which are in normal format. In other word, you don't want any abnormal urls to disturb your tasks. Then it's the tool for you to filter out what you really need.

## How to use this tool?
What the tool need as input are just input file path as well as output file path.
As an instance, 

    Python check_url_format.py -i THE/PATH/TO/YOUR/INPUT/FILE -o THE/PATH/TO/YOUR/OUTPUT/FILE

The content of input file should be one url you wanna check in one line. For example, 
> https://github.com/AxsPlayer/Tool_toolkit/edit/master/Tool_check-url-format/README.md

And the content of output file is url with corresponding tag in one line. The tag is 'Normal' for normal format and 'Error' for abnormal format. And the delimiter is '\t'. For example, 
> https://github.com/AxsPlayer/Tool_toolkit/edit/master/Tool_check-url-format/README.md \t Normal.


# Convert pb2ckpt.

## Motivation.
In some situation, you have trained the Tensorflow model and save model file in .pb format. However, in other situations, the necessary model file format is .ckpt. Thus, this project is designed to help you convert .pb model file into .ckpt model file.

## Usage.
Modify the pb_file_path and ckpt_file_path in the script.

Then, run the following script to start converting.

	python convert_pb2ckpt.py 


# Python code performance.

## Target/Motivation?
In Python scripts, ususally some lines of code cost most of running time, and what you want to do with code performance is to find the most time-consuming part of code and to optimize the performance.
The target of this tool is to help you find the 'evil'.

## How to use.
Firstly, install the necessary packages.

	pip install line_profiler

Secondly, add decorator **@profile** before the target function.

Thirdly, run the following command to get performance results.

	kernprof -l -v timing_functions.py

The result looks like as following:

![result](https://github.com/AxsPlayer/Tool_toolkit/tree/master/Tool_Python-code-performance/images/kernprof_line_profiler.png)


# Convert ip to number.
# Aims of this project.
Convert ip address into 32-bit integer.

# Usage Method.
First, write ip address into file named 'ip.txt'. One ip address in one line.
Secondly, run the script:
	
	python convert_ip2num.py -f ip.txt
	
Then, you will find results file in 'result/ip_num_result.txt', in format of 'ip address: number' in each line.

# Unit Test.
There are four test cases in script, each to test one kind of situation. Two are correct cases and two are wrong cases.
The usage method of unit test script is:
	
	python -m unittest converter_test

