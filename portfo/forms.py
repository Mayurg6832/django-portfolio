from django import forms

class UserForm(forms.Form):
	email=forms.EmailField(max_length=200)