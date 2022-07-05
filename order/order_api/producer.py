import pika

params = pika.URLParameters('amqps://evcwolsy:qY9FGzpS2C1qdQVELBmlwNO9g8y6XhXe@dingo.rmq.cloudamqp.com/evcwolsy')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='boss', body='hello')