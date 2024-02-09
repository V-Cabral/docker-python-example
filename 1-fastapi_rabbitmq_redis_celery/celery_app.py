from celery import Celery

BACKEND = "redis://:abcd@redis:6379/0"

app = Celery(
    "Celery_app",
    broker="amqp://admin:mypassword@rabbitmq:5672//",
    backend=BACKEND,
    include=["tasks"],
)
