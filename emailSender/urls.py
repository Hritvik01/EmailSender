from django.urls import path, include   
from emailSender.views import hello
from emailSender.views import mypage,sendEmail

urlpatterns = [
    path('index', hello, name="hello"),
    path('newpage', mypage, name="newpage"),
    path('sendEmail', sendEmail, name="sendEmail")
]

