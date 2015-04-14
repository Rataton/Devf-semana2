class Hacer(object):
	def __init__(self):
		print 'Mi tarea'
		print '--------------'
	def do1(self, str):
		'''Crear una funcion que reciba una cadena y repita cada caracter. Ejemplos de Entrada
		ddeevv..ff
		ppyytthhoonn
		'''
		print 'Ejercicio 1, string original: ', str, type(str)
		separado = list(str)
		for l in str:
			print '-', l

	def do2(self,serie):
		'''Crear una funcion que reciba una serie de numeros y regrese 
		la diferencia entre el numero mayor y el numero menor
		9'''
		print 'Ejercicio 2, serie original: ', serie, type(serie)
		minN = serie[0]
		maxN = 0
		for n in serie:
			if n>maxN:
				maxN = n
			if n<minN:
				minN = n
		print maxN, '-', minN, '=', maxN - minN
	def do3(self, serie):
		'''Dado un arreglo de enteros regresar True si contiene un 3 junto a un 3 en alguna parte'''
		print 'Ejercicio 2, serie original: ', serie, type(serie)
		i = 0
		prev = None
		next= None
		hay = len(serie)
		for n in serie:
			re = 'FALSE'
			ne = i + 1
			if ne<hay:
				next = serie[ne]
			else:
				next= None		
			i+=1

			if n == 3:
				if n == prev or n==next:
					re = 'TRUE'
			prev = n
			print re

	def do4(self, n):
		'''Hacer una funcion que regrese el factorial de un numero'''
		print 'Ejercicio 3, numero original: ', n, type(n)
		f = 1
		while n>1:
			f = f*n 
			n -= 1
			pass
		print f


ahorita = Hacer()
ahorita.do1('Parangaricutirimicuaro')
print ''
ahorita.do2([4,34,54,76,8,45,79,3,4])
print ''
ahorita.do3([4,34,54,54,3,45,76,87,5,3,3,56,3,56,89,6,53,3,6,4,3,76,8,45,79,3,4])
print ''
ahorita.do4(5)
print ''
