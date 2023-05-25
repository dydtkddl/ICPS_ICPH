from django.shortcuts import render, redirect
import sympy as sy
from django.http import HttpResponse, JsonResponse
from . import compute
from .models import *
import json
import time
import datetime as dt
def home(request):
    return render(request, 'app/home.html')
def out_zero(a):
    if a == '':
        a=0
    return a
def service(request):
    json_ = json.loads(request.body)
    print(json_)
    a = float(out_zero(json_['A']))
    b = float(out_zero(json_['B']))
    c = float(out_zero(json_['C']))
    d = float(out_zero(json_['D']))
    mode = json_['mode']
    T_ = float(json_['T'])
    T0_ = float(json_['T0'])
    if mode == "icph":
        expr = compute.get_ICPH(a,b,c,d)
        value = compute.compute_ICPH(expr,T0_,T_)
    else:
        expr = compute.get_ICPS(a,b,c,d)        
        value = compute.compute_ICPS(expr,T0_, T_)
    value = float(value)
    return JsonResponse([{"value" : value}], safe=False)

def like(request):
    datelist = [like.today for like in Like.objects.all()]
    if  dt.datetime.strftime(dt.datetime.now(),'%Y%m%d') not in datelist:
        Like(like=0, today=dt.datetime.strftime(dt.datetime.now(),'%Y%m%d') ).save()
    
    like = Like.objects.filter(today = dt.datetime.strftime(dt.datetime.now(),'%Y%m%d'))[0]
    like.like +=1
    like.save()
    like_count_today = like.like
    like_count_allday = sum_list([like.like for like in Like.objects.all()])
    return JsonResponse([{"today_like":like_count_today, "all":like_count_allday}],safe=False)

def sum_list(l):
    sum = 0
    for i in l:
        sum +=i
    return sum