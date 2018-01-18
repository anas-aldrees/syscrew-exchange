# -*- coding: utf-8 -*-

import logging

import json
from kombu import Connection, Exchange
from django.conf import settings


__author__ = 'Anas Aldrees'
__email__ = 'asaldrees@syscrew.xyz'
__copyright__ = 'Copyright (C) 2017, SysCrew Co ltd'

logger = logging.getLogger(__name__)


exchange = Exchange(settings.EXCHANGE_NAME, type='topic')
connection = Connection(settings.CELERY_BROKER_URL)


def create_event(payload, routing_key, headers=None):
    from exchange.models import Publishable
    assert not headers or isinstance(headers, dict), 'headers must be dict or None'
    assert isinstance(payload, dict) \
        or isinstance(payload, list), "Must be in specific types"

    if not headers:
        headers = dict()

    publishable = Publishable.objects.create(
        payload=json.dumps(payload), routing_key=routing_key, headers=json.dumps(headers))

    logger.info('Publishable with routing_key: < %s > has been created', routing_key)

    return publishable


def publish_event(publishable):
    from exchange.producers import publish_to_broker
    publish_to_broker(
        publishable.payload,
        publishable.routing_key,
        json.loads(publishable.headers),
        str(publishable.task_id)
    )
    publishable.mark_as_published()
    logger.info('Event with routing_key < %s > has been published', publishable.routing_key)
