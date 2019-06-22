#!/usr/bin/env python3
import pika
from data_generator import DataGenerator
import time
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    # tempo para iniciar o sistema e não dar erro.
    print("sender  conectando e enviando dados:")
    parameters = pika.URLParameters(os.getenv('URL_MQ'))
    connection = pika.BlockingConnection(
        parameters)
    channel = connection.channel()

    channel.queue_declare(queue='info_data')

    gerador = DataGenerator()
    active = True
    while active:
        try:
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
        time.sleep(5)
main()

