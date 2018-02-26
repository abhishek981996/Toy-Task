# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# 
from django.db import models


class Cases(models.Model):

	caseTitle = models.CharField(max_length=10)
	DOJ = models.DateField()
	body = models.TextField()
	def __str__(self):
		return "{}, {}".format( self.DOJ, self.caseTitle)


class Mentions(models.Model):
	"""docstring for """
	caseId = models.ForeignKey(Cases, related_name = 'Cases1')
	mentions_of = models.ForeignKey(Cases, related_name = 'Cases2')


class MentionedIn(models.Model):
	caseId = models.ForeignKey(Cases, related_name='Cases3')
	mentioned_in = models.ForeignKey(Cases , related_name= 'Cases4')
