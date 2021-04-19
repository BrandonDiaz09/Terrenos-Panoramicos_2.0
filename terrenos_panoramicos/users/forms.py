from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    contraseña = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    confirmar_contraseña = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    nombre = forms.CharField(min_length=2, max_length=50)
    apellido_paterno = forms.CharField(min_length=2, max_length=50)

    apellido_materno = forms.CharField( min_length=2, max_length=50)
    
    correo_electrónico = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El username ya esta en uso')
        return username

    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['correo_electrónico']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('El correo electrónico ya esta en uso')
        return email

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['contraseña']
        password_confirmation = data['confirmar_contraseña']

        if password != password_confirmation:
            raise forms.ValidationError('La contraseña no coincide')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data

        user = User.objects.create_user(username=data['username'], 
                                        password=data['contraseña'],
                                        first_name=data['nombre'],
                                        last_name=data['apellido_paterno'],
                                        email=data['correo_electrónico'])
        profile = Profile(user=user,
                          last_nameMa= data['apellido_materno'])
        profile.save()

class ProfileForm(forms.Form):
    """Profile form."""

    curp = forms.CharField(max_length=18,required=True )
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
    ine = forms.ImageField()