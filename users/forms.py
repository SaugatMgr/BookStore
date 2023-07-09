from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img']