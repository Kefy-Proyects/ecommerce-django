from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control','id':'validationEmail', 'placeholder':'Direccion de correo'}))
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')

    # def clean_username(self):
    #     username=self.cleaned_data.get('username')
    #     if not 6 <= len(username) <= 12:
        
    #         raise ValidationError('El usuario debe tener entre 6 y 12 caracteres.')
        
    #     return username

    # def clean_password2(self):
    #     password1=self.cleaned_data.get('password1')
    #     password2=self.cleaned_data.get('password2')

    #     if len(password2) < 7:
    #         raise ValidationError('La contraseña debe tener mas de 6 caracteres.')
        
    #     if password1 != password2:
    #         raise ValidationError('Las contraseñas no coinciden.')
        
    #     digit=False 
    #     minusc=False 
    #     mayusc=False
    #     for passw in password2:
    #         if passw.isspace():
    #             raise ValidationError('La contraseña no puede tener espacios en blanco.')
    #         elif passw.isdigit():
    #             digit=True 
    #         elif passw.isupper():
    #             mayusc=True 
    #         elif passw.islower():
    #             minusc=True

    #     if not digit:
    #         raise ValidationError('La contraseña debe tener al menos un numero')
    #     if not minusc:
    #         raise ValidationError('La contraseña debe tener al menos una minuscula.')
    #     if not mayusc:
    #         raise ValidationError('La contraseña debe contener al menos una mayuscula.')
        
    #     return password2



    def save(self, commit=True):
        user=User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['username'].widget.attrs['id']='validationUsername'
        self.fields['username'].widget.attrs['required']=''

        self.fields['username'].label='Usuario'
        self.fields['username'].help_text=''

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Contraseña'
        self.fields['password1'].widget.attrs['id']='validationPassword1'
        self.fields['password1'].widget.attrs['required']=''

        self.fields['password1'].label='Contraseña'
        self.fields['password1'].help_text=''

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Repetir contraseña'
        self.fields['password2'].widget.attrs['id']='validationPassword2'
        self.fields['password2'].widget.attrs['required']=''

        self.fields['password2'].label='Repetir Contraseña'
        self.fields['password2'].help_text=''