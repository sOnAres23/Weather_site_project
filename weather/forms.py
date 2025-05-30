from django import forms


class CitySearchForm(forms.Form):
    city = forms.CharField(label="Введите название города", max_length=100)
