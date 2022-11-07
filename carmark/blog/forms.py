from django.forms import ModelForm, TextInput, Textarea, EmailField
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        read_only_fields = ['car']
        # exclude = ['car']
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "email": TextInput(attrs={"class": "form-control", "type": "email"}),
            "message": Textarea(attrs={"class": "form-control", "cols": 10, "rows": 10})
        }
