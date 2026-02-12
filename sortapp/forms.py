from django import forms

class DatasetForm(forms.Form):
    dataset = forms.CharField(
        label='Enter numbers separated by commas',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 5,2,9,1,5,6'})
    )
