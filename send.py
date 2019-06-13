#!/usr/bin/env python
import pika
import random
import time
import datetime

# tempo para iniciar o sistema e não dar erro.
print("sender iniciando....")
time.sleep(90)
print("sender  conectando e enviando dados:")
credentials = pika.PlainCredentials('pi', '123123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('10.0.0.2', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

meta = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
atual = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
while 1:
    time.sleep(1)
    # logica do fake data
    if (round(atual["temp"], 1) == round(meta["temp"], 1)):
        meta["temp"] = random.randint(20, 35) + random.random()
    if (round(atual["pres"], 3) == round(meta["pres"], 3)):
        meta["pres"] = random.random()
    if (round(atual["umi"], 1) == round(meta["umi"], 1)):
        meta["umi"] = random.randint(40, 95) + random.random()
    atual["umi"] += (meta["umi"] - atual["umi"])/10
    atual["pres"] += (meta["pres"] - atual["pres"])/10
    atual["temp"] += (meta["temp"] - atual["temp"])/10
    mensagem = "data: %s temp:%.2f, pres: %.3f, umi: %.2f" % (datetime.datetime.now(
    ).__str__(), atual["temp"], atual["pres"], atual["umi"],)
    # fim
    # envia a mensagem
    channel.basic_publish(exchange='', routing_key='hello', body=mensagem)
    # avisa que enviou
    print("enviado data: %s" % mensagem)

print("finalizado")
connection.close()
