from django import forms 

class CustomerForm(forms.Form):
    gender = forms.CharField(max_length=2, widget=forms.Select(choices=[('Male', 'Male'),('Female', 'Female')]))
    age = forms.IntegerField()
    salary = forms.IntegerField()
