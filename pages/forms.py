from django import forms

## I'm importing the model needed
from .models import Company

## the model form to insert and edit a new company
class InsertCompany(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = ['company','nation']
