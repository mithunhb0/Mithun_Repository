from django import forms
from cricapp.models import Cricketer

class CricketerForm(forms.ModelForm):
    def clean_age(self):
        input_age = self.cleaned_data['age']
        if input_age>45:
             raise forms.ValidationError('Age Should be less than 45 years')
        return input_age

    class Meta:
        model = Cricketer
        fields = '__all__'

       