from django.contrib.auth import forms
from django import forms
from store.models import Order

class OrderForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"phone number",
        "class":'form-control',
        'rows':1
    }))
    customer_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Name",
        "class":'form-control',
        'rows':1,
        
    }))
    quantity = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"quantity",
        "class":'form-control',
        'rows':1
    }))
    Address = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder":"Address",
        "class":'form-control',
        'rows':1
    }))
    class Meta:
        model = Order
        fields = ["phone_number","customer_name","quantity","Address"]

