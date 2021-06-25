from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter title'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write...',
                'rows': 7,
            },
            
        ),
        required= False
    )

    class Meta:
        model = Post
        fields = ('title', 'content',)


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter title'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write...',
                'rows': 7,
            },
            
        ),
        required= False
    )
    
    class Meta:
        model = Post
        fields = ('title', 'content',)