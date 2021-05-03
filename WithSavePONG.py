import pygame
import sys
import random
import os

pygame.init()
Clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
init_score = pygame.font.SysFont(None, 64)
init_highscore = pygame.font.SysFont(None, 64)


file = open("data.txt", "r")
highscore = file.read()
file.close()
highscore = int(highscore)

def save(high_score):
    os.remove("data.txt")
    with open("data.txt", "w+") as data:
        data.write(str(high_score))
        data.close()


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG")

class Player:
    def __init__(self, player_width, player_height):
        self.player_width = player_width
        self.player_height = player_height
    def draw(self, x_pos, y_pos):
        pygame.draw.rect(screen, (255, 255, 255), (x_pos, y_pos, self.player_width, self.player_height))
class Ball:
    def __init__(self, size):
        self.size = size
    def draw(self, ball_x, ball_y):
        pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), self.size)


player_width = 350
player_height = 40
player = Player(player_width, player_height)
player_x = screen_width/2 - player_width/2
player_y = screen_height - player_height*3

enemy_x = screen_width/2 - player_width/2
enemy_y = 0 + player_height*3
enemy = Player(player_width, player_height)

ball = Ball(10)
ball_x = screen_width/2
ball_y = screen_height/2
ball_x_vel = random.choice([-2, 2])
ball_y_vel = random.choice([-2, 2])

score = 0

while True:
    screen.fill((7, 0, 59))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save(highscore)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save(highscore)
                pygame.quit()
                sys.exit()
    
    player.draw(player_x, player_y)
    mouse_x = pygame.mouse.get_pos()
    player_x = mouse_x[0] - player_width/2

    enemy.draw(enemy_x, enemy_y)
    enemy_x = ball_x - player_width/2

    ball_x += ball_x_vel
    ball_y += ball_y_vel
    ball.draw(ball_x, ball_y)

    if ball_x > screen_width:
        ball_x_vel *= -1

    if ball_x < 0:
        ball_x_vel *= -1

    if ball_y < 0:
        ball_y_vel *= -1 

    if ball_y > player_y + 5:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_x_vel = random.choice([-2, 2])
        ball_y_vel = random.choice([-2, 2])
        score = 0



    if ball_x > player_x and ball_x < player_x + player_width and ball_y > player_y:
        ball_y_vel *= -1
        score += 1

    if ball_x > enemy_x and ball_x < enemy_x + player_width and ball_y < enemy_y + player_height:
        ball_y_vel *= -1

    if score > highscore:
        highscore = score


    score_text = init_score.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (100, screen_height/2))

    high_score_text = init_highscore.render( "Highscore: " + str(highscore), True, (255, 255, 255))
    screen.blit(high_score_text, (100, screen_height/2 + 100))

    Clock.tick(360)
    pygame.display.update()
