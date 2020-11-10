from django import forms



class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", help_text="Bitte gib hier deine RZ Email Adresse ein", max_length=50)
    password  = forms.CharField(label="Passwort", help_text="Bitte gib hier dein Passwort ein", max_length = 50)