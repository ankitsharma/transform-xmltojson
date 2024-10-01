from flask import Flask, request, jsonify
import xmltodict, json
import xml.etree.ElementTree as ET
from lxml import etree
import logging

app = Flask(__name__)
logger = logging.getLogger()

# The same Lambda function logic, but adapted to work with Flask
@app.route('/transform', methods=['POST'])
def lambda_handler():
    try:
        # Extract the XML content from the incoming request body
        xml_body = request.data.decode('utf-8')
        
        if not xml_body:
            return json.dumps({"error": "No XML body provided"}), 400
        #dom = xml.etree.fromstring(xml_body)
        dom = etree.fromstring(xml_body)
        xsl = etree.parse('transform.xsl')
        transform = etree.XSLT(xsl)
        output_xml = str(transform(dom))
        cleaned_xml = output_xml.replace('\n','')
        # Convert extracted data to JSON
        cleaned_json = xmltodict.parse(cleaned_xml)
        json_data = json.dumps(cleaned_json)
        
    #    return jsonify(cleaned_json), 200
        return (json_data), 200

    except Exception as e:
        # General error handling for unforeseen issues
        return json.dumps({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
