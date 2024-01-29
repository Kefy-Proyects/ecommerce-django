from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion de correo'}))
    print('hola')
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['username'].label='Que muestra?'
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 </small></span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Contraseña'
        self.fields['password1'].label='Que muestra password1?'
        self.fields['password1'].help_text='<ul class="form-text text-muted"><li>Required. Must have more than 4 digitsz </li><ul>'
        
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Repetir contraseña'
        self.fields['password2'].label='Que muestra password2?'
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Required. Must the same </small></span>'


