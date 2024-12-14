# Adding Multilingual Support to Your Flask Project 🌐

This guide explains how to integrate **Flask-Babel** for multilingual support in a Flask application and automate translations using the **Microsoft Translator API**. 

With this approach, you can dynamically translate your Flask application's content into multiple languages and streamline the translation process.

---

## Features

- Easily mark text for translation in your Flask application.
- Automatically generate `.pot` and `.po` translation files using Flask-Babel.
- Translate `.po` files automatically using Microsoft Translator API.
- Secure handling of sensitive data using environment variables.

---

## Step-by-Step Guide

### **1. Install Required Libraries**

Ensure you have Flask and other necessary libraries installed. Run the following command:

```
pip install flask flask-babel requests polib python-dotenv
```

---

### **2. Configure Flask-Babel in Your Flask Project**

1. Import Flask-Babel in your Flask application:

```
from flask_babel import Babel
```

2. Initialize Flask-Babel in your `app.py`:

```
from flask import Flask, request

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.args.get('lang', 'en')  # Default language is English
```

3. Update your HTML templates:

Mark text for translation by wrapping it with `_()`. For example:

```
<h1>{{ _('Welcome to my website!') }}</h1>
<p>{{ _('Explore projects, resume, and contact information.') }}</p>
```

---

### **3. Create a Babel Configuration File**

Create a file named `babel.cfg` in the root of your project with the following content:

```
[python: **.py]
[jinja2: templates/**.html]
```

This tells Flask-Babel to look for translatable strings in Python and HTML files.

---

### **4. Extract Translatable Strings**

Run the following command to extract all strings marked for translation into a `.pot` file:

```
pybabel extract -F babel.cfg -o messages.pot .
```

This creates a `messages.pot` file with all the translatable strings in your project.

---

### **5. Initialize Language Files**

For each language you want to support, run the following command to create a `.po` file:

```
pybabel init -i messages.pot -d translations -l es
pybabel init -i messages.pot -d translations -l en
```

This creates `.po` files in the `translations` directory for Spanish (`es`) and English (`en`).

---

### **6. Automate Translation with Microsoft Translator API**

Use the provided script `translate_po.py` to automate translations for `.po` files.

1. Store your API credentials in a `.env` file:
   - Create a `.env` file in the root of your project with the following content:

```
TRANSLATOR_API_KEY=your_api_key
TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com
TRANSLATOR_REGION=your_region
```

2. Ensure the `.env` file is excluded from Git by adding it to `.gitignore`:

```
.env
```

3. Use the script `translate_po.py` to translate `.po` files:

```
import os
import requests
import polib
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TRANSLATOR_API_KEY")
ENDPOINT = os.getenv("TRANSLATOR_ENDPOINT")
LOCATION = os.getenv("TRANSLATOR_REGION")

def translate_text(text, to_language="es"):
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Ocp-Apim-Subscription-Region": LOCATION,
        "Content-Type": "application/json",
    }
    body = [{"text": text}]
    params = {"api-version": "3.0", "to": to_language}
    response = requests.post(f"{ENDPOINT}/translate", headers=headers, params=params, json=body)
    response.raise_for_status()
    return response.json()[0]["translations"][0]["text"]

input_po = "translations/es/LC_MESSAGES/messages.po"
po = polib.pofile(input_po)
for entry in po:
    if entry.msgid.strip() and not entry.translated():
        entry.msgstr = translate_text(entry.msgid)
po.save(input_po)
print(f"Translation completed: {input_po}")
```

Run this script with:

```
python translate_po.py
```

---

### **7. Compile Translations**

Once the `.po` files are translated, compile them into `.mo` files with the following command:

```
pybabel compile -d translations
```

---

### **8. Test Your Application**

Start the Flask development server and test the multilingual functionality:

```
flask run
```

Visit the site in your browser, adding `?lang=es` or `?lang=en` to the URL to test different languages.

---

## Folder Structure

Here’s an example folder structure for your project:

```
ProjectRoot/
│
├── app.py               # Main Flask application
├── babel.cfg            # Flask-Babel configuration file
├── templates/           # HTML templates for the project
├── translations/        # Folder containing .po and .mo files
├── translate_po.py      # Script for automating translations
├── .env                 # Environment variables (not included in Git)
├── .gitignore           # Excludes sensitive files from version control
└── requirements.txt     # Python dependencies
```

---

## Security Tips

- Always store sensitive data, like API keys, in environment variables.
- Never commit your `.env` file to version control.
- Regularly rotate your API keys to enhance security.

---

## License

This guide and script are licensed under the MIT License. Feel free to use, modify, and share!

---

This README provides a comprehensive overview for implementing Flask-Babel and automating translations in a Flask project. Let me know if there’s anything else you’d like to include! 😊
