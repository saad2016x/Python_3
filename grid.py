import random
n = 20 # horizontal size of the map
m = 30 # vertical size of the map
the_map = []
row = [0] * n
for i in range(m): # create empty map
    the_map.append(list(row))

# fillout the map with a obstacle pattern
for row in range(n):
    r1=random.randint(0, n-1)

    the_map[row][r1] = 0
    
   
 
# for y in range(m/8, m * 7 / 8):
#    the_map[y][n / 2] = 1
#the_map[m / 2][n/2]=0
#the_map[m / 4][n/8]=0


print the_map
