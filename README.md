# transform-xmltojson

Transform the XML request payload to JSON using python and expose the RestAPI using flask.
 and publish the transformed JSON to SQS


Note: Use user_data-Script.sh while creating EC2 instance or template it will setup all the script, Libraries. but before this please update the following Values with your own queue details.:


export SQS_QUEUE_REGION=**<REGION_NAME>**
export SQS_QUEUE_ACCESS_ID=**<ACCESS_ID>**
export SQS_QUEUE_SECRET_ID=**<SECRET_ID>**
export SQS_QUEUE_URL=**<QUEUE_URL>**
