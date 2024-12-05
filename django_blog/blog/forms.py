from django import forms
from .models import Post,Comment,Tag
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(attrs={'placeholder': 'Add comma-separated tags'}),
        help_text='Add comma-separated tags.',
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        if self.cleaned_data['tags']:
            tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',')]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance       

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']        