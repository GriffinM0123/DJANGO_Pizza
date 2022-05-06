from django import forms

from .models import Topping


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping_name']
        labels = {'topping_name':''}
        widgets = {'topping_name': forms.Textarea(attrs={'cols':80})}

