import pygame

# инициализация Pygame
pygame.init()


# определяем цвета
BLACK = (109, 176, 113)
WHITE = (248, 243, 235)

#image_paddle =pygame.image.load('ufo.png')
#image_paddle = pygame.transform.scale(image_paddle, (40,20) )


# размеры экрана
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

# создаем ракетки и мячик
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [5, 5]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = self.velocity[1]

# создаем спрайты
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 670
paddle2.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# добавляем все спрайты в список
all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)

# создаем основной цикл программы
carryOn = True

clock = pygame.time.Clock()
scoreA = 0
scoreB = 0

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.moveUp(5)
    if keys[pygame.K_s]:
        paddle1.moveDown(5)
    if keys[pygame.K_UP]:
        paddle2.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(5)

    # проверка на столкновение ракеток и мяча
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()

    all_sprites_list.update()

    # заливаем фон
    screen.fill(BLACK)

    # рисуем сетку
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # отображаем спрайты
    all_sprites_list.draw(screen)

    # выводим счет
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # обновляем экран
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
