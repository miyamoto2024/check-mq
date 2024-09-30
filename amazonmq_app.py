import ssl, pika, fire

RABBITMQ_HOST = 'xxx.amazonaws.com'
RABBITMQ_USER = 'user'
RABBITMQ_PASS = 'password'

def connect():
    # SSL/TLSでの接続設定
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
#    url = f"amqps://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:5671"
#    parameters = pika.URLParameters(url)
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    parameters = pika.ConnectionParameters(RABBITMQ_HOST, 5671, '/', credentials)
    parameters.ssl_options = pika.SSLOptions(context=ssl_context)
    connection = pika.BlockingConnection(parameters)
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
