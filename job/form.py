from django import forms
from django.core.validators import FileExtensionValidator
from .models import jobApply


class jobApplyForm(forms.ModelForm):
    
    
    resume = forms.FileField(
        label='resume',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text="Please upload your latest resume (PDF only)",
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf'})
    )

    class Meta:
        model = jobApply
        fields = ['job', 'username', 'email', 'resume', 'cover_letter', 'github_url', 'linkedin_url']












