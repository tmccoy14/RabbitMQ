"""Third party modules"""
import pika

# Establish connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# Create a queue to which the message will be delivered
channel.queue_declare(queue="hello")

# Use a default exchange to specify which queque the message should go to
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()
