from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'python_CRUD'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/python_CRUD'

mongo = PyMongo(app)

@app.route('/framework', methods=['GET'])
def getAllFrameworks():
    framework = mongo.db.framework

    output = []

    #query the framework to get all documents
    for q in framework.find():
        output.append({'name' : q['name'], 'language': q['language']})

    return jsonify({'result' : output})

@app.route('/framework/<name>', methods=['GET'])
def getOneFramework(name):
    framework = mongo.db.framework

    q = framework.find_one({'name' : name})    

    if q:
        output = {'name' : q['name'], 'language': q['language']}

    else:
        output = 'None found' 

    return jsonify({'result' : output})

@app.route('/framework', methods=['POST'])
def addFramework():
    framework = mongo.db.framework
    
    name = request.json['name']
    language = request.json['language']

    framework_id = framework.insert_one({'name' : name, 'language' : language}) #TODO: figure out why this line fails
    new_framework = framework.find_one({'_id' : framework_id})

    output = {'name' : new_framework['name'], 'language' : new_framework['language']}

    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)