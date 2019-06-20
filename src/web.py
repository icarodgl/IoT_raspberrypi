#!/usr/bin/env python3
from flask import Flask,jsonify
from flask_restful import Resource, Api
import os
from model import Dados

app = Flask(__name__)
api = Api(app)


class ping(Resource):
    def get(self):
        d = {"pong": "pong"}
        return jsonify(d)
    # end def

class temperatura (Resource):
    def get(self):
        query = Dados.select()
        temperaturas = [{"id": dados.rasp_id, "temperatura": dados.temp, "data": dados.data} for dados in query]
        return jsonify(temperaturas)
    # end def
class umidade (Resource):
    def get(self):
        query = Dados.select()
        umidades = [{"id": dados.rasp_id, "umidade": dados.umi, "data": dados.data} for dados in query]
        return jsonify(umidades)
#end def
class pressao(Resource):
    def get(self):
        query = Dados.select()
        pressao = [{"id": dados.rasp_id, "pressao": dados.pres, "data": dados.data} for dados in query]
        return jsonify(pressao)
#end def



#rotas
api.add_resource(ping, '/')
api.add_resource(temperatura, '/temperatura')
api.add_resource(umidade, '/umidade')
api.add_resource(pressao, '/pressao')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))