# Target/Motivation?
In Python scripts, ususally some lines of code cost most of running time, and what you want to do with code performance is to find the most time-consuming part of code and to optimize the performance.
The target of this tool is to help you find the 'evil'.

## How to use.
Firstly, install the necessary packages.

	pip install line_profiler

Secondly, add decorator **@profile** before the target function.

Thirdly, run the following command to get performance results.

	kernprof -l -v timing_functions.py


The result looks like as following:
![image](https://github.com/AxsPlayer/Tool_toolkit/tree/master/Tool_Python-code-performance/images/kernprof_line_profiler.png)
