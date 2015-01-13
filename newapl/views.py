from django.shortcuts import render
from django.http import HttpResponse
from urlparse import parse_qs
from django.template import loader, RequestContext, Context
from django.db import models
from newapl.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

"""
def index(request):
	output = '\nGET:'
	get_values = parse_qs(request.META['QUERY_STRING'])	
	for val in get_values:
		output += '\n\t' + val + ' = ' + get_values[val][0]

	output = request.META['CONTENT_LENGTH']
	return HttpResponse(output)
"""

"""
def index(request):
	output = '\nGETsdf:'	
	for val in request.GET:
		output += '\n\t' + val + ' = ' + request.GET[val]

	output += '\nPOST:'
	
	for value in request.POST:
		output += value + request.POST[value]
	
	return HttpResponse(output)
"""
def index(request):
	title = Question.objects.prefetch_related('author','tags').order_by('date_added').annotate(Count('answer'))
	paginator = Paginator(title,3)
	page = request.GET.get('page')
	try:
		question_list = paginator.page(page)
	except PageNotAnInteger:
		question_list = paginator.page(1)
	except EmptyPage:
		question_list = paginator.page(paginator.num_pages)
	return render(request,'index.html',{"question_list":question_list})

def login(req):
	return render(req,'login.html')

def signup(req):
	return render(req,'signup.html')

def register(req):
	return render(req,'register.html')

def question(req, question_id):
	#tag = Tag.objects.prefetch_related('tags').get(pk=question_id)
	q = Question.objects.get(id=question_id)
	answer_list = Answer.objects.all().filter(question=question_id).select_related()
	return render(req,'question.html',{"answer_list":answer_list,"q":q})