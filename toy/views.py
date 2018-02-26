# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from toy.models import Cases,Mentions,MentionedIn
import json
import datetime
from django.http import JsonResponse


def Index(request):
	return render(request,"index.html")


def Data(request):
	""" Api build for sending Bubble data
	This Api is used to create bubble """
	cases = Cases.objects.all()
	data = []
	for case in cases:
		mentions = Mentions.objects.filter(caseId = case).count()
		date = datetime.datetime.strptime(str(case.DOJ), "%Y-%m-%d")
		year = date.year
		month = date.month
		data.append({'x':year,'y':month,'z':mentions,'name':case.caseTitle}) 

	return JsonResponse({'Success':data})


def MentionedIN(request):

	"""
	Build to draw line for mentionedIn
	this function returns below format json
	{ "Success":[
						//[
 						[axis],
					[
 							[95,95],[86.5,102.9],null,[95,95],[63.4,51.8],null
 						]
 				]
 				[
 						[axis],
 						[
 							[80.3,86.1],[78.4,70.1],null,[80.3,86.1],[65.5,126.4],null,[80.3,86.1],[64,82.9]
 						]
 				]
 			]
 			}

	"""
	cases = Cases.objects.all()
	data = []
	
	for case in cases:
		mentions = MentionedIn.objects.filter(caseId = case)
		date = datetime.datetime.strptime(str(case.DOJ), "%Y-%m-%d")
		k = []
		j=1
		axis = [date.year,date.month]
		for i in mentions:
			
			date1 = datetime.datetime.strptime(str(i.mentioned_in.DOJ), "%Y-%m-%d")
			point = [date1.year,date1.month]			
			k.append(axis)
			k.append(point)
			k.append(None)
			print(k)
		if mentions:
			data.append([axis,k])
			

	print(data)
	return JsonResponse({'Success':data})


def MinimumYear(request):
	"""
	Returns both minimum and maximum for floor and ceiling in xaxis
	"""
	cases = Cases.objects.all()
	year = []
	for case in cases:
		date = datetime.datetime.strptime(str(case.DOJ), "%Y-%m-%d")
		year.append(date.year)
	data = [sorted(year)[0],sorted(year)[-1]]
	return JsonResponse({'Success':data})







