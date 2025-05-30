from django.db import models
from django.contrib.auth.models import User


class CitySearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255)
    search_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.city_name} (searched {self.search_count} times)"
