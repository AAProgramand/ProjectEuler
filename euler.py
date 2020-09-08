#https://projecteuler.net

def multiplos(maximo, multiplo1, multiplo2):
	caja = sum(i for i in range(maximo) if (i % multiplo1 ==0 or i % multiplo2==0))
	return (caja)

def fibonacci(maximo):
	box, x, y = 0,1,2
	while x <= maximo:
		if x%2==0:
			box +=x
		x,y = y, x+y

	print(box)

"""
#¿Y si no sólo son pares?
def fibonacci(maximo, typeofnumber):
	if typeofnumber == "even":
		box, x, y = 0,1,2
			while x <= maximo:
				if x%2==0:
					box +=x
				x,y = y, x+y

			print(box)

	elif typeofnumber =="odd":
		box, x, y = 0,1,2
			while x <= maximo:
				if x%2!=0:
					box +=x
				x,y = y, x+y

			print(box)
"""












def soluciones(problema):
	path = "https://github.com/milioe/Project_euler/blob/master/{number}_overview.pdf"
	complete = path.format(number=problema)
	print(complete)





