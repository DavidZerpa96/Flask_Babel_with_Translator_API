import requests
import polib
import json
import os

# Function to translate text using Azure Translator
def translate_text(text, to_language="en"):
    # Credentials and configuration
    subscription_key = os.getenv("subscription_key")
    endpoint = os.getenv("endpoint")
    location = os.getenv("location")

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': to_language
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json'
    }

    # If the text is empty or only has spaces, we return empty without calling the API
    if not text.strip():
        return ""

    body = [{
        'text': text
    }]

    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    response.raise_for_status()
    result = response.json()
    translated_text = result[0]['translations'][0]['text']
    return translated_text

# Translate Spanish `msgid` -> English `msgstr` for the English locale file.
input_po_path = "translations/en/LC_MESSAGES/messages.po"
po = polib.pofile(input_po_path)

# Translate each entry and assign the msgstr
for entry in po:
    # entry.msgid is the original text, entry.msgstr is the translation
    if entry.msgid.strip():  # if msgid is not empty
        # Translate
        translated = translate_text(entry.msgid, to_language="en")
        entry.msgstr = translated
    else:
        # if it is empty, we leave it as is
        entry.msgstr = ""

# Save the translated file (in-place).
output_po_path = input_po_path
po.save(output_po_path)

print(f"Translation completed. File saved in {output_po_path}")
