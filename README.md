# Learn Flask by Coding

Open-source project provided by AppSeed to help beginners accommodate faster with Flask. For newcomers, Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

> **For support and more [Free Samples](https://appseed.us/admin-dashboards/open-source) join [AppSeed](https://appseed.us).**

<br /> 

> 🚀 `PROMO`: **[Junior Developers Starter KIT](https://www.creative-tim.com/product/buy/bundle/junior-bundle?AFFILIATE=128200)** `85%OFF`

The package includes a `rock-solid collection of premium assets` (**Kits & Dashboards**) that can be used to build eye-catching portfolios and web apps in no time.

[![Junior Developers Starter KIT](https://user-images.githubusercontent.com/51854817/195055646-e55200cd-0ddd-4bdd-aded-0d4e4479789b.png)](https://www.creative-tim.com/product/buy/bundle/junior-bundle?AFFILIATE=128200)

<br /> 

## Getting Started with Flask

> Create a Virtual Environment

```bash
$ # Virtualenv modules installation (Unix-based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows-based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> Install `Flask`

```bash
$ pip install flask
```

<br />

> Edit your first Flask app `main.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
```

<br />

> Setup the environment

```bash
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=main.py
$ (Windows) set FLASK_APP=main.py
$ (Powershell) $env:FLASK_APP = ".\main.py" 
```

<br />

> Start the app

```bash
$ flask run
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

<br />

--- 
Learn Flask by Coding - Provided and actively supported by AppSeed [App Generator](https://appseed.us)
