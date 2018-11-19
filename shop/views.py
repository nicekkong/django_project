from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def year_archive(request, year):
    print("%s"%year)
    return HttpResponse('{}년 입니다....'.format(year))