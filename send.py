#!/usr/bin/env python
import pika
import random
import time
import datetime
import json
import netifaces

def getMacAddress():
  interfaces = netifaces.interfaces()
  interface = interfaces[0]
  if (len(interfaces) == 0):
    return ""
  elif (len(interfaces) > 1):
    interface = interfaces[1]
  else:
    interface = interfaces[0]
  return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]

# tempo para iniciar o sistema e não dar erro.
print("sender iniciando....")
# time.sleep(10)
print("sender  conectando e enviando dados:")
credentials = pika.PlainCredentials('pi', 'raspberry')
connection = pika.BlockingConnection(
   pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='info_data')

meta = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
atual = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
macaddress = getMacAddress()
active = True
while active:
  try:
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
    atual["date"] = datetime.datetime.now().__str__()
    atual["id"] = macaddress
    mensagem = json.dumps(atual)
    # fim
    # envia a mensagem
    channel.basic_publish(exchange='', routing_key='info_data', body=mensagem)
    # avisa que enviou
    print("enviado data: %s" % mensagem)
  except KeyboardInterrupt:
    active = False
    print("", end="\r")
print("finalizado")
connection.close()
