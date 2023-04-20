from django import forms


from . models import Film

class FilmAddForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Film 
        fields = ('name', 'description', 'author', 'image', 'video')