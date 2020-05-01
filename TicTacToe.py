# writer=parvej khan
# Game=Tic Tac Toe

import pygame
pygame.init()

# screen dimensions
screen_dimension = 400, 400

# win = window
win = pygame.display.set_mode(screen_dimension)
pygame.display.set_caption("TIC TAC TOE")

# colors           
white, black, green = (255, 255, 255), (255, 0, 0), (0, 255, 0)
blue, black, yellow, purple = (0, 0, 255), (0, 0, 0), (255, 255, 0), (255, 0, 255)

# fonts
font = pygame.font.SysFont("arial", 65, True)
player1 = font.render("O", True, purple)
player2 = font.render("X", True, yellow)
winner_msg = [font.render("Player 1 is", True, purple), font.render("WINNER", True, purple), font.render("Player 2 is", True, purple)]
match_draw = font.render("Match Draw", True, yellow)

# functions
def delay_update(time):
	pygame.display.update()
	pygame.time.delay(time)

def player_height(cord):
	height = (cord-player1.get_height())/2, (cord-player2.get_height())/2
	return height

def player_width(cord):
	width = (cord-player1.get_width())/2, (cord-player2.get_width())/2
	return width

# Designing grid for game
def grid():
	global first, second, third, fourth, fifth, sixth, seventh, eighth, ninth
	# first row rectangles
	first = pygame.draw.rect(win, white, (25, 25, 100, 100))
	delay_update(100)
	second = pygame.draw.rect(win, white, (150, 25, 100, 100))
	delay_update(100)
	third = pygame.draw.rect(win, white, (275, 25, 100, 100))
	delay_update(100)

	# second row rectangles
	fourth = pygame.draw.rect(win, white, (25, 150, 100, 100))
	delay_update(100)
	fifth = pygame.draw.rect(win, white, (150, 150, 100, 100))
	delay_update(100)
	sixth = pygame.draw.rect(win, white, (275, 150, 100, 100))
	delay_update(100)

	# third row rectangles
	seventh = pygame.draw.rect(win, white, (25, 275, 100, 100))
	delay_update(100)
	eighth = pygame.draw.rect(win, white, (150, 275, 100, 100))
	delay_update(100)
	ninth = pygame.draw.rect(win, white, (275, 275, 100, 100))
	delay_update(100)
# ----------------Grid ends-------------------


# checking for winner
def check(num, lst):
	# for row in lst
	for row in lst:
		for item in row:
			if item == num:
				continue
			else:

				break
		else:
			return True

	# for columnns in lst
	for column in range(3):
		for item in range(3):
			if lst[item][column] == num:
				continue
			else:
				break
		else:
			return True

	#  for diagonal (0, 0), (1, 1), (2, 2)
	for index in range(3):
		if lst[index][index] == num:
			continue
		else:
			break
	else:
		return True

	#  for diagonal (0, 2), (1, 1), 2, 0 )
	for index in range(3):
		if lst[index][2-index] == num:
			continue
		else:
			break
	else:
		return True	

