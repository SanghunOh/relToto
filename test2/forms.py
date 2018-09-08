from django import forms
from .models import Community_post
from .models import Member_info
from django.contrib.auth.models import User
from .models import Post



class Signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'signup_id', 'autocomplete': 'off', 'placeholder': 'Enter_new_ID'}),
            'email': forms.EmailInput(attrs={'class': 'signup_email', 'autocomplete':'off', 'placeholder': 'Enter_your_Email'}),
            'password': forms.PasswordInput(attrs={'class':'signup_pwd', 'autocomplete':'off', 'placeholder': 'Enter_new_Password'})
        }
        labels = {
            'username': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'username': None
        }

class Member_info_form(forms.ModelForm):
    class Meta:
        model = Member_info
        fields = ('name', 'myinfo', 'my_photo')


class Login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'signup_id', 'autocomplete': 'off', 'placeholder': 'Enter_new_ID'}),
            'email': forms.EmailInput(
                attrs={'class': 'signup_email', 'autocomplete': 'off', 'placeholder': 'Enter_your_Email'}),
            'password': forms.PasswordInput(
                attrs={'class': 'signup_pwd', 'autocomplete': 'off', 'placeholder': 'Enter_new_Password'})
        }
        labels = {
            'username': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'username': None
        }


#####
class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('story', 'photo', 'published_date')















########################################################

class Community_PostForm(forms.ModelForm):
    class Meta:
        model = Community_post
        fields = ('title', 'text',)
