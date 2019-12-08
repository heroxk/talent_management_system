from django import forms
from django.core import validators
import pandas as pd
import os



def validate_all_choices(value):
    # here have your custom logic
    pass

SKILL_LEVEL_CHOICES = [('1', '1 - Novice'), ('2', '2 - Beginner'), ('3', '3 - Competent'), ('4', '4 - Proficient'), ('5', '5 - Expert')]

SKILLS_L2_CHOICES = [(s, s) for s in pd.read_csv('data/skills_l2.csv')['skill_name']]
SKILLS_L3_CHOICES = [(s, s) for s in pd.read_csv('data/skills_l3.csv')['skill_name']]

# SKILLS_L2_CHOICES = [('1', os.getcwd())]
# SKILLS_L3_CHOICES = []
#
# SKILL_LEVEL_CHOICES = [('AWS', 'AWS')]

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
    # skillgroup = forms.ChoiceField(widget=forms.Select, choices=SKILLS_L2_CHOICES)
    # skill = forms.ChoiceField(widget=forms.Select, choices=SKILLS_L3_CHOICES)

    # skillgroup = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control input-lg'}), choices=SKILLS_L2_CHOICES, )
    selected_skill = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control input-lg'}), choices=SKILLS_L3_CHOICES)
