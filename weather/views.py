from django.db.models import Count
from django.shortcuts import render

from .api import get_cords, get_weather
from .forms import CitySearchForm
from .models import CitySearch
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def weather_view(request):
    if request.method == 'POST':
        form = CitySearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']

            # Получаем координаты города
            lat, lon = get_cords(city)

            # Получаем погоду
            weather = get_weather(lat, lon)

            # Сохраняем историю поиска только для авторизованных пользователей
            if request.user.is_authenticated:
                city_search, created = CitySearch.objects.get_or_create(user=request.user, city_name=city)
                if not created:
                    city_search.search_count += 1
                    city_search.save()

            return render(request, 'weather/weather.html', {'form': form, 'weather': weather})
    else:
        form = CitySearchForm()

    return render(request, 'weather/weather.html', {'form': form})


@login_required
def history_view(request):
    user = request.user
    history = CitySearch.objects.filter(user=user).order_by('-search_count')
    return render(request, 'weather/history.html', {'history': history})


def api_city_search_stats(request):
    """API для статистики по городам"""
    stats = CitySearch.objects.all().values('city_name').annotate(count=Count('city_name'))
    return JsonResponse(list(stats), safe=False)
