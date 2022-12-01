from django.forms import ModelForm
from .models import *


class CreateForum(ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"


class CreateDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
