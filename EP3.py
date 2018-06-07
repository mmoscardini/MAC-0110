#!/usr/bin/env python3

import copy

#Define global variables
labirinth = []
_lab = []
exit_tile = {}
graded_tiles = {
	'unvisited': [],
	'visited': []
}

def readMatrix():
	
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
	return labirinth

def locateExits():
	global _lab
	global graded_tiles
	i = 0
	for tile in labirinth[0]:
		print(tile)
		if(tile == 0):
			print('ITS 0000')
			exit_tile = {'row': 0, 'col': i, 'val': 1}
			graded_tiles['unvisited'].append(exit_tile)
			_lab[0][i] = 1
			gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'], _lab[:])
			printLabirinth(_lab)
			print('-----------------------')
			_lab = copy.deepcopy(labirinth)
			graded_tiles = { 'unvisited': [], 'visited': [] }
		i += 1
def isTileInsideMatrix(tile):
	if(tile['row'] < 0): 
		return False
	if(tile['row']> len(labirinth)): 
		return False
	if(tile['col'] < 0): 
		return False
	if(tile['col'] > len(labirinth[tile['row']])): 
		return False
	return True

def getTileIndex(tile, list):
	try:
		tile['row'] 
		tile['col']
	except: 
		print('Tile informado não possui row ou col')
		return False

	i=-1
	for obj in list:
		i +=1
		try:
			obj['row'] 
			obj['col']
			obj['val']
		except: 
			del list[i]
			continue
		else:
			if(obj['row'] == tile['row'] and obj['col'] == tile['col']): #they are at the same position
				return i
	else: 
		return -1

'''
	Função que numero os tiles de acordo com sua distância da saída
'''
def gradeTiles(visited, unvisited, lab):	
	for tile in unvisited:
		addAdjacentToUnvisited(tile, lab)
	else:
		if len(graded_tiles['unvisited']):
			gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'], lab)
	
def addAdjacentToUnvisited(tile, lab):
	tile_idx = getTileIndex(tile, graded_tiles['unvisited'])
	if(tile_idx == -1): #tile not in the list
		return
	else:
		try:
			lab[tile['row'] - 1][tile['col']]
		except Exception as err:
			#print(err)
			pass
		else:
			up = {'row': tile['row'] - 1, 'col': tile['col'] , 'val': lab[tile['row'] - 1][tile['col']]}
			if(up['val'] == 0 and isTileInsideMatrix(up) and getTileIndex(up, graded_tiles['unvisited']) == -1 and getTileIndex(up, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				up['val'] = tile['val'] + 1;
				lab[tile['row'] - 1][tile['col']] = up['val']
				graded_tiles['unvisited'].append(up)
		try:
			lab[tile['row'] + 1][tile['col']]
		except Exception as err:
			#print(err)
			pass
		else:
			down = {'row': tile['row'] + 1, 'col': tile['col'] , 'val': lab[tile['row'] + 1][tile['col']]}
			if(down['val'] == 0 and isTileInsideMatrix(down) and getTileIndex(down, graded_tiles['unvisited']) == -1 and getTileIndex(down, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				down['val'] = tile['val'] + 1;
				lab[tile['row'] + 1][tile['col']] = down['val']
				graded_tiles['unvisited'].append(down)
		try:
			lab[tile['row']][tile['col'] - 1]
		except Exception as err:
			#print(err)
			pass
		else:
			left = {'row': tile['row'], 'col': tile['col'] - 1, 'val': lab[tile['row']][tile['col'] - 1]}
			if(left['val'] == 0 and isTileInsideMatrix(left) and getTileIndex(left, graded_tiles['unvisited']) == -1 and getTileIndex(left, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				left['val'] = tile['val'] + 1;
				lab[tile['row']][tile['col'] - 1] = left['val']
				graded_tiles['unvisited'].append(left)
		try:
			lab[tile['row']][tile['col'] + 1]
		except Exception as err:
			#print(err)
			pass
		else:
			right = {'row': tile['row'], 'col': tile['col'] + 1, 'val': lab[tile['row']][tile['col'] + 1]}
			if(right['val'] == 0 and isTileInsideMatrix(right) and getTileIndex(right, graded_tiles['unvisited']) == -1 and getTileIndex(right, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				right['val'] = tile['val'] + 1;
				lab[tile['row']][tile['col'] + 1] = right['val']
				graded_tiles['unvisited'].append(right)

		graded_tiles['visited'].append(tile)
		del graded_tiles['unvisited'][tile_idx]
		
def printLabirinth(lab):
	for row in lab:
		for tile in row:
			print('{:2d}'.format(tile), end = ' ')
		else:
			print()

readMatrix()
_lab = copy.deepcopy(labirinth)
locateExits()

