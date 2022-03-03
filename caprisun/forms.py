
from django.forms import ModelForm
from .models import Question

class questionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']



#class TextForm(forms.Form):
 #   text = forms.CharField(label='Your text', max_length=200)

