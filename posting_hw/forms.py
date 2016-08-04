from django import forms
from .models import Post, Comment, Tag

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'tag_set', 'created_at']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','author', 'message']
