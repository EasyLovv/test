# -*- coding: utf-8 -*-
from django import forms
from UA.config import Choices
import datetime
class UserSelect(forms.Form):
	u"""
	Вибір користувача (набір користувачів береться з файлу config.py)
	"""
	user = forms.ChoiceField(widget=forms.RadioSelect, choices = tuple(Choices.items()))
class FeedBack(forms.Form):
	u"""Клас форми для зворотнього зв'язку"""
	readonly_fields = ("date",'ip_addr')
	ip_addr = forms.IPAddressField(label = u'IP адреса')
	name = forms.CharField(label = u'Ім\'я')
	date = forms.DateField(label = u'Дата', initial=datetime.datetime.now())
	email = forms.EmailField(label = u'E-mail',)
	text = forms.CharField(widget=forms.Textarea(),label = u'Текст сообщения')
	def __init__(self, readonly_form=False, *args, **kwargs):
		super(FeedBack, self).__init__(*args, **kwargs)
		for field in self.readonly_fields:
			self.fields[field].widget.attrs['readonly'] = True