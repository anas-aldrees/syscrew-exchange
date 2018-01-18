from django.db import models
from django.utils import timezone
import uuid


class Publishable(models.Model):
    payload = models.TextField()
    routing_key = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    headers = models.TextField(blank=True)
    published_time = models.DateTimeField(null=True, blank=True)
    task_id = models.UUIDField(default=uuid.uuid4)

    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

    def mark_as_published(self):
        self.published = True
        self.published_time = timezone.now()
        self.save()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.routing_key
