from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error("value", "Valor mínimo permitido é de R$ 50.000,00")
        else:
            return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2011:
            self.add_error("factory_year", "Ano de fabricação mínimo permitido para cadastro é de 2011")
        else:
            return factory_year
