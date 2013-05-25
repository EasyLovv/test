# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from UA.config import tabs, Choices
import datetime, UA, UA.forms

def home(request):
	u"""Домашня директорія. tabs - список (массив) всіх вкладок, 
	який береться з файлу config.py"""
	
	config = {'site_name': request.get_host()}
	config.update({'tabs' : tabs})
	return HttpResponse(render_to_response('page.html',config))

def get_data(request):
	u"""отримання інформації методом ajax"""

	config = {'site_name': request.get_host()}

	if  request.is_ajax() and request.GET and request.GET.__contains__('data'):
		if request.GET[u'data'] == u'tab1':
			return HttpResponse(render_to_response('nikon.html', config))

		elif request.GET[u'data'] == u'tab2':
			config.update(csrf(request))
			config.update({'form' : UA.forms.UserSelect().as_p()})
			config.update({'link' : 'file_user'})
			return HttpResponse(render_to_response('form.html', config))

		elif request.GET[u'data'] == u'tab3':
			config.update(csrf(request))
			print request.META['REMOTE_ADDR']
			form = UA.forms.FeedBack()
			form.fields['ip_addr'].initial = request.META['REMOTE_ADDR']
			config.update({'link' : 'feedback'})
			config.update({'form' : form.as_p()})
			return HttpResponse(render_to_response('form.html', config))

		if request.GET[u'data'] == u'MS':
			return HttpResponse(render_to_response('ms.html', config))

		return HttpResponse(request.GET['data'])

	else: return HttpResponse('bad')

def file_user(request):
	u"""Запив в файл вибраних користувачів та виведення файлу"""

	if request.POST and request.POST.__contains__('user'):
		message = '%s : %s select user %s\n' % (datetime.datetime.now(), request.META['REMOTE_ADDR'], Choices[request.POST['user']])
		open(UA.__path__[0]+'/user.info', 'a').write(message)
		return HttpResponseRedirect('/file_user')

	else:
		answer = ''

		for line in open(UA.__path__[0]+'/user.info', 'r').readlines():
			answer += line+'<br>'

		return HttpResponse(answer)

def feedback(request):
	u"""Зворотній зв'язок"""

	return HttpResponse('feedback')