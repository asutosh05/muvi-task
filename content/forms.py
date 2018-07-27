from django import forms

class ContentCreateForm(forms.Form):
    name=forms.CharField(required=True)
    releaseDate= forms.DateTimeField(required=False)
    genre= forms.CharField(required=False)
    description=forms.CharField(required=False)
    category= forms.CharField(required=False)
    geoRights=forms.CharField(required=False)
    price=forms.DecimalField(required=False)
    currency=forms.CharField(required=False)