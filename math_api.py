import mathOnTwoNumbers
from flask import Flask, request
from flask_restful import Resource, Api

#initialize flask instance
app = Flask(__name__)
#Initialize API? Need info on this
api = Api(app)

class mathNumbers(Resource):
    def get(self, ops, first_number, second_number):
        return {'data' : mathOnTwoNumbers.mathOfTwo(ops, first_number, second_number)}

api.add_resource(mathNumbers, '/mathOnTwoNumbers/<ops>/<first_number>/<second_number>')

if __name__ == '__main__':
    app.run()