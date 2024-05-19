from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import NetAuthorizationRequest
from .models import Folder, File

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class NetAuthorizationRequestForm(forms.ModelForm):
    class Meta:
        model = NetAuthorizationRequest
        fields = [
            'applicant_ps_number', 'applicant_name', 'applicant_email_id',
            'request_date', 'location', 'department', 'contact_no',
            'initiator_hod_ps_no', 'initiator_hod_name', 'initiator_hod_email_id',
            'net_request_type', 'copy_to_id', 'copy_from_id',
            'application_name', 'justification'
        ]
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'applicant_ps_number': forms.TextInput(attrs={'class': 'form-control'}),
            'applicant_name': forms.TextInput(attrs={'class': 'form-control'}),
            'applicant_email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'initiator_hod_ps_no': forms.TextInput(attrs={'class': 'form-control'}),
            'initiator_hod_name': forms.TextInput(attrs={'class': 'form-control'}),
            'initiator_hod_email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'net_request_type': forms.TextInput(attrs={'class': 'form-control'}),
            'copy_to_id': forms.TextInput(attrs={'class': 'form-control'}),
            'copy_from_id': forms.TextInput(attrs={'class': 'form-control'}),
            'application_name': forms.TextInput(attrs={'class': 'form-control'}),
            'justification': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'folder']
