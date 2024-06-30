from django import forms
from .models import classifier

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = classifier
        fields = ['image']
