from __future__ import unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand
from kombu import Connection

from exchange.consumers import Worker


class Command(BaseCommand):
    help = ''' Run Exchange consumer worker '''

    def handle(self, *args, **options):
        with Connection(settings.CELERY_BROKER_URL) as conn:
            worker = Worker(conn)
            worker.run()
