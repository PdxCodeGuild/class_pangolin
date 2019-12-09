from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label="Name of your glorious patriotic foodstuff", max_length=200)