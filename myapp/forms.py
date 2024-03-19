from django import forms

class InputForm1(forms.Form):
  name=forms.CharField()
  email=forms.EmailField()
  password=forms.CharField()