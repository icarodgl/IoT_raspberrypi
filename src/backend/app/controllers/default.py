from flask import jsonify
from app import app

from app.models.dados import Dados


@app.route("/")
def index():
    d = {"pong": "pong"}
    return jsonify(d)
#end def

@app.route("/temperatura", methods=['GET'])
def temperatura():
    query = Dados.select()
    temperaturas = [{"id": dados.rasp_id, "temperatura": dados.temp, "data": dados.data} for dados in query]
    return jsonify(temperaturas)
#end def

@app.route("/umidade", methods=['GET'])
def umidade():
    query = Dados.select()
    umidades = [{"id": dados.rasp_id, "umidade": dados.umi, "data": dados.data} for dados in query]
    return jsonify(umidades)
#end def

@app.route("/pressao", methods=['GET'])
def pressao():
    query = Dados.select()
    pressao = [{"id": dados.rasp_id, "pressao": dados.pres, "data": dados.data} for dados in query]
    return jsonify(pressao)
#end def