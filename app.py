from flask import Flask, render_template, request
import json
import unirest

app = Flask(__name__)

MASHAPE_KEY = "YOUR MASHAPE KEY HERE"

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
        if face_response.body['url'] != None:
            face_response.body['message'] = "success"
            return json.dumps(face_response.body)
        face_response.body['message'] = 'failed'
        return json.dumps(face_response.body)

    except:
        print("unirest failed")
        response = {'message': 'failed'}
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
    app.run(debug=True)
