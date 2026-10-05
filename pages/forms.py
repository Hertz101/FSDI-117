from django import forms

class ContactForm(forms.Form):
  name = forms.Charfield(
    max_length= 50,
    widget=forms.TextImput(attrs={'placeholder': 'Your Name'})
  )
  email = forms.EmailField(
    wiget=forms.EmailInput(attrs={'placeholder': 'Your email'})
  )
  message = forms.Charfield(
    widget=forms.Textarea(attrs={'placeholder': 'Your message'})
  )