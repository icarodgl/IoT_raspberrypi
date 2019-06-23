#!/usr/bin/env python3
import pika
import json
from model import Dados
import os
from dotenv import load_dotenv
load_dotenv()

parameters = pika.URLParameters(os.getenv('URL_MQ'))
connection = pika.BlockingConnection(
    parameters)
channel = connection.channel()

channel.queue_declare(queue='info_data')

def validador(mensagem):
    try:
        if mensagem["temp"] > 0 and mensagem["temp"] < 50 and mensagem["pres"] > 0 and mensagem["pres"] < 1.5 and mensagem["umi"] > 20 and mensagem["umi"] < 100:
            return 1
    except:
        print("mensagem muito errada!")
    return 0

def callback(ch, method, properties, body):
    mensagem = json.loads(body)

    if validador(mensagem):
        try:

            Dados.create(
                        rasp_id = mensagem["id"],
                        temp = mensagem["temp"],
                        umi = mensagem["umi"],
                        pres = mensagem["pres"],
                        data = mensagem["date"],
                        )
            print("Salvo: %r" % mensagem)
        except Exception as e:
            print("erro ao salvar: %s" % e)
    else:
        print("A mensagem não passou pela teste de validação")


channel.basic_consume(
    queue='info_data', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

try:
    # Loop so we can communicate with RabbitMQ
    channel.start_consuming()
except KeyboardInterrupt:
    print("Obrigado pelos peixes")
