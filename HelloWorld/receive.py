"""Standard library"""
import sys
import os

"""Third party modules"""
import pika


def main():
    # Establish connection with RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Create a queue to which the message will be delivered
    channel.queue_declare(queue="hello")

    # Callback will receive messages from the queue
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Call callback function to receive messages from queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    # Waits for data and runs callbacks
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
