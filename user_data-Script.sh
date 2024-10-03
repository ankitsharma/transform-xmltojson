#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y

yum install git -y
cd /home/ec2-user

git clone https://github.com/ankitsharma/transform-xmltojson.git

cd transform-xmltojson
yum install python -y
yum install pip -y
pip install flask xmltodict lxml boto3



export SQS_QUEUE_REGION=<REGION_NAME>
export SQS_QUEUE_ACCESS_ID=<ACCESS_ID>
export SQS_QUEUE_SECRET_ID=<SECRET_ID>
export SQS_QUEUE_URL=<QUEUE_URL>

python app.py > app.out.log 2> app.err.log < /dev/null &
