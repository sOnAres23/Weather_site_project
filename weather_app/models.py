from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    search_count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.city} ({self.search_count} раз)'

    class Meta:
        unique_together = ['user', 'city']
