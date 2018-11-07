from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def search_kw(request):
    import json
    from pytrends.request import TrendReq

    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = []
    kw = request.POST['search_kw']
    kw_list = [kw]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='TH', gprop='')
    preload = json.loads(pytrends.interest_over_time().to_json(orient='table'))['data']
    # print(preload)
    with open("trends_data.json", 'w') as f:
        json.dump(preload, f)
    return HttpResponse(kw)


# def login(request):
# return render(request, 'analytics/login.html')

# def register(request):
#     return render(request, 'analytics/register.html')

# def forgot_password(request):
# return render(request, 'analytics/forgot-password.html')
