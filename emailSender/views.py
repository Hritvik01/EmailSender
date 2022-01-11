from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import smtplib
from email.mime.text import MIMEText

def hello(request):
    if request.method =="GET":
        return HttpResponse("Welcome to Email Sender")



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def mypage(request):
    if request.method == "POST":
        data = request.data
        name = data['name']
        return HttpResponse("HI {} ".format(name))
        


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def sendEmail(request):
    data = request.data
    to_email = data.get("to_email")
    subject = data.get("subject")
    body = data.get("body")
    if not to_email or not subject or not body:
        return HttpResponse("Missing Params")

    from_ = "sachincum10@gmail.com"
    pwd = "Sachin@1122"

    msg = MIMEText(body)
    msg["From"] = from_
    msg["To"] = to_email
    msg["Subject"] = subject


    # msg.attach(MIMEText(body,"html"))
    try:
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(from_,pwd)
        mailServer.sendmail(from_,to_email,msg.as_string())
        mailServer.close()
        return JsonResponse({"Success": "True" ,"Comments" :"Email has been sent!"})
    except Exception as e:
        return JsonResponse({"Success" : "False", "Comments" :
        "Email has not been sent!", "Error": "{}".format(str(e))})