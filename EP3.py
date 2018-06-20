#!/usr/bin/env python3

#Define global variables
labirinth = []
_lab = []
entry_tile = {}
graded_tiles = {
	'unvisited': [],
	'visited': []
}

def readMatrix():
	while True:
		try:
			file_name = input('Entre com nome do arquivo com as matrizes: ')
			file = open(file_name, 'r')
		except:
			print('Erro na abertura do arquivo Matrizes.txt')
			continue
		i = 0
		for line in file:
			try:
				v = line.split()
				labirinth.append([])
				for j in range(len(v)):
					labirinth[i].append(int(v[j]))
				i +=1

			except Exception as err:
				print(err)
		print()
		print('Matriz labirinto com {} linhas por {} colunas'. format(len(labirinth), len(labirinth[0])))
		printLabirinth(labirinth)
		print('-----------------------------------------------------')
		return labirinth

def locateExits():
	global _lab
	global graded_tiles
	global entry_tile
	i = 0
	#loop throw the first line
	for tile in labirinth[0]:
		if(tile == 0):
			entry_tile = {'row': 0, 'col': i, 'val': 1}
			graded_tiles['unvisited'].append(entry_tile)
			_lab[0][i] = 1
			gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'])
			printResults()

			#Reset values to original, so it can calculate for other exits
			_lab = [i[:] for i in labirinth]
			graded_tiles = { 'unvisited': [], 'visited': [] }
		i += 1
	#check all first and last tile of middle rows
	else:
		i=1
		for row in labirinth[1:len(labirinth)-1]:
			j = 0
			for tile in row[::len(row)-1]:
				if(tile == 0):
					entry_tile = {'row': i, 'col':j, 'val': 1}
					graded_tiles['unvisited'].append(entry_tile)
					_lab[i][j] = 1
					gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'])
					printResults()

					#Reset values to original, so it can calculate for other exits
					_lab = [i[:] for i in labirinth]
					graded_tiles = { 'unvisited': [], 'visited': [] }
				j = len(row)-1
			i += 1
			#check last row for exists
		else:
			last_idx = len(labirinth)-1
			i= 0
			for tile in labirinth[last_idx]:
				if(tile == 0):
					entry_tile = {'row': last_idx, 'col': i, 'val': 1}
					graded_tiles['unvisited'].append(entry_tile)
					_lab[last_idx][i] = 1
					gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'])
					printResults()

					#Reset values to original, so it can calculate for other exits
					_lab = [i[:] for i in labirinth]
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
def gradeTiles(visited, unvisited):	
	for tile in unvisited:
		addAdjacentToUnvisited(tile)
	else:
		if len(graded_tiles['unvisited']):
			gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'])
	
def addAdjacentToUnvisited(tile):
	tile_idx = getTileIndex(tile, graded_tiles['unvisited'])
	if(tile_idx == -1): #tile not in the list
		return
	else:
		try:
			_lab[tile['row'] - 1][tile['col']]
		except Exception as err:
			#print(err)
			pass
		else:
			up = {'row': tile['row'] - 1, 'col': tile['col'] , 'val': _lab[tile['row'] - 1][tile['col']]}
			if(up['val'] == 0 and isTileInsideMatrix(up) and getTileIndex(up, graded_tiles['unvisited']) == -1 and getTileIndex(up, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				up['val'] = tile['val'] + 1
				_lab[tile['row'] - 1][tile['col']] = up['val']
				graded_tiles['unvisited'].append(up)
		try:
			_lab[tile['row'] + 1][tile['col']]
		except Exception as err:
			#print(err)
			pass
		else:
			down = {'row': tile['row'] + 1, 'col': tile['col'] , 'val': _lab[tile['row'] + 1][tile['col']]}
			if(down['val'] == 0 and isTileInsideMatrix(down) and getTileIndex(down, graded_tiles['unvisited']) == -1 and getTileIndex(down, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				down['val'] = tile['val'] + 1
				_lab[tile['row'] + 1][tile['col']] = down['val']
				graded_tiles['unvisited'].append(down)
		try:
			_lab[tile['row']][tile['col'] - 1]
		except Exception as err:
			#print(err)
			pass
		else:
			left = {'row': tile['row'], 'col': tile['col'] - 1, 'val': _lab[tile['row']][tile['col'] - 1]}
			if(left['val'] == 0 and isTileInsideMatrix(left) and getTileIndex(left, graded_tiles['unvisited']) == -1 and getTileIndex(left, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				left['val'] = tile['val'] + 1
				_lab[tile['row']][tile['col'] - 1] = left['val']
				graded_tiles['unvisited'].append(left)
		try:
			_lab[tile['row']][tile['col'] + 1]
		except Exception as err:
			#print(err)
			pass
		else:
			right = {'row': tile['row'], 'col': tile['col'] + 1, 'val': _lab[tile['row']][tile['col'] + 1]}
			if(right['val'] == 0 and isTileInsideMatrix(right) and getTileIndex(right, graded_tiles['unvisited']) == -1 and getTileIndex(right, graded_tiles['visited']) == -1): #tile not graded, and is inside matrix, and is not in unvisited list
				right['val'] = tile['val'] + 1
				_lab[tile['row']][tile['col'] + 1] = right['val']
				graded_tiles['unvisited'].append(right)

		graded_tiles['visited'].append(tile)
		del graded_tiles['unvisited'][tile_idx]
		
def printLabirinth(lab):
	for row in lab:
		for tile in row:
			print('{:2d}'.format(tile), end = ' ')
		else:
			print()

def printResults():
	print('Porta [{},{}]'.format(entry_tile['row'], entry_tile['col']))
	print('Todos os possiveis caminhos até a porta [{},{}]'.format(entry_tile['row'], entry_tile['col']))
	printLabirinth(_lab)
	print()
	farthest_away_tile =  {'row': 0, 'col': 0, 'val': 0}
	for tile in graded_tiles['visited']:
		if tile['val'] > farthest_away_tile['val']:
			farthest_away_tile = tile
	print('Posição com caminho mais distante da porta: [{},{}]'.format(farthest_away_tile['row'], farthest_away_tile['col']))
	print('Posições sem caminho')
	i=0
	for row in _lab:
		j = 0
		for tile in row:
			if tile == 0:
				print('[{},{}]'.format(i,j))
			j += 1
		i+=1		
	print('-----------------------------------------------------')

readMatrix()
_lab = [i[:] for i in labirinth]
locateExits()

