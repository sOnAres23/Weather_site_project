from django.test import TestCase
from django.contrib.auth.models import User
from .models import CitySearch


class CitySearchTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_city_search(self):
        """Проверяем создание поиска города"""
        city_search = CitySearch.objects.create(user=self.user, city_name="Москва")
        self.assertEqual(city_search.city_name, "Москва")
        self.assertEqual(city_search.user, self.user)

    def test_city_search_count(self):
        """Проверяем увеличение счетчика поиска города"""
        city_search = CitySearch.objects.create(user=self.user, city_name="Москва")
        city_search.search_count += 1
        city_search.save()
        self.assertEqual(city_search.search_count, 1)
