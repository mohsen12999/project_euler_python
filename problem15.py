# https://projecteuler.net/problem=15
# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

max=6

def find_way(way,width,height,all_way):
	if width !=max:
		way.append('right')
		#print(width,'right',width,height)
		find_way(way,width+1,height,all_way)
	if height !=max:
		way.append('top')
		#print(height,'top',width,height)
		find_way(way,width,height+1,all_way)
	if width==max and height==max:
		all_way.append(way)
		#print(way)
		way=[]
	return all_way


allway = find_way([],0,0,[])
print('all_way',len(allway))

