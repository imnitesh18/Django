from django import forms

class InputForm1(forms.Form):
  name=forms.CharField()
  email=forms.EmailField()
  password=forms.CharField()

from django import forms
from .models import SignUp

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)

from .models import Customers
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['username', 'email', 'password'] 



from .models import Cookie

class CookieForm(forms.ModelForm):
    class Meta:
        model = Cookie
        fields = ['name', 'value']



