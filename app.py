from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess as sp

app = Flask(__name__)
CORS(app)

@app.route('/home')
def hello():
    return jsonify({'message': 'Welcome to Innov-AI-te'})

@app.route('/data',methods=['GET'])
def upload_data():
    datapath = request.args.get('file_path')
    # os.system(hadoop fs -put )

@app.route('/model',methods=['GET'])
def runML():
    type_name = request.args.get('type_name')
    dataset_name = request.args.get('dataset_name')
    if(type_name and dataset_name):
        cat = sp.run(["python3", "mlproc.py",f"{type_name}",f"{dataset_name}"])
        if(cat.returncode == 0):
            return jsonify({'message': "Model Trained"})
        else:
            return jsonify({'message': 'Build Failed!!!'})
    else:
        return jsonify({'message': 'Build Failed!!!'})
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
