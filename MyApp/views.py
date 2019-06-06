from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.http import HttpResponse
import json,requests
from subprocess import Popen, PIPE, STDOUT
from requests_html import HTML,HTMLSession
from django.urls import path

# Create your views here.



def ScrapyStages():

    session = HTMLSession()
    dataStages = []
    linkScrap = 'https://www.offres-emploi.ma/stage.mc' #+pagenbr
    r = session.get(linkScrap)
    articles = r.html.find('.offre-content')
    for article in articles:
        try:
            print('*************Article-Title************************')
            titlearticle=article.find('h2 a',first=True).text
            print()
            print('Title : '+titlearticle)
            print()
            print('*************Article-POST-SUMMARY************************')
            articleSummary = article.find('p',first=True).text
            print(articleSummary)
            print()
            print('*************Article-Date************************')
            articleDate = article.find('.job-meta .job-date',first=True).text
            print(articleDate)
            print()
            print('*************Article-City************************')
            articleCity = article.find('.job-meta .job-location',first=True).text
            print(articleCity)
            print()
            print('*************Article-WebSite************************')
            articleWebsite = article.find('.job-meta .job-company',first=True).text
            print(articleWebsite)
            print()
            print('*************Article-URL************************')
            linkarticle =article.find('h2 a',first=True).attrs['href']
            print(linkarticle)
            print()

            print('*************Article-INFO-DETAILS************************')
            a =session.get(linkarticle)
            articleDetails =a.html.find('.offre-content-detail',first=True).text
            print(articleDetails)

            print('*************Article-Apply-URL************************')
            articleApplyURL =a.html.find('.offre-content .applybtns .apply a',first=True).attrs['href']
            print(articleApplyURL)
            stages ={
            'Title' : titlearticle,
            'Summary' :articleSummary,
            'Date' : articleDate,
            'City' : articleCity,
            'Company' : articleWebsite,
            'PostURL' : linkarticle,
            'Details' : articleDetails,
            'ApplyURL' : articleApplyURL
            }
            dataStages.append(stages)
        except AttributeError:
            continue
    #with open('stage.json', 'w',encoding='utf-8') as json_file:
    json_file = json.dumps(dataStages,indent=4)
    #csv_file.close()
    print('********************JSON FILE*******************')
    return json_file
    #End Scrappy func
    #@csrf_exempt


@api_view(["GET"])
def ScrappyServiceStages(request):
        if request.method == 'GET':
            data = ScrapyStages()
            response = HttpResponse(data , 
            content_type='application/json', status=200)
            return response