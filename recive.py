#!/usr/bin/env python3
import pika

credentials = pika.PlainCredentials('pi', '123123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('10.0.0.2', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("Received: %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
