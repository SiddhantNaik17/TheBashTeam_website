from django.db import models
from django.utils import timezone

year_dropdown = []
for y in range(timezone.now().year - 30, timezone.now().year + 1):
    year_dropdown.append((y, y))


class Motorcycle(models.Model):
    company = models.CharField( max_length=200)
    name = models.CharField(max_length=200)
    manufacture = models.IntegerField(choices=year_dropdown, default=timezone.now().year)

    def __str__(self):
        return self.company
