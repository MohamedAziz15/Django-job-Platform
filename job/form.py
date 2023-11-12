from django import forms
from django.core.validators import FileExtensionValidator
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import jobApply,job


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


class AddjobForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    class Meta:
        model = job
        fields = ['title', 'Location', 'company', 'salary_start', 'salary_end', 'description','vacancy','job_type','experience','category']









