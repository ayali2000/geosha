from django.contrib.auth import forms
from django import forms
from geomatics.models import Quest,Ans

class QuesForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control",
        "placeholder":"Ask your question here",
        "rows":6
    }))
    class Meta:
        model = Quest
        fields = ['question']


class AnsForm(forms.ModelForm):
    ans = forms.CharField(widget=forms.Textarea(attrs={
         
        }))

    class Meta:
        model = Ans
        fields = ['ans']         