import base64
from io import BytesIO
import requests
import ast
import xmltodict

from langchain_core.messages import HumanMessage


def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def prompt_func(data):
    text = data["text"]
    image = data["image"]
    data_id = data['thread_id']

    image_part = {
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{image}",
    }

    content_parts = []

    text_part = {"type": "text", "text": text}
    id_part = {"type": "text", "text": f"The UID for this voucher is {data_id}"}

    content_parts.append(image_part)
    content_parts.append(text_part)
    content_parts.append(id_part)

    return [HumanMessage(content=content_parts)]

def convert_json_to_xml(json_data):
    """
    Convert JSON data to XML format.

    :param json_data: JSON string or dictionary
    :return: XML string
    """

    inv_details = ast.literal_eval(json_data)
    inv_details['ENVELOPE']['BODY']['IMPORTDATA']['REQUESTDATA']['TALLYMESSAGE']['VOUCHER']['DATE'] = '20250401'

    xml_data = xmltodict.unparse(inv_details, pretty=True)

    return xml_data


def upload_to_acc(xml_data, url, headers):
    """
    Upload XML data to a accounting software.

    :param xml_data: XML string
    :param url: URL of the accounting software endpoint
    :param headers: Headers for the HTTP request
    :return: Response from the accounting software
    """

    response = requests.post(
        url,
        data=xml_data.encode('utf-8'),
        headers=headers
    )

    return response
