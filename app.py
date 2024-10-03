from flask import Flask, request, jsonify
import xmltodict, json
import xml.etree.ElementTree as ET
from lxml import etree
import logging
import boto3

app = Flask(__name__)

logger = logging.getLogger()

# Initialize the SQS client

sqs = boto3.client('sqs', region_name='<QUEUE_REGION_NAME>', 
                   aws_access_key_id='<ACCESS_KYE>',
                   aws_secret_access_key='<SECRET_ACCESS_KEY>')

# Replace 'your-queue-url' with the actual URL of your SQS queue
SQS_QUEUE_URL = '<YOUR_QUEUE_URL>'

# The same Lambda function logic, but adapted to work with Flask
@app.route('/transform', methods=['POST'])
def lambda_handler():
    try:
        # Extract the XML content from the incoming request body
        xml_body = request.data.decode('utf-8')
        
        if not xml_body:
            return json.dumps({"error": "No XML body provided"}), 400
        dom = etree.fromstring(xml_body)
        xsl = etree.parse('transform.xsl')
        transform = etree.XSLT(xsl)
        output_xml = str(transform(dom))
        cleaned_xml = output_xml.replace('\n','')
        # Convert extracted data to JSON
        cleaned_json = xmltodict.parse(cleaned_xml)
        json_data = json.dumps(cleaned_json)
        
    #    return jsonify(cleaned_json), 200
    #    return (json_data), 200

    # Publish the message to SQS
        try:
            response = sqs.send_message(
                QueueUrl=SQS_QUEUE_URL,
               MessageBody=json_data
            )
           # Log success for monitoring
            print(f"Message sent to SQS: {response['MessageId']}")
        except Exception as e:
            raise RuntimeError(f"Failed to send message to SQS: {str(e)}")

        # Return a success response
        return {
                'message': 'Data successfully processed and sent to SQS',
                'sqs_message_id': response['MessageId']
        }

    except Exception as e:
        # General error handling for unforeseen issues
        return json.dumps({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
