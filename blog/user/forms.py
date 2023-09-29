from django import forms




class LogiForm(forms.Form):
    username = forms.CharField(label="Input Username")
    password = forms.CharField(label="Input Password", widget= forms.PasswordInput)

class RegisterForm(forms.Form):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    email =  forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    password1 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    password2 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confrim Password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords don't match")

        values = {
            "username" : username,
            "password" : password,
            "email" : email,
        }
        return values

class LoginForm(forms.Form):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    
    