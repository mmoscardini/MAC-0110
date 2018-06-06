#!/usr/bin/env python3

#Define global variables
labirinth = []
_lab = []
exit_tile = {}
graded_tiles = {
	'unvisited': [],
	'visited': []
}

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
	_lab = labirinth
	return labirinth

def locateExits():
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
				up['val'] = tile['val'] + 1;
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
				down['val'] = tile['val'] + 1;
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
				left['val'] = tile['val'] + 1;
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
				right['val'] = tile['val'] + 1;
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
setup()
exit_tile = {'row': 0, 'col': 3, 'val': 1}
graded_tiles['unvisited'].append(exit_tile)
_lab = labirinth
_lab[0][3] = 1
printLabirinth(_lab)
print('-----------------------')
gradeTiles(graded_tiles['visited'], graded_tiles['unvisited'])
printLabirinth(_lab)

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


'''
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

'''