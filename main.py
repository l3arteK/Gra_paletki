import time

import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(self, x, y, player):
        self.width = 40
        self.height = 300
        self.x_cord = x
        self.y_cord = y
        self.player = player

    def tick(self, KEYS):
        if self.player == 1:
            if KEYS[pygame.K_w] and self.y_cord > 0:
                self.y_cord -= 10
            if KEYS[pygame.K_s] and self.y_cord < 720 - self.height:
                self.y_cord += 10
        elif self.player == 2:
            if KEYS[pygame.K_UP] and self.y_cord > 0:
                self.y_cord -= 10
            if KEYS[pygame.K_DOWN] and self.y_cord < 720 - self.height:
                self.y_cord += 10
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, [200, 150, 100], self.hitbox)


class Ball:
    def __init__(self, x, y):
        self.width = 20
        self.height = 20
        self.x_cord = x
        self.y_cord = y
        self.movment_x = 12
        self.movment_y = 5

    def tick(self, Player1, Player2):
        self.x_cord += self.movment_x
        self.y_cord += self.movment_y
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        if Player1.hitbox.colliderect(self.hitbox):
            self.movment_x *= -1
            if Player1.height > 60:
                Player1.height -= 20
                Player1.y_cord += 10
        elif Player2.hitbox.colliderect(self.hitbox):
            self.movment_x *= -1
            if Player2.height > 60:
                Player2.height -= 20
                Player2.y_cord += 10
        if self.y_cord < 0 or self.y_cord > 700:
            self.movment_y *= -1

    def draw(self, window):
        pygame.draw.rect(window, [200, 0, 0], self.hitbox)


def game_over(ball, player1, player2, window, KEYS):
    txt_img2 = pygame.font.Font.render(pygame.font.SysFont("arial", 32), "Nacisnij spacje by rozpoczać ponownie!", True,
                                       (255, 255, 255))
    if ball.x_cord < 0:
        txt_img = pygame.font.Font.render(pygame.font.SysFont("arial", 72), "Wygrywa strona prawa!", True, (255, 255, 255))
        window.blit(txt_img, (WIDTH / 2 - txt_img.get_width()/2, HEIGHT / 2))
        window.blit(txt_img2, (WIDTH / 2 - txt_img2.get_width()/2, HEIGHT / 2 + 100))
        if KEYS[pygame.K_SPACE]:
            reset(player1, player2, ball,window)
    elif ball.x_cord > 1200:
        txt_img = pygame.font.Font.render(pygame.font.SysFont("arial", 72), "Wygrywa strona lewa!", True, (255, 255, 255))
        window.blit(txt_img, (WIDTH / 2 - txt_img.get_width()/2, HEIGHT / 2))
        window.blit(txt_img2, (WIDTH / 2 - txt_img2.get_width()/2, HEIGHT / 2 + 100))
        if KEYS[pygame.K_SPACE]:
            reset(player1, player2, ball, window)


def reset(player1, player2, ball, window):
    player1.y_cord = 200
    player1.height = 300
    player2.y_cord = 200
    player2.height = 300
    ball.x_cord = WIDTH / 2
    ball.y_cord = HEIGHT / 2
    for i in range(3, -1, -1):
        time_text = pygame.font.Font.render(pygame.font.SysFont("arial", 72), str(i), True, (255, 255, 255))
        window.fill((0,0,0))
        player1.draw(window)
        player2.draw(window)
        window.blit(time_text, (WIDTH/2 - time_text.get_width()/2, HEIGHT/2 - time_text.get_height()/2))
        pygame.display.update()
        time.sleep(1)

def main():
    player1 = Player(10, 200, 1)
    player2 = Player(1150, 200, 2)
    ball = Ball(WIDTH / 2, HEIGHT / 2-100)
    run = True
    for i in range(3, -1, -1):
        time_text = pygame.font.Font.render(pygame.font.SysFont("arial", 72), str(i), True, (255, 255, 255))
        window.fill((0, 0, 0))
        window.blit(time_text, (WIDTH / 2 - time_text.get_width() / 2, HEIGHT / 2 - time_text.get_height() / 2))
        pygame.display.update()
        time.sleep(1)
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((0, 0, 0))

        KEYS = pygame.key.get_pressed()

        player1.tick(KEYS)
        player2.tick(KEYS)
        ball.tick(player1, player2)

        player1.draw(window)
        player2.draw(window)
        ball.draw(window)
        game_over(ball, player1, player2, window, KEYS)
        pygame.display.update()



if __name__ == "__main__":
    main()
