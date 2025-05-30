from django.shortcuts import render, redirect
from .forms import CityForm
from .api import get_weather
from .models import SearchHistory

def weather_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather(city)

            if weather_data:
                # Сохраняем историю поиска
                SearchHistory.objects.get_or_create(user=request.user, city=city)
                return render(request, 'weather/weather.html', {'weather_data': weather_data, 'city': city})
            else:
                form.add_error('city', 'Не удалось получить данные о погоде для этого города.')
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {'form': form})
