import json

with open('docs/purchase_invoice_glossary.json', 'r') as file:
    json_glossary = json.load(file)

with open('docs/purchase_invoice_lean.json', 'r') as file:
    reference_json = json.load(file)


system_prompt_template = """
You are an expert in information extraction from documents.
I will be providing invoices to you are task is to find out the following information from these invoices.
Please extract the following information from the invoice and return it in a JSON format:
{json_glossary}

You can find this example JSON for reference:
{reference_json}


This is a very critical piece of documentation and you can't afford to get the information wrong. The units of the items in the invoices
are also very important, these are small things that go unnoticed and cause a great deal of trouble.

Return the response in a JSON format such that it can be converted to pandas Dataframe. You don't need to show me any working or code.
I am just concerned with the JSON response and nothing else. I will be providing several invoices to you in different formats.
Again remember returning proper JSON format is REALLY IMPORTANT for my use case. I should be able to directly use your JSON output for further processing without needing to clean it.
"""

system_prompt = system_prompt_template.format(
    json_glossary=json_glossary,
    reference_json=reference_json, indent=2
)