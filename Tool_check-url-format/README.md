# Normal Url's Format Inspector
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

