from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


# Todo (Mentee): After creating the campaigns app
#  1. Create forms.py where you define your `CampaignForm` form
