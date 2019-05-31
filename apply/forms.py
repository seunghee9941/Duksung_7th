from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'major', 'student_id', 'email', 'phone', 'body', 'file', 'isFinal']
