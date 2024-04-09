from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def rent_venue(request):
	return render(request,'rent-venue.html')

def shows_events(request):
	return render(request,'shows-events.html')

def tickets(request):
	return render(request,'tickets.html')

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
		del request.session['profile_picture']
		msg = "Logout Successfilly"
		return render(request,'login.html',{'msg': msg})
	except:
		msg = "Logout Successfilly"
		return render(request,'login.html',{'msg': msg})

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