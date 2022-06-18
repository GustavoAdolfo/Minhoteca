from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.forms import PasswordChangeForm as PdwChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import MinhotecaUser as MinhotecaUser
# from captcha.fields import CaptchaField


class CreateUserForm(UserCreationForm):
    # recaptcha = CaptchaField()
    # site key = 6LfI738gAAAAADAs0ja5JcUFdzPT4yXViOXs5pUX
    # secret key = 6LfI738gAAAAAM6mEDXnCPNziPeBy8D_aaB4WT_m
    email = forms.EmailField(label='Email')
    user_term_accept = forms.BooleanField(
        required=True, label='Li e aceito os termos de uso')

    def save(self, commit=True):
        if not self.cleaned_data['user_term_accept']:
            raise forms.ValidationError(
                'Você precia ler e aceitar os termos de uso para continuar.')

        user = get_user_model().objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user

    class Meta:
        model = MinhotecaUser
        fields = ['email','user_term_accept']

class UserProfileForm(ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = MinhotecaUser
        # model.state = "SP"
        fields = ['email', 'first_name', 'last_name', 'contact_phone',
            'zip_code', 'address', 'address_number', 'city', 'state',
            'address_complement', 'neighborhood']
            
    def save(self, commit=True):
        user = MinhotecaUser.objects.get(id=self.cleaned_data['id'])
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.contact_phone = self.cleaned_data['contact_phone']
        user.zip_code = self.cleaned_data['zip_code']
        user.address = self.cleaned_data['address']
        user.address_number = self.cleaned_data['address_number']
        user.address_complement = self.cleaned_data['address_complement']
        user.neighborhood = self.cleaned_data['neighborhood']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.can_borrow = \
            len(user.first_name.strip()) > 0 and \
                len(user.contact_phone.strip()) > 0 and \
                    len(user.last_name.strip()) > 0 and \
                        len(user.zip_code.strip()) > 0 and \
                            len(user.address.strip()) > 0 and \
                                len(user.city.strip()) > 0 and \
                                    len(user.address_number.strip()) > 0 and \
                                        len(user.state.strip()) > 0
        if commit:
            user.save()
        
        return user
        

