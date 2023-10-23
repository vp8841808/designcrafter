import uuid
from django import views
import os
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect,render ,get_object_or_404
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from .models import Newuser
import logging
logging.basicConfig(filename='logs.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def index(request):
    return HttpResponse('Hello there designer!!!')

def registration(request):
    return render (request,'registration/reg_1.html')

def sendotp(request, length=6):
    if request.method == 'POST':
        user_names = request.POST['User']
        user_emails = request.POST['email']
        user_passwords = request.POST['password']

        try:
            #to verfy if user already exists
            username1 = Newuser.objects.get( user_email = user_emails)
            return HttpResponse ("User already exists") 
        except:               
            characters = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
            digits = ''.join(random.choice(string.digits) for _ in range(2))
            gen_otp = characters + digits

            listotp = list(gen_otp)
            random.shuffle(listotp)
            slist = ''.join(listotp)

            otp = slist

            user1 = Newuser(user_name=user_names, user_email=user_emails, user_otp=otp,password = user_passwords)
            user1.save()

            # subject = 'Hello, Django Email'
            # message = f'This is a test otp sent from designcrafter. Your OTP is {otp}'
            # from_email = settings.EMAIL_HOST_USER
            # recipient_list = {user_emails}

            # send_mail(subject, message, from_email, recipient_list)
            logging.info("otp sent successfully")
            # Redirect to the login page or provide a success message
            return redirect('/user_login') 


def user_login(request,):
    return render (request,'login/user_login.html')


def verify_otp(request):
    if request.method == 'POST':
        us = request.POST['email']
        ps = request.POST['otp']
        try:
            user = Newuser.objects.get(user_email=us)
        except Newuser.DoesNotExist:
            user = "none"

        if user!="none":
           if user.user_otp == ps :
                user.user_otp = "used"
                user.save()
                return HttpResponse('Login Success')
           else:
               return HttpResponse('OTP Does not meet')
        else:
            return HttpResponse('Email id is Wrong')
        # return HttpResponse(user)
    #     try:
    #         user = Newuser.objects.get(user_email=us)
            
    #     except Newuser.DoesNotExist:
    #         user = None

    #     if user is None:
    #         if user.user_otp == ps:
    #             # login(request ,user) 
    #             ###otp delete
    #             user.user_otp = None
    #             user.save()
    #             return HttpResponse('Welcome')
    #         else:
    #             return HttpResponse('OTP is Wrong')
    #     else:
    #         return HttpResponse('User Not Found')
    
    # return redirect('/user_login')

def userlogin_page(request):
    return render(request,'login/userlogin1.html')

def userlogin(request):
    if request.method =='POST':
        us = request.POST['email']
        ps = request.POST['password']

        try:
            user = Newuser.objects.get(user_email=us)
            user_id = user.id
            user_name = user.user_name
            user_email = user.user_email
            ######
            request.session['user_id'] = user_id
            request.session['user_name'] = user_name
            request.session['user_email'] = user_email
        except ObjectDoesNotExist:
            user = None
        if user is not None:
            if user.password==ps:
            
                return redirect ('/user_session')
            else:
                return HttpResponse('Password is Wrong')
        else:
            return HttpResponse('user Not Found')

def user_session(request):
    user_id = request.session.get('user_id',None)
    user_name = request.session.get('user_name',None)
    user_email = request.session.get('user_email',None)

    return render(request,'session/user_session.html',{'user_id':user_id,'user_name':user_name,'user_email':user_email})

def dashboard(request):
    return render (request,"index.html")

def desgignuploadpage(request):
    return render (request,'admin/designsextend.html')

def designupload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        unique_filename = str(uuid.uuid4()) + ".png"


        file_path = os.path.join(settings.STATIC_ROOT, 'images/designs/' ,unique_filename)
        if not os.path.exists(file_path):
         os.makedirs(file_path)
        with open(file_path, 'wb') as destination_file:
            for chunk in uploaded_file.chunks():
                destination_file.write(chunk)
        
        return HttpResponse("File uploaded successfully.")
            