from django.shortcuts import render
from django.http import HttpResponse
from urlparse import parse_qs
"""
def index(request):
	output = '\nGET:'
	get_values = parse_qs(request.META['QUERY_STRING'])	
	for val in get_values:
		output += '\n\t' + val + ' = ' + get_values[val][0]

	output = request.META['CONTENT_LENGTH']
	return HttpResponse(output)
"""


def index(request):
	output = '\nGET:'	
	for val in request.GET:
		output += '\n\t' + val + ' = ' + request.GET[val]

	output += '\nPOST:'
	
	for value in request.POST:
		output += value + request.POST[value]
	
	return HttpResponse(output)
