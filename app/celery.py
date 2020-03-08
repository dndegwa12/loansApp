
from __future__ import absolute_import
from celery import Celery


"""
Here, we initialize an instance of Celery called app, which is used later for creating a task.
The first argument of Celery is just the name of the project package.

The broker argument specifies the broker URL, which should be the RabbitMQ. Note that the format of broker URL should be:
transport://userid:password@hostname:port/virtual_host
For RabbitMQ, the transport is amqp.
The backend argument specifies a backend URL. A backend in Celery is used for storing the task results.
"""

"""
We must have installed rabbitMQ and created a virtual host and user, and set appropriate permissions
"""

app = Celery(__name__,
             broker='amqp://ken:123456@localhost/rmq_vhost',
             backend='rpc://',
             include=['app.tasks'])