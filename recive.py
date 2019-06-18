#!/usr/bin/env python
import pika
import json
from peewee import *
from model import Dados


credentials = pika.PlainCredentials('pi', 'raspberry')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('172.16.108.16', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')


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
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
