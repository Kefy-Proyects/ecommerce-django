from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from django.core.exceptions import ValidationError

class UserUpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model=User
        fields=('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(UserUpdatePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class']='form-control'
        self.fields['old_password'].widget.attrs['placeholder']='Old Password'
        self.fields['old_password'].widget.attrs['id']='oldPassword'
        self.fields['old_password'].widget.attrs['required']=''
        self.fields['old_password'].label='Old Password'
        self.fields['old_password'].help_text=''

        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='New Password'
        self.fields['new_password1'].widget.attrs['id']='validationPassword1'
        self.fields['new_password1'].widget.attrs['required']=''
        self.fields['new_password1'].label='New Password'
        self.fields['new_password1'].help_text=''

        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['placeholder']='Repeat Password'
        self.fields['new_password2'].widget.attrs['id']='validationPassword2'
        self.fields['new_password2'].widget.attrs['required']=''
        self.fields['new_password2'].label='Repeat Password'
        self.fields['new_password2'].help_text=''


class UserUpdateForm(UserChangeForm):

    password=None

    email=forms.EmailField(label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control','id':'validationEmail', 'placeholder':'Direccion de correo'}))

    class Meta:
        model=User
        fields=('username','first_name', 'last_name', 'email')
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['placeholder']='First Name'
        self.fields['first_name'].label='First Name'
        self.fields['first_name'].help_text=''

        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['placeholder']='Last Name'
        self.fields['last_name'].label='Last Name'
        self.fields['last_name'].help_text=''

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].label='Username'
        self.fields['username'].help_text=''



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
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].widget.attrs['id']='validationUsername'
        self.fields['username'].widget.attrs['required']=''

        self.fields['username'].label='Username'
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