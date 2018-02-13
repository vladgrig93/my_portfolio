from django.shortcuts import render, HttpResponse, redirect
from ..portfolio_app.models import *
from xml.etree import ElementTree
import requests
import json


def index(request):       
    return render(request, 'portfolio_app/home.html')
