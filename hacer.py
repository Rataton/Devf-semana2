# -*- encoding: utf-8 -*-

class Do(object):
	def __init__(self):
		print "==  Diálogos  =="

	def Say(self,str):
		print "- ", str

do = Do()

do.Say('Hi, master')