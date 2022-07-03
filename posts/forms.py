from django import forms
from django.contrib.auth import get_user_model

from posts.models import Post, Group, Comment

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'description', 'slug')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

