from django import forms
from .models import restaurantes

class restaurantesForm(forms.ModelForm):
    class Meta:
        model = restaurantes
        fields = "__all__"