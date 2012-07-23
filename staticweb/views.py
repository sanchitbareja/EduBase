from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.contrib import auth

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def index_home(request):
	return render_to_response('index_home.html',{},context_instance=RequestContext(request))