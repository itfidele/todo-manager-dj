from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Task ,Category
from django.contrib.auth import get_user_model

User = get_user_model() # get user model from settings.py

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ['user']



class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        exclude=["last_login","is_superuser","is_staff","is_active","date_joined","groups","user_permissions","password"]



class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        exclude = ['user']