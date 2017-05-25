from flask import Flask, render_template, request
import unirest
app = Flask(__name__)
MASHAPE_KEY = "YOUR KEY HERE"


response = unirest.post("https://community-sentiment.p.mashape.com/text/",
  headers={
    "X-Mashape-Key": MASHAPE_KEY,
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "txt": "Today is  a good day"
  }
)
print(response.body)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
