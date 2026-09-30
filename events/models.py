from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    location = models.TextField(blank=True, default="TBD")
    published_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title