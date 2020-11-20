from django.db import models
from django.utils import timezone

MANUFACTURED_YEAR_CHOICES = [(str(y), str(y)) for y in range(timezone.now().year - 30, timezone.now().year + 1)]


class Motorcycle(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    manufactured_year = models.CharField(max_length=10, choices=MANUFACTURED_YEAR_CHOICES)

    def __str__(self):
        return '%s %s' % (self.company, self.name)
