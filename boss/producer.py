import pika
import json

params = pika.URLParameters('amqps://evcwolsy:qY9FGzpS2C1qdQVELBmlwNO9g8y6XhXe@dingo.rmq.cloudamqp.com/evcwolsy')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='order', body=json.dumps(body), properties=properties)