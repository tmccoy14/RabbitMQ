# Hello World!

RabbitMQ is a message broker: it accepts and forwards messages.

It accepts, stores, and forwards binary blobs of data - messages.

RabbitMQ jargon:

Producing -- means nothing more than sending; a program that sends messages is a producer

Queue -- the name for a post box that lives inside RabbitMQ; a queue is only bound by the host's memory and disk limits

Consuming -- similar meaning to receiving; a consumer is a program that mostly waits to receive messages

An application can be both a producer and consumer
