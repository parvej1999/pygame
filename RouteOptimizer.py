# writer Parvej khan
# Travelling salesman problem(TSP)
# Run the program and select some points on screen using mouse
# after selecting the points press "e" to execute TSP


import pygame
import os
import random
import time

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# color
white,  black,  success, blue  =  (255,  255,  255),  (255,  0,  0),  (0,  255,  0), (0, 0, 255)
blue,  black,  yellow,  purple  =  (0,  0,  255),  (0,  0,  0),  (255,  255,  0),  (255,  0,  255)

# Global
screen_dimension = height, width = 1300, 700
win = pygame.display.set_mode(screen_dimension)

# checks if User is clicking on only "black screen"
def valid_click(click_pos):
	if click_pos[1]>80:
		return True
	else:
		return False

# calculates the total distance of the path
def get_distance(points):
	total = 0
	for i in range(len(points)-1):
		total += ((points[i][0]-points[i+1][0])**2+(points[i][1]-points[i+1][1])**2)**0.5
	return total

# shuffles the element of different indexs of a list
def shuffle_idx(lst,idx1,idx2):
	temp = lst[idx1]
	lst[idx1] = lst[idx2]
	lst[idx2] = temp
	return lst

# draws the graph
def draw_graph(lst):
	# circles as vertex of graph
	for n in range(len(lst)): 
		pygame.draw.circle(win, white, lst[n], 10)

	# lines between each nodes/vertex
	for n in range(len(lst)-1):
		pygame.draw.line(win, purple, lst[n], lst[n+1], 3)

	# Animation lines between nodes
	for line in range(len(lst)):
		pygame.draw.line(win, blue, random.choice(lst), random.choice(lst))
		pygame.display.update()

# blits the text on the screen
def print_msg(font_name,msg,x,y,color,font_size):
	myfont = pygame.font.SysFont(font_name,font_size)
	text = myfont.render(msg,1,color)
	win.blit(text,(x,y))

# formats the time
def format_time(secs):
	sec = secs%60
	minute = sec//60
	hour = minute//60
	time = str(hour)+":"+str(minute)+":"+str(sec)
	return time


# main_loop
def main_loop():
	clock = pygame.time.Clock()
	FPS = 100  #Frames per second
	text_t = None
	text1 = "Select some points on the screen"
	text2 = "Press E to execute the Algo "
	text3 = "Maximum 11 points are recommended"
	clicked = False
	point_list, shortest_path, stop, execute, tsp = [], [], False, False, False
	while not stop:
		win.fill(black)
		rect=pygame.draw.rect(win,(200,200,200),(0,0,1300,80))
		if not clicked:
			print_msg("times new roman",text1,10,5,black,30)

		elif clicked and not execute:
			print_msg("times new roman",text2+text3,10,5,black,30)
			# print_msg("times new roman",text3,10,40,black,30)

		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				stop = True

			elif event.type == pygame.MOUSEBUTTONUP:
				if not execute:
					pos = pygame.mouse.get_pos()
					if valid_click(pos):
						point_list.append(pos)
						clicked = True					
	
			elif event.type == pygame.KEYDOWN and not execute:
				if event.key == pygame.K_e:
					execute = True
					tsp = True
				

		# Execute TSP Press e
		if tsp:
			start = time.time()

		if execute:
			execution_time  = round(time.time()-start)
			text_t = format_time(execution_time)
			print_msg("times new roman", "Time: "+text_t, 10, 5, black, 30)
			if tsp:
				initial_distance = get_distance(point_list)
				shortest_path = point_list
				tsp = False
			index1 = random.randint(0, len(point_list)-1)
			index2 = random.randint(0, len(point_list)-1)
			shortest_path = shuffle_idx(shortest_path,index1,index2)
			new_distance = get_distance(shortest_path)
			
			if new_distance < initial_distance:
				initial_distance = new_distance
				point_list = shortest_path.copy()
				print("New shortest path= ",point_list)
		text_path="shortest path"+str(point_list)
		print_msg("times new roman",text_path,10,35,black,20)
		draw_graph(point_list)
		pygame.display.update()
	
main_loop()
time.sleep(10)
pygame.quit()
