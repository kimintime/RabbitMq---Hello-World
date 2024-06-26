# Description: This script receives messages from a queue named hello. It is based on the RabbitMQ tutorial 1: "Hello World!".

import os
import sys

import pika


def main():
    try:
        # Create a connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        #Testing the error handling
        #raise pika.exceptions.AMQPError("This is a test error")
        #raise ValueError("This is a test error")
        
        # Create a queue named hello, if it doesn't exist
        channel.queue_declare(queue='hello')
        
        # Define a callback function that will be called when a message is received. The ch, method, properties, and body parameters are required by the library. Only body is used in this example.
        def callback(ch, method, properties, body):
            
            # Print the message to the console. message is a bytes object, so we need to decode it to a string.
            print(" [x] Received %r" % body.decode())
            
        channel.basic_consume(queue='hello',
                            on_message_callback=callback,
                            auto_ack=True)
            
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
        
    # Handle exceptions
    except pika.exceptions.AMQPError as e:
        print("An error occurred: " + str(e))
        
    except Exception as e:
        print("An error occurred: " + str(e))
        
    finally:
        # Close the connection
        connection.close()
    
if __name__ == '__main__':
    try:
        main()
        
    # Handle the KeyboardInterrupt exception to allow the user to stop the script with CTRL+C
    except KeyboardInterrupt:
        print('\nInterrupted')
        
        # Exit the script
        try:
            sys.exit(0)
        
        except SystemExit:
            os._exit(0)
        
        