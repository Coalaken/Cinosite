from django import forms

from . models import Film

class FilmAddForm(forms.ModelForm):

    class Meta:
        model = Film 
        fields = ('name', 'description', 'author', 'image', 'video')
        
