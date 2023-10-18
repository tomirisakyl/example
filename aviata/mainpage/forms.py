from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User
from .models import UserProfile
# from .models import User
from .models import Ticket
from django.forms import ModelForm, TextInput
from .models import UserProfile



class ItemsForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['company', 'city1', 'city2', 'time1', 'time2', 'price']

        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company',
            }),
            'city1': forms.TextInput(attrs={
                
                'class': 'form-control',
                'placeholder': 'City1',
            }),
            'city2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City2',
            }),
            'time1': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'time1',
            }),
            'time2': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'time2',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
            }),
        }
        
class ChangeForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['company', 'city1', 'city2', 'time1', 'time2', 'price']

        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company',
            }),
            'city1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City1',
            }),
            'city2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City2',
            }),
            'time1': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'time1',
            }),
            'time2': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'time2',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
            }),
        }


# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(max_length=254)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)


#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class UploadForm(forms.Form):
    image_upload = forms.ImageField()
    file_upload = forms.FileField()


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']

        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'placeholder': 'Enter your bio here...',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Birth Date',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
        }

# class CustomCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
# # class SignUpForm()


# class EditProfileForm(UserChangeForm):
#     template_name='/something/else'

#     class Meta:
#         model = User
#         fields = (
#             'email',
#             'first_name',
#             'last_name',
#             'password'
#         )

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2'
#         )

#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()

#         return user