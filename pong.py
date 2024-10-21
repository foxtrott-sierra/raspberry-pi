import pygame
import sys

pygame.init()

FPS =120
FramePerSecond = pygame.time.Clock()

pong_screen = pygame.display.set_mode((800,600))

class Ball:
    xPos = 0
    yPos = 0

    xDir = True
    yDir = True
    
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.xPos, self.yPos), 20)

    def move(self):
        if self.xDir:
            self.xPos += 2
        else:
            self.xPos -= 2

        if self.yDir:
            self.yPos += 2
        else:
            self.yPos -= 2

    def checkCollision(self, player1, player2, score):

        print(player1.yPos)

        if self.xPos == player1.xPos + 50:
            if self.yPos >= player1.yPos and self.yPos < player1.yPos + 150:
                self.xDir = True

        if self.xPos == player2.xPos - 20:
            if self.yPos >= player2.yPos and self.yPos < player2.yPos + 150:
                self.xDir = False

        if self.yPos < 20:
            self.yDir = True
        if self.yPos > 580:
            self.yDir = False

        if self.xPos < 0:
            score.counterP2 += 1
            self.xPos = 200
            self.yPos = 200
            self.xDir = True

        if self.xPos > 800:
            score.counterP1 += 1
            self.xPos = 600
            self.yPos = 200
            self.xDir = False

class Playerbrick:

    xPos = 0
    yPos = 0

    up = False
    down = False

    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.xPos, self.yPos, 30, 150))

    def move(self):
        if self.down:
            if self.yPos < 440:
                self.yPos += 4
        if self.up:
            if self.yPos > 5:
                self.yPos -= 4


class Score:
    counterP1 = 0
    counterP2 = 0

    def draw(self, screen):
        score_pl1 = pygame.font.SysFont("comicsansms", 40).render(str(self.counterP1), True, (255,255,255))
        score_pl2 = pygame.font.SysFont("comicsansms", 40).render(str(self.counterP2), True, (255,255,255))

        screen.blit(score_pl1, (screen.get_width() * 0.25, 70))
        screen.blit(score_pl2, (screen.get_width() * 0.75, 70))


ball = Ball(200,200)
player1 = Playerbrick(24,200)
player2 = Playerbrick(750,200)
score = Score()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player1.down = True
            if event.key == pygame.K_w:
                player1.up = True

            if event.key == pygame.K_DOWN:
                player2.down = True
            if event.key == pygame.K_UP:
                player2.up = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1.down = False
            if event.key == pygame.K_w:
                player1.up = False

            if event.key == pygame.K_DOWN:
                player2.down = False
            if event.key == pygame.K_UP:
                player2.up = False

    pong_screen.fill((0,0,0))
    for x in range(15):
        pygame.draw.rect(pong_screen, (255,255,255), (pong_screen.get_width() / 2, 50*x + 15, 20, 20))
    
    ball.draw(pong_screen)
    ball.checkCollision(player1, player2, score)
    ball.move()

    player1.draw(pong_screen)
    player1.move()
    player2.draw(pong_screen)
    player2.move()

    score.draw(pong_screen)

    FramePerSecond.tick(FPS)
    pygame.display.update()