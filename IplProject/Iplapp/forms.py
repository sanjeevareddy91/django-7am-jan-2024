from django import forms
# from django.forms import ModelForm,Form
from .models import Franchesis
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Row,Column
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('f_name', css_class='form-group col-md-6 mb-0'),
                Column('f_nickname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('f_started_year', css_class='form-group col-md-6 mb-0'),
                Column('no_of_titles', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'f_logo',
            Submit('submit', 'Register')
        )
