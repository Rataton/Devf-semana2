#!/usr/bin/python

class Do (object):
	def __init__(self):
		print 'Inicia dialogo'

	def Say (self, que='Nada'):
		print '- ' , que

dialog = Do()

dialog.Say(' Hi master')
