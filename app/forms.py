from django import forms


class GenerateTypedWord(forms.Form):
    typed_word = forms.CharField(max_length=50)
