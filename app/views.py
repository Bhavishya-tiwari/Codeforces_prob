import imp
from urllib import request
from django import http
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect
import json
import datetime 
import requests
from datetime import date, datetime
from django.contrib import messages
import os
from django.utils import timezone
from pathlib import Path


def home(request):

    return render(request, 'app/home.html')
def resp(request, inff ):
    inff = inff-1
    ff = requests.get('https://codeforces.com/api/contest.list').json()
    lnk=[]
    cnt=0
    st = inff*50
    en = (inff+1)*50 -1
    # for f in ff["result"]:
    for f in range(st,en):
        if "Div. 2" in ff["result"][f]["name"] and ff["result"][f]["relativeTimeSeconds"]>0:
                
            o={
                    "name":ff["result"][f]["name"],
                    "id":ff["result"][f]["id"],
                    "f":f,
                }
            lnk.append(o)


            cnt = cnt+1
        if cnt==50:
                break
    print(lnk)
    return render(request, 'app/resp.html', {"dd":lnk})


