#!/bin/bash

line=$(head -n 1 "../t.txt")
#store file name in variable
A=`(echo $line | cut -d "'" -f 2)`
echo $A

#move file
scp t.txt justin@10.0.1.39:/home/justin/Desktop

python mailalert.py
