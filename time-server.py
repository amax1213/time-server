import requests
import os
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

response = requests.get("https://www.epochconverter.com/")

etime = {}
soup = BeautifulSoup(response.content, "html.parser")
etime = soup.find_all("div", class_="ecclock")

print(etime[0].getText())


@app.route("/")
def get_epoch_time(): #home
    print(etime[0].getText())
    return str(etime[0].getText())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6783))
    app.run(host="0.0.0.0", port=port)