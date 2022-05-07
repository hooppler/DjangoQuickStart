from django import forms

class TestForm(forms.Form):
    attribute1 = forms.CharField(label='Attribute1', max_length=30)
    attribute2 = forms.CharField(label='Attribute2', max_length=30)

