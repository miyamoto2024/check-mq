import pika, fire

RABBITMQ_HOST = 'hostname'
RABBITMQ_USER = 'user'
RABBITMQ_PASS = 'password'

def connect():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(RABBITMQ_HOST, 5672, '/', credentials))
    channel = connection.channel()
    try:
        channel.queue_declare(queue='hello')
        print('completed connection.')
        return channel
    except pika.exceptions.ChannelClosedByBroker as ex:
        print(ex)
        exit(1)

def produce(ch):
    ch.basic_publish(exchange='', routing_key='hello', body='TEST.')
    print('completed produce.')

def consume(ch):
    # ch.basic_consume(queue='hello', on_message_callback=on_message)
    # ch.start_consuming()
    for method, properties, body in ch.consume('hello'):
        print(body.decode('utf-8'))
        ch.basic_ack(delivery_tag=method.delivery_tag)
    print('completed consume.')
    
# callback function for consumer
def on_message(ch, method, frame, body):
    print(body.decode('utf-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)

ch = connect()
fire.Fire({'produce': lambda: produce(ch), 'consume': lambda: consume(ch)})
ch.close()
