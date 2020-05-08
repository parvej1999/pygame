import pygame
import os
import random
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# color
white,  black,  success, blue  =  (255,  255,  255),  (255,  0,  0),  (0,  255,  0), (0, 0, 255)
blue,  black,  yellow,  purple  =  (0,  0,  255),  (0,  0,  0),  (255,  255,  0),  (255,  0,  255)

# Global
screen_offset = 50
screen_dimension = height, width = 1300, 700
wn = pygame.display.set_mode(screen_dimension)

# display text
wn.blit(wn, (10, 20))
pygame.display.update()

def get_distance(points):
	total = 0
	for i in range(len(points)-1):
		total += ((points[i][0]-points[i+1][0])**2+(points[i][1]-points[i+1][1])**2)**0.5
	return total

def shuffle_idx(lst,idx1,idx2):
	temp = lst[idx1]
	lst[idx1] = lst[idx2]
	lst[idx2] = temp

def draw_graph(lst):
	# circles as vertex of graph
	for n in range(len(lst)): 
		pygame.draw.circle(wn, white, lst[n], 10)
	# lines between nodes/vertex
	for n in range(len(lst)-1):
		pygame.draw.line(wn, success, lst[n], lst[n+1], 3)

	for line in range(len(lst)):
		pygame.draw.line(wn, blue, random.choice(lst), random.choice(lst))
		pygame.display.update()


# main loop
def main():
	clock = pygame.time.Clock()
	FPS = 100  #Frames per second
	point_list, shortest_path, stop, execute, tsp = [], [], False, False, False
	while not stop:
		wn.fill(black)
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				stop = True
			if event.type == pygame.MOUSEBUTTONUP:
				if not execute:
					pos = pygame.mouse.get_pos()
					point_list.append(pos)
				# draw = True
			if event.type == pygame.KEYDOWN and not execute:
				if event.key == pygame.K_e:
					execute = True
					tsp = True
					# print(tsp)
				if event.key == pygame.K_ESCAPE:
					stop = True
		# Execute TSP
		if execute:
			if tsp:
				initial_distance = get_distance(point_list)
				shortest_path = point_list
				tsp = False
			index1 = random.randint(0, len(point_list)-1)
			index2 = random.randint(0, len(point_list)-1)
			shuffle_idx(shortest_path,index1,index2)
			new_distance = get_distance(shortest_path)
			if new_distance<initial_distance:
				initial_distance = new_distance
				point_list = shortest_path.copy()
				print("New shortest path= ",point_list)

		draw_graph(point_list)
		pygame.display.update()
	
main()
pygame.quit()
