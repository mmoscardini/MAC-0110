#!/usr/bin/env python3

def setup():
	
	try:
		#file_name = input('Nome do arquivo com as matrizes: ')
		file = open('Matrizes.txt', 'r')
	except:
		print(f'Erro na abertura do arquivo {file_name}')
		return
	matriz = []
	i = 0
	for line in file:
		try:
			v = line.split()
			matriz.append([])
			for j in range(len(v)):
				matriz[i].append(int(v[j]))
				print("{:2d}".format(matriz[i][j]) , end=' ')
			i +=1
			print()

		except Exception as err:
			print(err)
	#print(matriz)
	return matriz

setup()