from django import forms
from django.core import validators


SKILL_LEVEL_CHOICES = [('1', '1 - Novice'), ('2', '2 - Beginner'), ('3', '3 - Competent'), ('4', '4 - Proficient'), ('5', '5 - Expert')]

class FormInfo(forms.Form):
    name = forms.CharField()
    organisation = forms.CharField()
    email = forms.EmailField()
    skill = forms.CharField()
    skill_level = forms.ChoiceField(widget=forms.Select, choices=SKILL_LEVEL_CHOICES)

class SerachByName(forms.Form):
    name = forms.CharField(required=False)

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("Ensure Emails Match!")

class SerachBySkill(forms.Form):
    skill = forms.Select()
