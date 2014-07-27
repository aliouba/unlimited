#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
	url(r'^newclient/$', 'first.views.add_client', name='add_client'),
    
) 
