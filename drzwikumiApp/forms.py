from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label="Twój email")
    subject = forms.CharField(required=True, label="Temat")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Wiadomość")
