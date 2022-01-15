from django import forms
from blogapp.models import Comment


#It doesnt have table so considered Form
class EmailSendForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    to = forms.CharField(max_length=50)
    comments = forms.CharField(widget=forms.Textarea, required=False)

#it has table so considered ModelForm
class CommentForm(forms.ModelForm):
    class  Meta:
        model = Comment
        fields = ('name', 'email', 'body')

