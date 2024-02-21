from django import forms

class UserInputForm(forms.Form):
    choices = (("4", "4 and up"),("3", "3 and up"),("2", "2 and up"),("1", "1 and up"))
    budget = forms.CharField(label="Budget")
    rating = forms.ChoiceField(label="Rating", choices=choices)