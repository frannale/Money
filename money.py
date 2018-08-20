#import#
import json 
import pattern
import datetime
import os

#def#
def ingresar_gasto(datos_list):
	gasto=[]
	aux=int(input('\nMonto del gasto: '))
	gasto.append(aux)			
	aux=str(input('\nMotivo del gasto: '))
	gasto.append(aux)
	aux=datetime.datetime.now()
	gasto.append((aux.day,aux.month,aux.year))
	datos_list.append(gasto)
	return datos_list


def eliminar_gasto(datos_list):
	aux=input('Ingrese el numero de gasto a eliminar, -1 si quiere eliminar el ultimo: ')
	aux= int(aux)
	if aux == -1 :
		del datos_list[aux]
	else:
		del datos_list[aux-1]


def consultar(gastos_list):
	i=1
	for el in gastos_list:
		print('Gasto N`',i,': \n Monto: ',el[0],'\n Motivo: ',el[1],'\n Dia: ',el[2])
		i+=1
	print('--------------------------------------------------------------------\nTotal Gastado: ',sum(list(map(lambda x: x[0],gastos_list))))	


def cerrar_mes(datos_list):
	f_mes= open('meses.txt', 'r')
	lista_meses= json.load(f_mes)
	f.close()
	lista_meses.append(datos_list)
	f_mes= open('meses.txt', 'w')
	json.dump(lista_meses,f_mes)
	f.close()
	print('Mes cerrado correctamente!\n')
	consultar(datos_list)
	
	
def consulta_meses():
	f_mes= open('meses.txt', 'r')
	lista_meses= json.load(f_mes)
	f.close()
	print('\n*******************************************')
	for el in lista_meses:
		consultar(el)
		print('\n*******************************************')

#setup#
f=open('gastosmes.txt', 'r')
datos_list=json.load(f)
f.close()
# ~ datos_list=[]
#The Code#
while True:
	os.system('cls')
	print('A- Ingresar gasto')
	print('B- Consultar mes actual')
	print('C- Cerrar mes')
	print('D- Eliminar Gasto')
	print('E- Consulta meses')
	op=str(input('\n Ingrese opcion: '))
	op=op.upper()
	if op == 'A':
		ingresar_gasto(datos_list)
	elif op == 'B':
		consultar(datos_list)
	elif op == 'C':
		cerrar_mes(datos_list)
		datos_list=[]
	elif op == 'D':
		eliminar_gasto(datos_list)
	elif op == 'E':
		consulta_meses()		
	else:
		print('\nNo ha elegido ninguna opcion')
	op=input('\nPresione enter para seguir usando o  ingrese z para guardar cambios y cerrar: ')
	op=op.upper()
	if op == 'Z':
		break
f=open('gastosmes.txt', 'w')
json.dump(datos_list,f)	
f.close()	
