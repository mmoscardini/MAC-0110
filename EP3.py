#!/usr/bin/env python3

#Define global variables
labirinth = []
entry_tile = {}
exit_tile = {}
graded_tiles = {}
ppp = 0

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
			entry_tile.update({'row': 0, 'col': k, 'val': 0})
			break
	else:
		labirinth[0][0] = 0;
		entry_tile.update({'row': 0, 'col': 0, 'val': 0})
		print('Nenhuma porta de entrada encontrada...')
		print('Plantando explosivos...')
		print('Porta criada na posição (0, 0)')
		


	i = len(labirinth) -1
	for j in range(len(labirinth[i])):
		if(labirinth[i][j] == 0):
			exit_tile.update({'row': i, 'col': j, 'val': 0})
	else:
		#possibilidade de criar uma porta em uma posição aleatória
		exit_tile.update({'row': len(labirinth)-1, 'col': len(labirinth[len(labirinth)-1])-1, 'val': 0})
		print(exit_tile)
		labirinth[exit_tile['row']][exit_tile['col']] = 0;
		print('Nenhuma porta de saída encontrada...')
		print('Plantando explosivos...')
		print('Porta criada na posição ({}, {})'.format(exit_tile['row'], exit_tile['col']))
		

'''
	Função que numero os tiles de acordo com sua distância da saída
'''
def gradeTiles():	
	print
	def verifyAdjacents(item): #item contains row, col, val
		try:
			if((item['row'] - 1) < 0): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			else:
				up = {'row': item['row'] - 1, 'col': item['col'], 'val': labirinth[item['row'] - 1][item['col']]+1}
				if(up['val'] != -1 and up['val'] >= item['val']):
					graded_tiles.update({len(graded_tiles): up})
		except Exception as err:
			#this will deal with index out of range err
			#print('err1', err)
			pass
		try:
			if(item['row'] + 1 >= len(labirinth)): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			else:
				down = {'row': item['row'] + 1, 'col': item['col'], 'val': labirinth[item['row'] + 1][item['col']]+1}
				if(down['val'] != -1 and down['val'] >= item['val']):
					graded_tiles.update({len(graded_tiles): down})
		except Exception as err:
			#this will deal with index out of range err
			#print('err2', err)
			pass	
		try:
			if(item['col'] - 1 < 0): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			else:
				left = {'row': item['row'], 'col': item['col'] - 1, 'val': labirinth[item['row']][item['col'] - 1]+1}
				if(left['val'] != -1 and left['val'] >= item['val']):
					graded_tiles.update({len(graded_tiles): left})
		except Exception as err:
			#this will deal with index out of range err
			#print('err3', err)
			pass
		try:
			if(item['col'] + 1 >= len(labirinth[item['row']-1])): 
				#raize exception to stop python from reading list backwards
				raise Exception('index out of range')
			else:
				right = {'row': item['row'], 'col': item['col'] + 1, 'val': labirinth[item['row']][item['col'] + 1]+1}
				if(right['val'] != -1 and right['val'] >= item['val']):
					graded_tiles.update({len(graded_tiles): right})
		except Exception as err:
			#this will deal with index out of range err
			#print('err4', err)
			pass

		print('1',item)
		if(item['row'] == exit_tile['row'] and item['col'] == exit_tile['col']):
			return True
		else: 
			global ppp
			ppp += 1
			return False
		#end  verifyAdjacents


	if(len(graded_tiles) == 0):
		print('start')
		verifyAdjacents(entry_tile)
		gradeTiles()
	else:
		print(graded_tiles)
		var g = graded_tiles
		for i in graded_tiles: 
			if ppp > 50: break
			print(graded_tiles[i])
			input()
			exit_found = verifyAdjacents(graded_tiles[i])
			if(exit_found): break
		else:
			print('exit was found')
	print('graded_tiles: ', graded_tiles)
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
gradeTiles()

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