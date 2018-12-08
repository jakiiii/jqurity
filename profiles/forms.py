from django import forms

from ckeditor.widgets import CKEditorWidget

from post.models import Post


# Create your form here.
class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class CreatePostFrom(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'link',
            'category',
            'tags',
            'timestamp',
            'active',
            'slug',
        ]
        widgets = {
            'timestamp': DateTimeInput(),
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'link': 'Link',
            'category': 'Category',
            'tags': 'Tags',
            'timestamp': 'Timestamp',
            'active': 'Active',
            'slug': 'Slug',
        }
