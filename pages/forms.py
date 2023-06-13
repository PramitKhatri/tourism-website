from django.forms import ModelForm
from . models import *

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'


class PlaceForm(ModelForm):
    class Meta:
        model=Place
        fields='__all__'