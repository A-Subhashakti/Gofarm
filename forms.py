from django import forms

class CropForm(forms.Form):
    nitrogen = forms.FloatField()
    phosphorus = forms.FloatField()
    potassium = forms.FloatField()
    temperature = forms.FloatField()
    humidity = forms.FloatField()
    ph = forms.FloatField()
    rainfall = forms.FloatField()
