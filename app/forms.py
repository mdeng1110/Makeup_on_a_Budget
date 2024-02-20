from django import forms

class UserInputForm(forms.Form):
    budget = forms.CharField(label="Budget")