from moviesapp.models import movietable
from django import forms

class movietableForm(forms.ModelForm):

    class Meta:

        model = movietable
        fields = ('id','moviename','hero','heroine')
