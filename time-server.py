from flask.wrappers import Response
import requests
import os
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

response = requests.get("https://www.epochconverter.com/")
etime = {}
soup = BeautifulSoup(response.content, "html.parser")
etime = soup.find_all("div", class_="ecclock")

@app.route('/')
def get_time():
    return str(etime[0].getText())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host="127.0.0.1", port=port)