from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.contrib import auth

from django import forms
from django.http import HttpResponseRedirect

from courses.models import Course, Assessment

def courses_all(request):
	courses = Course.objects.all()
	assessments = Assessment.objects.all()
	return render_to_response('courses/all.html',{'courses':courses},context_instance=RequestContext(request))