from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.contrib import auth

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Login and signup handles

def login(request):
	if request.method == 'GET':
		return render_to_response('accounts/login.html',{},context_instance=RequestContext(request))
	else:
		username = request.POST.get('username','')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			# Correct password, and the user is marked "active"
			auth.login(request, user)
			# Redirect to a success page.
			return HttpResponseRedirect("/courses/home/")
		else:
			# Show an error page
			return HttpResponseRedirect("/accounts/login/")    

def logout(request):
    auth.logout(request)
    # Redirect to a success page. - to redo and redirect to /account/loggedout/ instead
    return render_to_response('accounts/logout.html',{},context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
    return render_to_response("accounts/signup.html", {'form': form}, context_instance=RequestContext(request))
