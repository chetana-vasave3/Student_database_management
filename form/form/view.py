from django.http import HttpResponse
from saveform.models import stdent_data,attendence
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from datetime import datetime

from django.shortcuts import render
def saveinquery(request):
    #return HttpResponse("welcome")
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        joining_date=request.POST.get("joiningdate")
        joining_date = datetime.strptime(joining_date, "%Y-%m-%d").date()
        
     
        

        course=request.POST.get("course")
        roll_no=request.POST.get("rollno")
        duration=request.POST.get("duration")
        
        topic=request.POST.get("topic")
        Date=request.POST.get("topic_date")
        intime=request.POST.get("intime")
        outtime=request.POST.get("outtime")
        table1=stdent_data(name=name,email=email,joining_date=joining_date,course=course,roll_no=roll_no,duration=duration)#get data
        table1.save()#save data
        table2=attendence(topic=topic,Date=Date,intime=intime,outtime=outtime,message=message)
        table2.save()
        
        
        
    return render(request,"inquiryform.html")
#def homepage(request):
    #'subject here',
    #'Here is the message',
    #'from@example.com',
   # ['to@example.com'],
    #fail_silently=False
   # send_mail('Testing mail',
    #'Here is the message',
    #'Welcome to IPCS',
    #['chetanavasave3@gmail.com'],
    #fail_silently=False,)
   # return render(request,"inquiryform.html")
   
  # subject="Testing mail"
  # from_email="vasavechetana5@gmail.com"
  # msg="<p>welcome to <b>IPCS</b></p>"
  # to="chetanavasave3@gmail.com"
  # msg=EmailMultiAlternatives(subject,msg,from_email,[to])
  # msg.content_subtype="html"
  # msg.send()
 #  return render(request,"inquiryform.html")