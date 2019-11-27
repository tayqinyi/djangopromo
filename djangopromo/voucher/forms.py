from django import forms

class VoucherForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Please enter your voucher code here'}))

