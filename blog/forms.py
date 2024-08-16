from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'style': 'border: 2px solid #333; padding: 10px; font-size: 16px;'
            }),
            'content': TinyMCE(attrs={
                'class': 'form-control',
                'style': 'border: 2px solid #333; padding: 15px; font-size: 16px;',
                'cols': 80,
                'rows': 10,
            }),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Content',
        }
