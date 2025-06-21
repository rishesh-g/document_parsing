"""
Document Parsing and CRM Integration Script
This script processes an image, extracts information using a language model, converts the response to XML, and uploads it to a CRM system.
It uses various utility functions for image processing, JSON to XML conversion, and HTTP requests.
It also includes configuration settings for the model and server connection.
It is designed to handle invoice data extraction and integration with a CRM system.
It is a complete workflow for document parsing and data integration.

"""
from PIL import Image
from utils import convert_to_base64, convert_json_to_xml, upload_to_crm
from get_llm_response import get_response
import config
from prompts import system_prompt
import uuid

def extract_and_upload(uploaded_file):
    """
    Main function to process the image and upload the response to CRM.
    """
    # Load the image and convert it to Base64
    pil_image = Image.open(uploaded_file)
    image_b64 = convert_to_base64(pil_image)

    # Get the response from the LLM
    json_response = get_response(
        text=system_prompt,
        image=image_b64,
        thread_id=str(uuid.uuid4()),   
    )

    # Convert JSON response to XML format
    xml_response = convert_json_to_xml(json_response)

    # Define CRM URL
    crm_url = f'http://{config.HOST}:{config.PORT}'

    # Upload XML data to CRM
    crm_response = upload_to_crm(
        xml_data=xml_response,
        url=crm_url,
        headers={'Content-Type': 'application/xml'}
    )

    return crm_response.text
    
if __name__ == "__main__":

    file_path = 'docs/Instant-e-invoice-in-TallyPrime.jpg'
    status = extract_and_upload(file_path)
    print("CRM Response:", status)

