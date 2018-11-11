from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
# login
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢察輸入的欄位是否正確')
    else:
        login_form = LoginForm()

    return render(request, 'registration/login.html', locals())

# def register(request):
#     return render(request, 'analytics/register.html')

# def forgot_password(request):
# return render(request, 'analytics/forgot-password.html')
