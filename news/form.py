from django import forms
from news.models import Comment, News
from tinymce.widgets import TinyMCE


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['email', 'text']


class NewsForm(forms.ModelForm):
    # text = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

    class Meta:
        model = News
        fields = ['article', 'text']
