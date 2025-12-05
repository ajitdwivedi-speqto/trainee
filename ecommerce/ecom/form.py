from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.FloatField()
    specifications = forms.CharField(widget=forms.Textarea)
    img = forms.ImageField(required=False)

class buyForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(min_value=1)       