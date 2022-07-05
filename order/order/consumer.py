import pika

params = pika.URLParameters('amqps://evcwolsy:qY9FGzpS2C1qdQVELBmlwNO9g8y6XhXe@dingo.rmq.cloudamqp.com/evcwolsy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):
    print('Received in order')
    print(body)
    

channel.basic_consume(queue='order', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()