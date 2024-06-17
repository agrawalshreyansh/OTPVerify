from django.http import HttpResponse
from django.shortcuts import render,redirect
from random import randint
import smtplib
import ssl
from email.message import EmailMessage

def register(request):
    return render(request, 'index.html')

def submit(request):
    if request.method=='POST':
        usermail=request.POST.get('email')
        print(usermail)

        email_sender = "contactcode.ag@gmail.com"
        email_pwd = "jjeb gqfz sdrp osxo"
        otp = randint(100000,1000000)
        
        subject = "OTP Verification"
        body = " Your otp for verification is: " + str(otp)
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = usermail
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(email_sender, email_pwd)
            smtp.sendmail(email_sender, usermail, em.as_string())

      #  ver_otp = int(input('Enter the 6 digit otp recieved on your email:'))

       # if ver_otp == otp :
        #    print("Verification Successful")
        #else :
         #   print("Please try again.")





        return render(request, 'index.html', {"OTP":otp})

        
    else :
        return redirect("Login")