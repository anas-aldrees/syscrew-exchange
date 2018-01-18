# -*- coding: utf-8 -*-

import logging

from kombu.pools import producers
from exchange import connection, exchange

__author__ = 'Anas Aldrees'
__email__ = 'asaldrees@syscrew.xyz'
__copyright__ = 'Copyright (C) 2017, SysCrew Co ltd'

logger = logging.getLogger(__name__)


def publish_to_broker(payload, routing_key, headers=None, message_id=None):

    with producers[connection].acquire(block=True) as producer:
        producer.publish(
            payload,
            headers=headers,
            serializer='text',
            content_type='application/json',
            exchange=exchange,
            routing_key=routing_key,
            declare=[exchange],
            retry=True,
            message_id=message_id)

    return True
