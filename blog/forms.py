from django import forms
from .models import Blog

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
# fields = __all__ 은 model의 모든 필드 포함.
# exclude = ['body'] body를 제외한 모든 필드 포함.
