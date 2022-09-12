import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/returnjson', methods=['GET'])
def ReturnJSON():
    if (request.method == 'GET'):
        # r = requests.get('https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty')
        #     data = r.text
        r = requests.get('https://api-shipx-pl.easypack24.net/v1/organizations/34060',headers={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJhcGktc2hpcHgtcGwuZWFzeXBhY2syNC5uZXQiLCJzdWIiOiJhcGktc2hpcHgtcGwuZWFzeXBhY2syNC5uZXQiLCJleHAiOjE2NDAyNTQ4NTgsImlhdCI6MTY0MDI1NDg1OCwianRpIjoiYTMzMmFmMmYtODYzMC00MWZhLTkwNzUtMmFmYmI5ODM4ZTZiIn0.DIOY9TkcWcjHs64t7kIAHyBn-Evz3oD6zewAxzvACbuj_g64rwVUbb1-6Alxr_8YjDyPRbzxwVV-jlk4x9pU6A'})
        data = r.text
        return data

if __name__ == '__main__':
    app.run(debug=True)
