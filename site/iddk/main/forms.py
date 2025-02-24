from django import forms
from .models import News, Image, Audio

class NewsForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    audios = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = News
        fields = ['title', 'content', 'images', 'audios']