from .models import Sample
from django.forms import ModelForm

class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = ['title', 'path_to_template']