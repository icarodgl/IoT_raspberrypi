#!/usr/bin/env python3
import pika
from data_generator import DataGenerator
import datetime
import time
from daemonize import Daemonize


def main():
    # tempo para iniciar o sistema e não dar erro.
    print("sender iniciando....")
    time.sleep(1)
    print("sender  conectando e enviando dados:")
    credentials = pika.PlainCredentials('pi', '123123')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('10.0.0.2', 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='info_data')

    gerador = DataGenerator()
    active = True
    while active:
        try:
            time.sleep(1)
            mensagem = gerador.generate()
            # envia a mensagem
            channel.basic_publish(
                exchange='', routing_key='info_data', body=mensagem)
            # avisa que enviou
            print("enviado data: %s" % mensagem)
        except KeyboardInterrupt:
            active = False
            print("", end="\r")
    print("finalizado")
    connection.close()


pid = "/tmp/test.pid"
daemon = Daemonize(app="send_IOT", pid=pid, action=main)
daemon.start()
