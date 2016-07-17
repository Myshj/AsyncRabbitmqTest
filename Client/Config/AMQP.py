import ssl

# Где размещена очередь для прослушивания.
HOST = "localhost"

# Порт очереди для прослушивания.
PORT = 5671

# Имя очереди для прослушивания.
QUEUE = "db_users__input_queue"

# Сколько сообщений из очереди резервируем для себя.
PREFETCH_COUNT = 1

# Используем ли SSL.
USE_SSL = True

# С какими параметрами используем SSL.
SSL_OPTIONS = {"ca_certs": "/etc/rabbitmq/testca/cacert.pem",
               "certfile": "/etc/rabbitmq/client/cert.pem",
               "keyfile": "/etc/rabbitmq/client/key.pem",
               "cert_reqs": ssl.CERT_REQUIRED,
               "server_side": False}

# Имя точки обмена.
EXCHANGE = 'message'

# Тип точки обмена.
EXCHANGE_TYPE = 'topic'

# Какие сообщения будем получать.
ROUTING_KEY = 'example.text'

# Под каким пользователем заходим.
USER = 'guest'

# Пароль пользователя.
PASSWORD = 'guest'

# С каким интервалом отправляем сообщения.
PUBLISH_INTERVAL = 0.0
