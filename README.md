This is a celery kombu wrapper

build the package:

    `python setup.py sdist`

install with pip

    `pip install dist/exchange-xx.tar.gz`


 Add `'exchange'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'exchange',
    )

configure your exchange name and consumers

    EXCHANGE_NAME = 'daal'

    EXCHANGE = {
        'QUEUES': {
            'myapp.consumers.my_queue': {
                'CONSUMERS': [
                    'myapp.consumers.my_consumer',
                ],
            }
        }
    }

create your consumers and queues

    from kombu import Queue
    from exchange import exchange

    test_queue = Queue(
        'daal_test',
        exchange,
        routing_key='my.routing.key
    )


    def test_consumer(body, message):
        # write your magic here
        message.ack()

start your consumers

    python manage.py consumers_worker