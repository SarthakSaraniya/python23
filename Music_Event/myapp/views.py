from django.shortcuts import render
from .models import User
import requests 
import random

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def track(request):
	return render(request,'track.html')

def blog(request):
	return render(request,'blog.html')

def single_blog(request):
	return render(request,'single-blog.html')

def elements(request):
	return render(request,'elements.html')

def contact(request):
	return render(request,'contact.html')

def signup(request):
	if request.method == "POST":
		try :
			User.objects.get(email=request.POST['email'])
			msg = "Email Alredy Registered"
			return render(request,'login.html',{'msg': msg})
		except :
			if request.POST['password'] == request.POST['cpassword']:

				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
					)
				msg = "User Sign Up Successfully"
				return render(request,'login.html',{'msg': msg})
			else :
				msg = "Password & Confirm Dose Not Matched"
				return render(request,'signup.html',{'msg': msg})
	else :	
		return render(request,'signup.html')

def login(request):
	if request.method == 'POST':
		try :
			user = User.objects.get(email=request.POST['email'])
			if user.password == request.POST['password'] :
				request.session['email'] = user.email
				request.session['fname'] = user.fname
				return render(request,'index.html')
			else :
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not Registered"
			return render(request,'signup.html',{'msg':msg})

	else:
		return render(request,'login.html')

def logout(request):
	try :
		del request.session['email']
		del request.session['fname']
		msg = "Logout Successfilly"
		return render(request,'login.html',{'msg': msg})
	except:
		msg = "Logout Successfilly"
		return render(request,'login.html',{'msg':msg})

def change_password(request):
	if request.method == 'POST':
		user = User.objects.get(email=request.session['email'])
		if user.password == request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
					user.password=request.POST['new_password']
					user.save()
					msg = "Password changed Successfilly. Please login Again."
					del request.session['email']
					del request.session['fname']
					return render(request,'login.html',{'msg':msg})
			else :
				msg = "New Password & Confirm Password Dose not Matched"
				return render(request,'change-password.html',{'msg':msg})

		else :
			msg = "Old Password Dose not Matched"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			otp=str(random.randint(1000,9999))
			mobile=str(request.POST['mobile'])
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"xWPDfw1r8KTc6gyznUQ9VYqv35FJpLmS0dBlho2AXuCaZHEiNeli6TxgOIbPwftLyR2Kzu4ZqajSoe9h","variables_values":otp,"route":"otp","numbers":mobile}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.text)
			return render(request,'otp.html',{'otp':otp,'mobile':mobile})
		except:
			msg="mobile not registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	mobile=request.POST['mobile']

	if otp==uotp:
		return render(request,'new-password.html',{'mobile':mobile})
	else:
		msg="invalid OTP"
		return render(request,'otp.html',{'otp':otp,'mobile':mobile,'msg':msg})

def new_password(request):
	mobile=request.POST['mobile']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(mobile=mobile)
		user.password=np
		user.save()
		msg="Password Updated Successfilly"
		return render(request,'login.html',{'msg':msg})

	else:
		msg="New Password & Confirm New Password Dose not Matched"
		return render(request,'new-password.html',{'msg':msg,'mobile':mobile})