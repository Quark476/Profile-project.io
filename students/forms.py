from django import forms
from .models import Portfolio
import json

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'last_name', 'first_name', 'email', 'phone', 
            'school', 'education_level', 'specialization',
            'experience', 'hobbies', 'skills', 'achievements', 'goals'
        ]
        widgets = {
            'skills': forms.HiddenInput(),
        }

    def clean_skills(self):
        skills = self.cleaned_data.get('skills', '[]')
        if not skills:
            return '[]'
        try:
            json.loads(skills)
            return skills
        except json.JSONDecodeError:
            return '[]'
