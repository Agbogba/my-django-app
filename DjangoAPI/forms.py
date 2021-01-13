from django import forms 

class CustomerForm(forms.Form): 
    gender = forms.CharField(choices=[('Male', 'Male'), ('Female', 'Female')])
    age = forms.IntegerField() 
    salary = forms.IntegerField()

