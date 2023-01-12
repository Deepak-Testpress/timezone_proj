from django.shortcuts import render, redirect
from django.utils import timezone
from backports.zoneinfo import ZoneInfo
from django.conf import settings
from .forms import TimeForm
import pytz


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('base')
    else:
        return render(request, 'home.html')

def base(request):
    return render(request, "base.html")
# def home(request):
# 
#         timezone = timezone
#         cookies = request.COOKIES
#         print(cookies)
#         timezone_session = cookies.get(settings.TIMEZONE_SESSION_ID)
#         if cookies.get(settings.TIMEZONE_SESSION_ID) == None:
#             print("cookie is none")
#             timezone.activate(ZoneInfo(settings.TIME_ZONE))
#         else:
#             print("cookie not none")
#             timezone.activate(ZoneInfo(timezone_session))

#         if request.method == "POST":
#             print("ullaa")
#             form = TimeForm(request.POST)
#             if form.is_valid():
#                 print("form is valid da")
#                 tzname = form.cleaned_data.get('timezone')
#                 print(tzname)
#                 timezone_session = cookies[settings.TIMEZONE_SESSION_ID] = tzname
#                 # timezone = timezone    
#                 print(cookies)

#                 timezone.activate(ZoneInfo(timezone_session))
#         else:
#             form = TimeForm()
            
#         return render(
#             request,
#             "home.html",
#             {"timezone": timezone, "form": form},
#         )


# def ok(request):
#     # request.session.set_test_cookie()
#     request.COOKIES["test"] = "okk"
#     if request.COOKIES["test"] == "okk":
#         print(">>>> TEST COOKIE WORKED!")

#     return render(request, "base.html")
