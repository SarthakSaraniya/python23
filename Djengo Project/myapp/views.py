from django.shortcuts import render
from .models import Contact,User
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	if request.method == "POST" :
		Contact.objects.create(
				name = request.POST['name'],
				email = request.POST['email'],
				mobile = request.POST['mobile'],
				remarks = request.POST['remarks']
			)
		msg = "Contact Save Successfilly"
		contacts = Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts = Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'contacts':contacts})

def signup(request):
	if request.method == "POST":
		try :
			User.objects.get(email=request.POST['email'])
			msg = "Email Alredy Registered"
			return render(request,'signup.html',{'msg': msg})
		except :
			if request.POST['password'] == request.POST['cpassword']:

				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_picture=request.POST['profile_picture']
					)
				msg = "User Sign Up Successfully"
				return render(request,'signup.html',{'msg': msg})
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
				request.session['profile_picture'] = user.profile_picture.url
				return render(request,'index.html')
			else :
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not Registered"
			return render(request,'login.html',{'msg':msg})

	else:
		return render(request,'login.html')

def logout(request):
	try :
		del request.session['email']
		del request.session['fname']
		del request.session['profile_picture']
		msg = "Logout Successfilly"
		return render(request,'login.html',{'msg': msg})
	except:
		return render(request,'login.html')

def change_password(request):
	if request.method == 'POST':
		user = User.objects.get(email=request.session['email'])
		if user.password == request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				if user.password != request.POST['new_password'] :
					user.password=request.POST['new_password']
					user.save()
					msg = "Password changed Successfilly. Please login Again."
					del request.session['email']
					del request.session['fname']
					return render(request,'login.html',{'msg':msg})
				else:
					msg = "New Password Can't be your one of the Old Password"
					return render(request,'change-password.html',{'msg':msg})
			else :
				msg = "New Password & Confirm Password Dose not Matched"
				return render(request,'change-password.html',{'msg':msg})

		else :
			msg = "Old Password Dose not Matched"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')

def forgot_password(request):
	if request.method=="POST" :
		try :
			user = User.objects.get(email=request.POST['email'])
			otp = random.randint(1000,9999)
			subject = 'OTP for Forgot Password'
			message = 'Hello'+user.fname+',Ypur OTP for Forgot Password is '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'email':user.email,'otp':otp})
		except:
			msg = "Email Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})	
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	email=request.POST['email']
	otp = int(request.POST['otp'])
	uotp = int(request.POST['uotp'])

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg = "Invalid OTP"
		return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="Password Updated Successfilly"
		return render(request,'login.html',{'msg':msg})

	else:
		msg="New Password & Confirm New Password dose not Matched"
		return render(request,'new-password.html',{'email':email,'msg':msg})

def profile(request):
	user = User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_picture=request.FILES['profile_picture']
		except:
			pass
		user.save()
		msg="Profile Updated Successfilly"
		request.session['profile_picture']=user.profile_picture.url
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})