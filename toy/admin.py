# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from toy.models import Cases,Mentions,MentionedIn
# Register your models here.
admin.site.register(Cases)
admin.site.register(Mentions)
admin.site.register(MentionedIn)