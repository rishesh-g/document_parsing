from beam import Image, endpoint, env
from prompts import system_prompt
from PIL import Image
import uuid
import base64
from io import BytesIO

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
        "type": "image",
        "image": f"data:image/jpeg;base64,{image}",
    }

    content_parts = []

    text_part = {"type": "text", "text": text}
    id_part = {"type": "text", "text": f"The UID for this voucher is {data_id}"}

    content_parts.append(image_part)
    content_parts.append(id_part)

    messages = [
        {
            "role": "system",
            "content": [text_part]
        },
        {
            "role": "user",
            "content": content_parts
        }
    ]

    return messages

img_path = 'docs/Instant-e-invoice-in-TallyPrime.jpg'
pil_image = Image.open(img_path)

image_b64 = convert_to_base64(pil_image)

inp_data = {
    "text": system_prompt,
    "image": image_b64,
    "thread_id": str(uuid.uuid4()),
}

input_message = prompt_func(inp_data)

import requests

url = "https://14d789ec-ebb3-4d3c-a247-83bdb483e470.app.beam.cloud"
headers = {
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Authorization": "Bearer TpEiqae56owfqWH1eM2UIVat28-WEmxR_CAWtl6hzmkCdfm6YfOymsCVxtIhlEAlwsSPJaEyYqyzvHVqjHjBMA=="
}
data = {"messages": input_message}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)



# if env.is_remote():
#     from transformers import AutoModelForCausalLM
#     import torch

# def download_models():
#     from transformers import AutoModelForImageTextToText,pipeline,AutoProcessor

#     print ("Downloading model...")
#     print ("-"*80)

#     processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
#     model = AutoModelForImageTextToText.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
#     hf_pipeline = pipeline(
#         "image-text-to-text",
#         model=model, 
#         device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
#         processor=processor
#     )

#     print ("Model downloaded successfully!")
#     print ("-"*80)

#     return hf_pipeline

# @endpoint(
#     name="inference-quickstart",
#     on_start=download_models,
#     gpu="A100-40",
#     image=Image(python_version="python3.10")
#     .add_python_packages(["transformers", "torch","torchvision", "huggingface_hub[hf-transfer]","langchain-huggingface","pillow","PIL"])
#     .with_envs("HF_HUB_ENABLE_HF_TRANSFER=1"),
# )
# def predict(context, prompt: str = "Hello, how are you?"):

    

#     # print ('Recieved prompt:', prompt)

#     # from langchain_huggingface.llms import HuggingFacePipeline

#     messages = input_message
#     pipeline = context.on_start_value

#     # hf = HuggingFacePipeline(pipeline=pipeline)

#     # Generate
#     result = pipeline(messages)
#     # result = hf.generate(messages)

#     print(result)

#     return {"prediction": result}