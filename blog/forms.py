from django import forms
from blog.models import Posts

class PostsForm(forms.ModelForm):
    """ Render and process a form based on the Posts model """
    class Meta:
        model = Posts
        fields = "__all__"