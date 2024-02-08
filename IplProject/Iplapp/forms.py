from django import forms
# from django.forms import ModelForm,Form
from .models import Franchesis
class FranchesisModelForm(forms.ModelForm):
    class Meta:
        model = Franchesis
        # fields = "__all__"
        # fields = ('f_name','f_nickname')
        exclude = ('f_logo',)


class FranchesisForm(forms.Form):
    f_name = forms.CharField(max_length=30)
    f_nickname = forms.CharField(max_length=4)
    f_started_year = forms.IntegerField()
    no_of_titles = forms.IntegerField()
    f_logo = forms.ImageField(required=False)
