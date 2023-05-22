from django.shortcuts import render, redirect
import sympy as sy
from django.http import HttpResponse, JsonResponse
from . import compute
import json
def home(request):
    return render(request, 'app/home.html')
def service(request):
    json_ = json.loads(request.body)
    print(json_)
    a = float(json_['A'])
    b = float(json_['B'])
    c = float(json_['C'])
    d = float(json_['D'])
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

    