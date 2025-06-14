from django import forms
from .models import Category, Husband

class AddPostForm(forms.Form):
    title=forms.CharField(max_length=255, min_length=5,
                          widget=forms.TextInput(attrs={'class': 'form-input'}),
                          error_messages={
                              'min_length': 'Title is too short',
                              'required': 'Title is required',
                          })
    slug=forms.SlugField(max_length=255, label='URL: ')
    content=forms.CharField(widget=forms.Textarea(), required=False)
    is_published=forms.BooleanField(required=False, initial=True)
    cat=forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='not selected', label='Category')
    husband=forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='not married', required=False)
