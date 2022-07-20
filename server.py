from flask import Flask, json
from flask import request


api = Flask(__name__)

@api.route('/sentence', methods=['POST'])
def get_sentence():
    sentence = request.form.get('sentence')
    ret = [{"id": 1, "sinhala": str(sentence)}]
    return json.dumps(ret)

if __name__ == '__main__':
    api.run()
