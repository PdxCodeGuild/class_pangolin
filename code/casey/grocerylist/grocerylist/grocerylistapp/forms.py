from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label=Entry_name, max_length=100)