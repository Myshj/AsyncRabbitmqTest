import pika
import ssl

server = "localhost"
port = 5671
vhost = "yourvhost"
username = "username"
password = "password"
caCert = "SSL/rootCA.crt" #change it to the actual path to CA certificate
exchangeName = "testEx"
routingKey = "test"

try:
    #connect
    credentials = pika.PlainCredentials(username, password)
    ssl_options = {"ca_certs": "/etc/rabbitmq/testca/cacert.pem",
                   "certfile": "/etc/rabbitmq/client/cert.pem",
                   "keyfile": "/etc/rabbitmq/client/key.pem",
                   "cert_reqs": ssl.CERT_REQUIRED,
                   "server_side": False}
    parameters = pika.ConnectionParameters(host = server, port = port,
                                           ssl = True, ssl_options = ssl_options)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    #send message
    properties = pika.spec.BasicProperties(content_type = "text/plain", delivery_mode = 1)
    channel.basic_publish(exchange = exchangeName, routing_key = routingKey, body = "Hello World!", properties = properties)

    #disconnect
    connection.close()
except:
    print("Maus!")