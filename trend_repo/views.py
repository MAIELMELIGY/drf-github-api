from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

#from .data import  get_trend_repo 
from . import repo_data
from rest_framework.decorators import api_view
 

@api_view(['GET', 'POST'])
def data_repo(request):
    if request.method == 'GET':
        repo = repo_data.final_repo
        return Response(repo)

@api_view(['GET', 'POST'])
def lang_data(request):
    if request.method == 'GET':
        num_langs =repo_data.final_lang 
        return Response(num_langs)
