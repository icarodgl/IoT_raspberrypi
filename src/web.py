from flask import Flask,jsonify
from flask_restful import Resource, Api
import os
import json
from model import Dados

app = Flask(__name__)
api = Api(app)


class ping(Resource):
    def get(self):
        m = {"mensagem": "estou vivo!"}
        return m

class get_dados (Resource):
    def get(self):
        dados = Dados.select()
        print(dados)
        return jsonify(dados)

api.add_resource(ping, '/')
api.add_resource(get_dados, '/dados/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))