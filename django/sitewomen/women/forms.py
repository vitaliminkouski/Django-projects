from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Husband, Women

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='not selected', label='Category')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='not married', required=False)

    class Meta:
        model=Women
        fields=['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(),
        }

        labels={'slug': 'URL'}

    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>50:
            raise ValidationError('Length greater than 50 symbols')

        return title




