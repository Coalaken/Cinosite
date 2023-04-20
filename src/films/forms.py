from django.forms import forms


from . models import Film

class FilmAddForm(forms.Modelform):
    email = forms.EmailField(required=True)
    class Meta:
        model = Film 
        fields = ('name', )