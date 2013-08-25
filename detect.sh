#!/bin/bash

line=$(head -n 1 "filelog.txt")
#store file name in variable
filename=`(echo $line | cut -d "'" -f 2)`
echo $filename

#move file
scp mmal/filename justin@10.0.1.39:/home/justin/Desktop

python3 mailalert.py