# funtion for playing game
chance = "p1"
won = False
pos_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
winner = 0
play_track = 0
def play():
	global chance, won, pos_list, winner, play_track
	
	if not won:
		pos = pygame.mouse.get_pos()
		if first.collidepoint(pos):
			pygame.draw.rect(win, black, (40, 40, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(150)[0], player_height(150)[0]))
				chance = "p2"
				pos_list[0][0] = 1
			else:
				win.blit(player2, (player_width(150)[1], player_height(150)[1]))
				chance = "p1"	
				pos_list[0][0] = 2

		if second.collidepoint(pos):
			pygame.draw.rect(win, black, (165, 40, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(400)[0], player_height(150)[0]))
				chance = "p2"
				pos_list[0][1] = 1
			else:
				win.blit(player2, (player_width(400)[1], player_height(150)[1]))
				chance = "p1"	
				pos_list[0][1] = 2	

		if third.collidepoint(pos):
			pygame.draw.rect(win, black, (290, 40, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(650)[0], player_height(150)[0]))
				chance = "p2"
				pos_list[0][2] = 1
			else:
				win.blit(player2, (player_width(650)[1], player_height(150)[1]))
				chance = "p1"
				pos_list[0][2] = 2	

		if fourth.collidepoint(pos):
			pygame.draw.rect(win, black, (40, 165, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(150)[0], player_height(400)[0]))
				chance = "p2"
				pos_list[1][0] = 1
			else:
				win.blit(player2, (player_width(150)[1], player_height(400)[1]))
				chance = "p1"	
				pos_list[1][0] = 2

		if fifth.collidepoint(pos):
			pygame.draw.rect(win, black, (165, 165, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(400)[0], player_height(400)[0]))
				chance = "p2"
				pos_list[1][1] = 1
			else:
				win.blit(player2, (player_width(400)[1], player_height(400)[1]))
				chance = "p1"
				pos_list[1][1] = 2

		if sixth.collidepoint(pos):
			pygame.draw.rect(win, black, (290, 165, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(650)[0], player_height(400)[0]))
				chance = "p2"
				pos_list[1][2] = 1
			else:
				win.blit(player2, (player_width(650)[1], player_height(400)[1]))
				chance = "p1"	
				pos_list[1][2] = 2

		if seventh.collidepoint(pos):
			pygame.draw.rect(win, black, (40, 290, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(150)[0], player_height(650)[0]))
				chance = "p2"
				pos_list[2][0] = 1
				
			else:
				win.blit(player2, (player_width(150)[1], player_height(650)[1]))
				chance = "p1"
				pos_list[2][0] = 2

		if eighth.collidepoint(pos):
			pygame.draw.rect(win, black, (165, 290, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(400)[0], player_height(650)[0]))
				chance = "p2"
				pos_list[2][1] = 1
			else:
				win.blit(player2, (player_width(400)[1], player_height(650)[1]))
				chance = "p1"
				pos_list[2][1] = 2

		if ninth.collidepoint(pos):
			pygame.draw.rect(win, black, (290, 290, 70, 70))
			if chance == "p1":
				win.blit(player1, (player_width(650)[0], player_height(650)[0]))
				chance = "p2"
				pos_list[2][2] = 1
			else:
				win.blit(player2, (player_width(650)[1], player_height(650)[1]))
				chance = "p1"	
				pos_list[2][2] = 2
		pygame.display.update()
		if check(1, pos_list):
			winner = 1
			won = True
		if check(2, pos_list):
			winner = 2
			won = True
		play_track +=  1

def declare_winner():
	global play_track, chance, pos_list
	
	if won == True:
		pygame.time.delay(1000)
		win.fill(white)
		if winner == 1:
				win.blit(winner_msg[0], ((400-winner_msg[0].get_width())/2, (300-winner_msg[0].get_height())/2))
				win.blit(winner_msg[1], ((400-winner_msg[1].get_width())/2, (450-winner_msg[1].get_height())/2))
		elif winner == 2:
			win.blit(winner_msg[2], ((400-winner_msg[0].get_width())/2, (300-winner_msg[2].get_height())/2))
			win.blit(winner_msg[1], ((400-winner_msg[1].get_width())/2, (450-winner_msg[1].get_height())/2))
		pygame.display.update()
		pygame.time.delay(2000)
		return True

	elif play_track == 9:
		win.fill(white)
		win.blit(match_draw, ((400-match_draw.get_width())/2, (400-match_draw.get_height())/2))
		pygame.display.update()
		pygame.time.delay(2000)
		return True
		
	
def main():
	won1 = False
	won2 = False
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				play()
				declare_winner()
				if declare_winner():
					try:
						pygame.quit()
					finally:
						raise SystemExit("----------GOOD BYE--------")
			
grid()
main()
pygame.quit()