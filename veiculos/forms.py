from django import forms
from veiculos.models import Carros

class CarrosForm(forms.ModelForm):

    class Meta:
        model = Carros
        fields = [
          "modelo_carro",
          "marca_carro",
          "ano_carro",
        ]

