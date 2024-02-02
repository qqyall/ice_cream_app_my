from django import forms
from .models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = {
            'title',
            'description',
            'price',
            'comment'
        }
        widgets = {
            'title': forms.Textarea(attrs={'cols': '10', 'rows': '1'}),
            'description': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
        }
