from django import forms


class BookNameFilterForm(forms.Form):
    name = forms.CharField()