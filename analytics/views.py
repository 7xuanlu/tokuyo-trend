from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, KWForm
# login
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def topic_massage(request):
    return render(request, "topic_massage.html")

def topic_fit(request):
    return render(request, "topic_fit.html")

def topic_rival(request):
    return render(request, "topic_rival.html")

def trend(request):
    return render(request, "trend.html")

def traffic(request):
    return render(request, "traffic.html")

@login_required
def search_kw(request):
    import json
    from pytrends.request import TrendReq

    pytrends = TrendReq(hl='en-US', tz=360)
    if request.method == 'POST':
        form = KWForm(request.POST)
        if form.is_valid():
            kw = form.cleaned_data["keyword"]
            request.session["keyword"] = kw
    else:
        kw = request.session["keyword"]
    kw_list = [kw]

    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='TH', gprop='')

    df = pytrends.interest_over_time()
    preload = json.loads(df.to_json(orient='table'))['data']

    return JsonResponse(preload, safe=False)  # safe defaults to python dict

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

def logout_view(request):
    logout(request)
    return redirect('/login')
