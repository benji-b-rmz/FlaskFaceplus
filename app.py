from flask import Flask, render_template, request
import json
import unirest

app = Flask(__name__)

MASHAPE_KEY = "YOUR MASHAPE KEY"

def faceplus(input_url):
    try:
        print (input_url)
        face_response = unirest.get(
            "https://faceplusplus-faceplusplus.p.mashape.com/detection/detect?attribute=glass%2Cpose%2Cgender%2Cage%2Crace%2Csmiling&url" + input_url,
            headers={
                "X-Mashape-Key": MASHAPE_KEY,
                "Accept": "application/json"
            }
            )
        print(face_response.body)
        face_response.body['success'] = 'true'
        json_response = json.dumps(face_response.body)
        return json_response
    except:
        print("unirest failed")
        response = {}
        response['success'] = 'false'
        json_response = json.dumps(response)
        return json_response

@app.route('/api/faceplus', methods = ['POST'])
def face_api():
    input_url = request.data.decode(encoding='UTF-8')
    return faceplus(input_url)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
