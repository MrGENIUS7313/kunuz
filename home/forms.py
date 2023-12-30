from django import forms
from .models import News
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'body', 'video', 'category', 'tags', 'is_active']
       