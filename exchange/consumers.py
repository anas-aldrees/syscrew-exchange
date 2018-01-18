# -*- coding: utf-8 -*-

import logging

from kombu.mixins import ConsumerMixin
from kombu.utils.encoding import safe_repr
from django.conf import settings
from django.utils.module_loading import import_string

__author__ = 'Anas Aldrees'
__email__ = 'asaldrees@syscrew.xyz'
__copyright__ = 'Copyright (C) 2017, SysCrew Co ltd'

logger = logging.getLogger(__name__)


class Worker(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection

    def on_consume_ready(self, connection, channel, consumers, **kwargs):
        logger.info('Events Consumer started')

    def on_decode_error(self, message, exc):
        logger.error(
                "Can't decode message body: %s (type:%s encoding:%s raw:%s')",
                exc, message.content_type, message.content_encoding,
                safe_repr(message.body)
        )
        message.reject()

    def get_consumers(self, Consumer, channel):
        queues = settings.EXCHANGE['QUEUES']
        res = []

        for queue, consumers in queues.items():
            res.append(
                Consumer(
                    queues=import_string(queue),
                    accept=['json'],
                    callbacks=[import_string(x) for x in [consumer for consumer in consumers['CONSUMERS']]]
                ),
            )

        return res
