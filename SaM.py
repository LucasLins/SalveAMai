import pygame


class cor:
    AMARELO = '\033[93m'
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    FIM = '\033[0m'


print(cor.AMARELO + 'Iniciando o jogo Salve a Mai! By: Lins. Divirta-se!' + cor.FIM)

pygame.init()

# Variáveis Imagens
walkRight = [pygame.image.load('imagens/Player/R1.png'), pygame.image.load('imagens/Player/R2.png'),
             pygame.image.load('imagens/Player/R3.png'), pygame.image.load('imagens/Player/R4.png'),
             pygame.image.load('imagens/Player/R5.png'), pygame.image.load('imagens/Player/R6.png'),
             pygame.image.load('imagens/Player/R7.png'), pygame.image.load('imagens/Player/R8.png'),
             pygame.image.load('imagens/Player/R9.png')]
walkLeft = [pygame.image.load('imagens/Player/L1.png'), pygame.image.load('imagens/Player/L2.png'),
            pygame.image.load('imagens/Player/L3.png'), pygame.image.load('imagens/Player/L4.png'),
            pygame.image.load('imagens/Player/L5.png'), pygame.image.load('imagens/Player/L6.png'),
            pygame.image.load('imagens/Player/L7.png'), pygame.image.load('imagens/Player/L8.png'),
            pygame.image.load('imagens/Player/L9.png')]
attackLeft = [pygame.image.load('imagens/Player/SL1.png'), pygame.image.load('imagens/Player/SL2.png'),
              pygame.image.load('imagens/Player/SL3.png'), pygame.image.load('imagens/Player/SL4.png'),
              pygame.image.load('imagens/Player/SL5.png'), pygame.image.load('imagens/Player/SL6.png'),
              pygame.image.load('imagens/Player/SL7.png'), pygame.image.load('imagens/Player/SL8.png'),
              pygame.image.load('imagens/Player/SL9.png')]
attackRight = [pygame.image.load('imagens/Player/SR1.png'), pygame.image.load('imagens/Player/SR2.png'),
               pygame.image.load('imagens/Player/SR3.png'), pygame.image.load('imagens/Player/SR4.png'),
               pygame.image.load('imagens/Player/SR5.png'), pygame.image.load('imagens/Player/SR6.png'),
               pygame.image.load('imagens/Player/SR7.png'), pygame.image.load('imagens/Player/SR8.png'),
               pygame.image.load('imagens/Player/SR9.png')]
charL = pygame.image.load('imagens/Player/standingL.png')
charR = pygame.image.load('imagens/Player/standingR.png')
jumpL = pygame.image.load('imagens/Player/jumpL.png')
jumpR = pygame.image.load('imagens/Player/jumpR.png')
smileR = pygame.image.load('imagens/Player/smileR.png')
smileL = pygame.image.load('imagens/Player/smileL.png')
arrowL = pygame.image.load('imagens/Player/arrowL.png')
arrowR = pygame.image.load('imagens/Player/arrowR.png')
bg = pygame.image.load('imagens/Mapa/mapa.png')
teclas = pygame.image.load('imagens/Misc/keys.png')
icone = pygame.image.load('imagens/Misc/icone.png')
diepic = pygame.image.load('imagens/Mapa/die.png')
gameoverpic = pygame.image.load('imagens/Mapa/gameover.png')
vidas3 = pygame.image.load('imagens/Mapa/vidas3.png')
vidas2 = pygame.image.load('imagens/Mapa/vidas2.png')
vidas1 = pygame.image.load('imagens/Mapa/vidas1.png')
vidas0 = pygame.image.load('imagens/Mapa/vidas0.png')

# Configurações da janela
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Salve a Mai!")
pygame.display.set_icon(icone)
clock = pygame.time.Clock()
life = 3

# Variáveis BGM
arrowSound = pygame.mixer.Sound("BGM/arrow.wav")
hitSound = pygame.mixer.Sound("BGM/hit.wav")
snaildie = pygame.mixer.Sound("BGM/snaildie.wav")
die = pygame.mixer.Sound("BGM/die.wav")
gameover = pygame.mixer.Sound("BGM/gameover.wav")

#music = pygame.mixer.music.load("BGM/BGM01.mp3")
#pygame.mixer.music.play(-1)


