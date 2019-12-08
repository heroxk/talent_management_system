from django.shortcuts import render
from django.http import HttpResponse
from talent_info_app.models import Person
from talent_info_app import forms
import os
import pandas as pd

# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")

    # my_dict = {'insert_me':'Hello I am from first_app/views.py !'}
    # return render(request, 'first_app/index.html', context=my_dict)

    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records':webpages_list}
    # return render(request,'first_app/index.html', context=date_dict)

    return render(request, 'talent_info_app/index.html')

def talent_search(request):

    rendering_dict = {}

    df_talent_records = pd.read_csv('data/talent_info.csv')
    df_l2_l3_mapping = pd.read_csv('data/skills_l3.csv')
    form_search = forms.SerachBySkill()

    if request.method == 'POST':
        form = forms.SerachBySkill(request.POST)

        print(request.body)

        if form.is_valid():
        # if true:

            print("VALIDATION SUCCESS!")
            selected_skill = form.cleaned_data['selected_skill']
            # skill = form['skill']
            print(f"Selected Skill: {selected_skill}")

            if len(selected_skill) > 0:
                print(df_talent_records)
                df_talent_records_subset = df_talent_records[df_talent_records['skill'].isin(selected_skill)]
                df_talent_records_subset = \
                  df_talent_records_subset.merge(df_l2_l3_mapping,
                    how='left',
                    left_on='skill',
                    right_on='skill_name') \
                    .drop(columns='skill_name') \
                    .rename(columns={'skill_group_name':'skill_group'})

                df_talent_records_subset = \
                  df_talent_records_subset[['name', 'orgnisation', 'email', 'skill_group', 'skill', 'skill_level']]

                dict_records = df_talent_records_subset.to_dict('index')
                print(dict_records)

            else:
                dict_records = dict()

            rendering_dict.update({'talent_records':dict_records})

    rendering_dict.update({'form_search':form_search})

    return render(request, 'talent_info_app/talent_search.html', context=rendering_dict)


def talent_list(request):
    # talent_list = Person.objects.order_by('name')
    # print(talent_list)
    # records_dict = {'talent_records':talent_list}
    # return render(request,'talent_info_app/talent_list.html', context=records_dict)

    df_records = pd.read_csv('data/talent_info.csv')
    dict_records = df_records.to_dict('index')

    form = forms.SerachByName()

    if request.method == 'POST':
        form = forms.SerachByName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            talent_name = form.cleaned_data['name']
            print(f"NAME: {talent_name}")

            if talent_name:
                df_records_subset = df_records[df_records['name'].str.contains(str(talent_name))]
            else:
                df_records_subset = df_records

            dict_records = df_records_subset.to_dict('index')

    rendering_dict = {'talent_records': dict_records}
    rendering_dict.update({'form':form})
    return render(request,'talent_info_app/talent_list.html', context=rendering_dict)


def info_input(request):

    form = forms.FormInfo()

    if request.method == 'POST':
        form = forms.FormInfo(request.POST)

        if form.is_valid():
            # DO SOMETHING
            print("VALIDATION SUCCESS!")
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"ORGANISATION: {form.cleaned_data['organisation']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"SKILL: {form.cleaned_data['skill']}")
            print(f"SKILL LEVEL: {form.cleaned_data['skill_level']}")

    return render(request, 'talent_info_app/info_input.html',{'form':form})

    # return render(request, 'talent_info_app/index.html')
