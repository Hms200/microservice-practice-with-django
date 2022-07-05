import pika
import os, django, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE','order.settings')
django.setup()

from order_api.models import Shop, Order


params = pika.URLParameters('amqps://evcwolsy:qY9FGzpS2C1qdQVELBmlwNO9g8y6XhXe@dingo.rmq.cloudamqp.com/evcwolsy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):
    print('Received in order')
    id = json.loads(body)
    order = Order.objects.get(id=id)
    order.deliver_finish = 1
    order.save()
    print('order deliver_finished')
    

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()