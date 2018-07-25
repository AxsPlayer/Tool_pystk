# pystk
Small tools in toolkit to deal with piece of cakes in daily life, such as small tool to check normal url format.
'pystk' represents for Python Small Toolkit.
<br>
<br>

## Motivation?
In daily work, there are always bunch of need for small tools to deal with tiny problems. You can search using Google and write scripts for them. However, it's also time-consuming after multiple times for one small task, for the reason you should create tools again and again. Then the toolkit is designed to alleviate this problem.

## What's the content?
### Keras2tensorflow
***
#### Motivation.
In some situation, you would use Keras to train the model, but in engineer environment, what would be used is Java Based Tensorflow. Therefore, the Keras model should be converted into Tensorflow model. This project aims to convert Keras model file into Tensorflow model file.
#### Usage.
Import and use function in Python script as followings:

	from pystk.keras2tensorflow import convert_model
	convert_model(input_file_path, target_fold, target_file_name)

- ***Parameters***
	- input_file_path: The input file path of Keras model file, in .h5.
	- target_fold: The target fold where the Tensorflow model file is saved in.
	- target_file_name: The output file name of Tensorflow model file, in .pb.
- ***Output***
The output Tensorflow model file will be saved in target_fold/tensorflow_model/.
<br>

### Convert pb2ckpt.
***
#### Motivation.
In some situation, you have trained the Tensorflow model and save model file in .pb format. However, in other situations, the necessary model file format is .ckpt. Thus, this project is designed to help you convert .pb model file into .ckpt model file.

#### Usage.
Import and use function in Python script as followings:

	from pystk.convert_pb2ckpt import convert_model
	convert_model(pb_file_path, ckpt_file_path)

- ***Parameters***
	- pb_file_path: The file path of .pb model.
	- ckpt_file_path: The file path of .ckpt model.
- ***Output***
The output Tensorflow model file will be saved in ckpt_file_path.
<br>


### Check url format
***
Normal Url's Format Inspector. This Tool is designed to inspect the format of url whether it's normal or not using Regular Expression.

#### Motivation.
In some situation, you need to filter out or crawl URLs which are in normal format. In other word, you don't want any abnormal urls to disturb your tasks. Then it's the tool for you to filter out what you really need.

#### Usage.
Import and use function in Python script as followings:

	from pystk.check_url_format import check_url_format
	check_url_format(url)

- ***Parameters***
	- url: The url which is tended to be checked.
- ***Output***
The string result.
	- 'Normal' for normal url format.
	- 'Error' for abnormal url format.
<br>


### Convert ip to number.
#### Aims of this project.
Convert ip address into 32-bit integer.
#### Usage.
Import and use function in Python script as followings:

	from pystk.convert_ip2num import convert_to_num
	convert_to_num(ip_address)

- ***Parameters***
	- ip_address: The ip address, eg. 127.125.5.1.
- ***Output***
The 32-bit number converted from ip address.
<br>


### Python code performance.
#### Target/Motivation?
In Python scripts, ususally some lines of code cost most of running time, and what you want to do with code performance is to find the most time-consuming part of code and to optimize the performance.
The target of this tool is to help you find the 'evil'.
#### How to use.
Firstly, install the necessary packages.

	pip install line_profiler

Secondly, add decorator **@profile** before the target function.

Thirdly, run the following command to get performance results.

	kernprof -l -v timing_functions.py

The result looks like as following:

![result](https://github.com/AxsPlayer/Tool_toolkit/tree/master/Tool_Python-code-performance/images/kernprof_line_profiler.png)





