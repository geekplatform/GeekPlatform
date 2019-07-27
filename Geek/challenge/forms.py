from django import forms
from .models import Category
class SubmitForms(forms.Form):
    s_flag=forms.CharField()

"""
class ScoreboardForm(forms.Form):
    list=((0,"看所有人"),(1,"只看新生"))
    Form_is_freshman=forms.IntegerField(widget=forms.Select(choices=list))
    Form_category=forms.IntegerField(widget=forms.Select())
    def __init__(self,*args,**kwargs):
        super(ScoreboardForm,self).__init__(*args,**kwargs)
        self.fields["Form_category"].widget.choices=Category.objects.all().values_list('id','name')
"""