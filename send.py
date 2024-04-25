# Description: This script sends a message to a queue named hello. Run receive.py in another terminal to receive the message.

import pika

# Create a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue named hello
channel.queue_declare(queue='hello')

# Send a message to the queue. The exchange is default and the routing key is the queue name.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

# Print a message to the console. message is a bytes object, so we need to decode it to a string.
print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()