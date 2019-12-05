from django.shortcuts import render
from django.http import HttpResponse
from talent_info_app.models import Person
from talent_info_app import forms
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


def talent_list(request):
    # talent_list = Person.objects.order_by('name')
    # print(talent_list)
    # records_dict = {'talent_records':talent_list}
    # return render(request,'talent_info_app/talent_list.html', context=records_dict)

    df_records = pd.read_csv('talent_info.csv')
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
