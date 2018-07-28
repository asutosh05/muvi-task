from django import forms
from .models import Content
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea,DateInput,MultipleChoiceField

class ContentCreateForm(forms.ModelForm):
    class Meta:
        
        model=Content
        fields = [
            'name',
            'releaseDate',
            'genre',
            'description',
            'category',
            'geoRights',
            'price',
            'currency'
        ]
        labels = {
            'name': _('Muvi Name'),
            'releaseDate':_('Release/Recored Date'),
            'geoRights':_('Geographical Rights For')
        }
        help_texts = {
            'releaseDate': 'Please enter in MM/DD/YYYY',
        }
         
    def clean_name(self):
        name=self.cleaned_data.get("name")
        if name == "hello":
            raise forms.ValidationError("Not a valid error")
        return name
        




    