# Variáveis do Personagem
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.smile = False
        self.attack = False
        self.walkCount = 0
        self.jumpCount = 10
        self.attackCount = 0
        self.facing = 1  # Direita = 1 | Esquerda = 0
        self.hitbox = (self.x + 23, self.y + 5, 37, 73)
        self.health = 3
        self.onPlatform = False

    def draw(self, win):
        if self.attackCount + 1 >= 27:
            self.attackCount = 0

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            if self.jumpCount < 10:
                win.blit(jumpL, (round(self.x), round(self.y)))
            else:
                win.blit(walkLeft[self.walkCount // 3], (round(self.x), round(self.y)))
                self.walkCount += 1

        elif self.right:
            if self.jumpCount < 10:
                win.blit(jumpR, (round(self.x), round(self.y)))
            else:
                win.blit(walkRight[self.walkCount // 3], (round(self.x), round(self.y)))
                self.walkCount += 1

        elif self.jumpCount < 10 and self.facing == 0:
            win.blit(jumpL, (round(self.x), round(self.y)))

        elif self.jumpCount < 10 and self.facing == 1:
            win.blit(jumpR, (round(self.x), round(self.y)))

        elif self.attack:
            if self.facing == 0:
                win.blit(attackLeft[self.attackCount // 3], (round(self.x), round(self.y)))
                self.attackCount += 1
            elif self.facing == 1:
                win.blit(attackRight[self.attackCount // 3], (round(self.x), round(self.y)))
                self.attackCount += 1

        elif self.smile == True and self.facing == 1:
            win.blit(smileR, (round(self.x), round(self.y)))

        elif self.smile == True and self.facing == 0:
            win.blit(smileL, (round(self.x), round(self.y)))

        elif self.facing == 1:
            win.blit(charR, (round(self.x), round(self.y)))

        else:
            win.blit(charL, (round(self.x), round(self.y)))
        self.hitbox = (self.x + 23, self.y + 5, 37, 73)

    # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if self.health >= 1:
            die.play()
            win.blit(diepic, (0, 0))
            pygame.display.update()
            self.x = 654
            self.y = 361
            pygame.time.delay(3000)
            self.walkCount = 0
            self.jumpCount = 10
            self.isJump = False


class projectile(object):
    def __init__(self, x, y, radius, facingB):
        self.x = x
        self.y = y
        self.radius = radius
        self.facingB = facingB
        self.vel = 24 * facingB

    def draw(self, win):
        if self.facingB == -1:
            win.blit(arrowL, (round(self.x), round(self.y)))
        else:
            win.blit(arrowR, (round(self.x), round(self.y)))


class platform(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 100, 5)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, 100, 5)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False

class spike(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 65, 40)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, 65, 40)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class snail(object):
    walkRight = [pygame.image.load('imagens/Mob/Snail/R1S.png'), pygame.image.load('imagens/Mob/Snail/R2S.png'),
                 pygame.image.load('imagens/Mob/Snail/R3S.png'), pygame.image.load('imagens/Mob/Snail/R4S.png'),
                 pygame.image.load('imagens/Mob/Snail/R5S.png'), pygame.image.load('imagens/Mob/Snail/R6S.png')]

    walkLeft = [pygame.image.load('imagens/Mob/Snail/L1S.png'), pygame.image.load('imagens/Mob/Snail/L2S.png'),
                pygame.image.load('imagens/Mob/Snail/L3S.png'),
                pygame.image.load('imagens/Mob/Snail/L4S.png'), pygame.image.load('imagens/Mob/Snail/L5S.png'),
                pygame.image.load('imagens/Mob/Snail/L6S.png')]
    RHS = pygame.image.load('imagens/Mob/Snail/RHS.png')
    LHS = pygame.image.load('imagens/Mob/Snail/LHS.png')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, 37, 29)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(self.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(self.LHS, (round(self.x -camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] -2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, 37, 29)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        hitSound.play()
        if self.health > 0 and self.vel > 0:
            self.washit = 1
            self.health -= 1
        elif self.health > 0 and self.vel < 0:
            self.washit = 2
            self.health -= 1
        else:
            if self.vel > 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 1
                self.visible = False
                snaildie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                snaildie.play()
            else:
                self.washit = 0


def redrawGameWindow():
    # Background
    win.blit(bg, (0 - camx, 0 - camy))
    win.blit(teclas, (600, 5))
    if life == 3:
        win.blit(vidas3, (336, 5))
    elif life == 2:
        win.blit(vidas2, (336, 5))
    elif life == 1:
        win.blit(vidas1, (336, 5))
    elif life == 0:
        win.blit(vidas0, (336, 5))

    # text = font.render('Vidas: ' + str(life), 1, (255,255,255))
    # win.blit(text, (400, 10))
    man.draw(win)
    snail.draw(win)
    platform.draw(win)
    spike.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# Main loop
camx = 0
camy = 0
font = pygame.font.SysFont('comicsans', 25, True)
man = player(400, 470, 64, 64)
snail = snail(100, 522, 64, 64, 300)
platform = platform(400, 369, 100, 1)
spike = spike(3765, 575, 65, 40)
bullets = []
run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(27)

    #print(camx)
    #print(man.y)
    if camx == 0:
        music = pygame.mixer.music.load("BGM/BGMLOGIN.mp3")
        pygame.mixer.music.play(-1)

    if camx == 1500:
        music = pygame.mixer.music.load("BGM/BGM01.mp3")
        pygame.mixer.music.play(-1)

    if camx == 6400:
        music = pygame.mixer.music.load("BGM/BGM02.mp3")
        pygame.mixer.music.play(-1)

    if man.health < 0:
        gameover.play()
        win.blit(gameoverpic, (0, 0))
        pygame.display.update()
        pygame.time.delay(5000)
        print(cor.VERMELHO + 'GAMEOVER! Boa sorte da próxima vez.' + cor.FIM)
        break
    if man.hitbox[1] < snail.hitbox[1] + snail.hitbox[3] and man.hitbox[1] + man.hitbox[3] > snail.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > snail.hitbox[0] and man.hitbox[0] < snail.hitbox[0] + snail.hitbox[2]:
            man.hit()
            life -= 1
            man.health -= 1
            camx = 0
            
    if man.hitbox[1] < spike.hitbox[1] + spike.hitbox[3] and man.hitbox[1] + man.hitbox[3] > spike.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > spike.hitbox[0] and man.hitbox[0] < spike.hitbox[0] + spike.hitbox[2]:
            man.hit()
            life -= 1
            man.health -= 1
            camx = 2065
            man.x = 400
            man.y = 470

    # gravidade
    if man.y < 361 and man.isJump == False and man.onPlatform == False:
        man.y = man.y + 15

    if camx > 3330 and camx < 3395 and man.isJump == False and man.onPlatform == False:
        man.y = man.y + 15

    if man.hitbox[1] < platform.hitbox[1] + platform.hitbox[3] and man.hitbox[1] + man.hitbox[3] > platform.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > platform.hitbox[0] and man.hitbox[0] < platform.hitbox[0] + platform.hitbox[2]:
            platform.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False
    else:
        man.onPlatform = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < snail.hitbox[1] + snail.hitbox[3] and bullet.y + bullet.radius > snail.hitbox[1]:
            if bullet.x + bullet.radius > snail.hitbox[0] and bullet.x - bullet.radius < snail.hitbox[0] + snail.hitbox[2]:
                snail.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # Controles do jogo

    # Seta esquerda
    if keys[pygame.K_LEFT] and man.x > man.vel and man.x - camx < 400:
       # man.x -= man.vel
        man.left = True
        man.right = False
        man.facing = 0
        camx -= 5

    # Seta direita
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
      #  man.x += man.vel
        man.right = True
        man.left = False
        man.facing = 1
        camx += 5

    # Tecla X
    elif keys[pygame.K_x]:
        man.right = False
        man.left = False
        man.attack = True
        if man.facing == 0:
            facingB = -1
        else:
            facingB = 1
        if len(bullets) < 1:
            bullets.append(projectile(round(man.x + man.width // 1.6), round(man.y + man.height // 1.6), 13, facingB))
            arrowSound.play()


    elif keys[pygame.K_F2]:
        man.smile = True
        man.right = False
        man.left = False
        man.attack = False
    else:
        man.right = False
        man.left = False
        man.attack = False
        man.smile = False
        man.walkCount = 0
        man.attackCount = 0

    # Tecla espaço
    if man.isJump == False:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
            man.attackCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) / 4 * neg
            #camy -=(man.jumpCount ** 2) / 4 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()