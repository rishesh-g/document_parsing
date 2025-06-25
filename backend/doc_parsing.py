"""
Document Parsing and accounting software Integration Script
This script processes an image, extracts information using a language model, converts the response to XML, and uploads it to an accounting software.
It uses various utility functions for image processing, JSON to XML conversion, and HTTP requests.
It also includes configuration settings for the model and server connection.
It is designed to handle invoice data extraction and integration with a accounting software.
It is a complete workflow for document parsing and data integration.

"""
from PIL import Image
from utils import convert_to_base64, convert_json_to_xml, upload_to_acc
from get_llm_response import get_response
import config
from prompts import system_prompt
import uuid


def extract_and_upload(uploaded_file):
    """
    Main function to process the image and upload the response to accounting software.
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

    # Define accounting software URL
    acc_url = f'http://{config.ACC_HOST}:{config.ACC_PORT}'

    # Upload XML data to accounting software
    acc_response = upload_to_acc(
        xml_data=xml_response,
        url=acc_url,
        headers={'Content-Type': 'application/xml'}
    )

    return acc_response.text
    
if __name__ == "__main__":

    file_path = 'docs/Instant-e-invoice-in-TallyPrime.jpg'
    status = extract_and_upload(file_path)
    print("Accounting Software Response:", status)

