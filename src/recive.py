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


def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print("Received: %r" % mensagem)
    Dados.create(    
                    rasp_id = mensagem["id"],
                    temp = mensagem["temp"],
                    umi = mensagem["umi"],
                    pres = mensagem["pres"],
                    data = mensagem["date"],
                    )


channel.basic_consume(
    queue='info_data', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

try:
    # Loop so we can communicate with RabbitMQ
    channel.start_consuming()
except KeyboardInterrupt:
    # Gracefully close the connection
    connection.close()
    print("Obrigado pelos peixes")
