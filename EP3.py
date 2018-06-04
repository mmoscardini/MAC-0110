#!/usr/bin/env python3

#Define global variables
labirinth = []
entry_tile = {}
exit_tile = {}
graded_tiles = []

def setup():
	
	try:
		#file_name = input('Nome do arquivo com as matrizes: ')
		file = open('Matrizes.txt', 'r')
	except:
		print('Erro na abertura do arquivo Matrizes.txt')
		return
	i = 0
	for line in file:
		try:
			v = line.split()
			labirinth.append([])
			for j in range(len(v)):
				labirinth[i].append(int(v[j]))
				#print("{:2d}".format(labirinth[i][j]) , end=' ')
			i +=1
			#print()

		except Exception as err:
			print(err)
	#print(labirinth)
	return labirinth

'''
	Função criada para determinal qual o ponto de saída do labirinto
	Definições:
		- A entrada e saída é representada com o número zero
		- A entrada deve estar localizada na primeira linha da matriz
		- A saída deve estar localizada na ultima linha da matriz
		- A Entrada é sempre o primeiro zero da primeira linha
		- A saída é sempre o ultimo zero da ultima linha
'''
def locateEntryAndExit():
	for k in range(len(labirinth[0])):
		if(labirinth[0][k] == 0):
			entry_tile.update({'row': 0, 'col': k})
			break

	i = len(labirinth) -1
	for j in range(len(labirinth[i])):
		if(labirinth[i][j] == 0):
			exit_tile.update({'row': i, 'col': j})

'''
	Função que numero os tiles de acordo com sua distância da saída
'''
def gradeTiles(start, end):	
	print
	def verifyAdjacents(i,j):
		try:
			if(j-1 < 0): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			up = labirinth[i][j-1]
			if(up != -1):
				graded_tiles.append({'row': i,'col': j-1,'val': up+1})
		except Exception as err:
			#this will deal with index out of range err
			#print('err', err)
			pass
		try:
			if(j+1 > len(labirinth[i])): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			down = labirinth[i][j+1]
			if(down != -1):
				graded_tiles.append({'row': i,'col': j+1,'val': down+1})
		except Exception as err:
			#this will deal with index out of range err
			#print('err', err)
			pass	
		try:
			if(i-1 < 0): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			left = labirinth[i-1][j]
			if(left != -1):
				graded_tiles.append({'row': i-1,'col': j,'val': left+1})
		except Exception as err:
			#this will deal with index out of range err
			#print('err', err)
			pass
		try:
			if(i+1 > len(labirinth)): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			right = labirinth[i+1][j]
			if(right != -1):
				graded_tiles.append({'row': i+1,'col': j,'val': right+1})
		except Exception as err:
			#this will deal with index out of range err
			#print('err', err)
			pass

		if(i == end['row'] and j == end['col']):
			return True
		else: 
			return False
		print(graded_tiles)
		#end  verifyAdjacents

	if(len(graded_tiles) == 0):
		verifyAdjacents(start['row'], start['col'])
		gradeTiles(start, end)
	else:
		for item in graded_tiles: 
			exit_found = verifyAdjacents(item['row'], item['col'])
			print(exit_found)
	print(graded_tiles)
'''
	for row in labirinth:
		for tile in row:
			try:
				up = labirinth[i][j-1]
				if(up != -1 and graded_tiles['{} {}'.format(i, j)]):
					graded_tiles.update({'{} {}'.format(i, j): {'row': i,'col': j,'val': up+1}})
			except Exception as err:
				#this will deal with index out of range err
				pass
			try:
				down = labirinth[i][j+1]
				if(down != -1):
					graded_tiles.update({'{} {}'.format(i, j): {'row': i,'col': j,'val': down+1}})
			except Exception as err:
				#this will deal with index out of range err
				pass	
			try:
				left = labirinth[i-1][j]
				if(left != -1):
					graded_tiles.update({'{} {}'.format(i, j): {'row': i,'col': j,'val': left+1}})
			except Exception as err:
				#this will deal with index out of range err
				pass
			try:
				right = labirinth[i+1][j]
				if(right != -1):
					graded_tiles.update({'{} {}'.format(i, j): {'row': i,'col': j,'val': right+1}})
			except Exception as err:
				#this will deal with index out of range err
				pass
'''

setup()
locateEntryAndExit()
gradeTiles(entry_tile, exit_tile)

'''
	Se graded_tiles for vazio:
		Leia o tile inicial (descobrir os dois index)
		adicionar os 4 tiles ao redor no dict graded_tiles
	else:
		for tile in graded_tiles
			adicionar os 4 tiles ao redor no dict graded_tiles
			if (tile === final) stop. Cheguei ao resultado return graded_tiles

	criar funççao para imprimir o graded_tiles
'''