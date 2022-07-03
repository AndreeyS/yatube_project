from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from posts.models import Post

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group',)

