import pygame

class cor:
    AMARELO = '\033[93m'
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    FIM = '\033[0m'


print(cor.AMARELO + 'Iniciando o jogo Salve a Mai! By: Lins. Divirta-se!' + cor.FIM)

pygame.init()

# Imagens do Player
walkR = [pygame.image.load('imagens/Player/R1.png'), pygame.image.load('imagens/Player/R2.png'),
         pygame.image.load('imagens/Player/R3.png'), pygame.image.load('imagens/Player/R4.png')]

walkL = [pygame.image.load('imagens/Player/L1.png'), pygame.image.load('imagens/Player/L2.png'),
         pygame.image.load('imagens/Player/L3.png'), pygame.image.load('imagens/Player/L4.png')]

attackL = [pygame.image.load('imagens/Player/SL1.png'), pygame.image.load('imagens/Player/SL2.png'),
           pygame.image.load('imagens/Player/SL3.png'), pygame.image.load('imagens/Player/SL4.png'),
           pygame.image.load('imagens/Player/SL5.png'), pygame.image.load('imagens/Player/SL6.png'),
           pygame.image.load('imagens/Player/SL7.png'), pygame.image.load('imagens/Player/SL8.png'),
           pygame.image.load('imagens/Player/SL9.png')]

attackR = [pygame.image.load('imagens/Player/SR1.png'), pygame.image.load('imagens/Player/SR2.png'),
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

# Imagem flecha
arrowL = pygame.image.load('imagens/Player/arrowL.png')
arrowR = pygame.image.load('imagens/Player/arrowR.png')

# Imagens HUD / Background
bg = pygame.image.load('imagens/Mapa/mapa.png')
#bg2 = pygame.image.load('imagens/Mapa/mapa2.png')
teclas = pygame.image.load('imagens/Misc/keys.png')
icone = pygame.image.load('imagens/Misc/icone.png')
diepic = pygame.image.load('imagens/Mapa/die.png')
gameoverpic = pygame.image.load('imagens/Mapa/gameover.png')
vidas3 = pygame.image.load('imagens/Mapa/vidas3.png')
vidas2 = pygame.image.load('imagens/Mapa/vidas2.png')
vidas1 = pygame.image.load('imagens/Mapa/vidas1.png')
vidas0 = pygame.image.load('imagens/Mapa/vidas0.png')

# Configurações da janela
pygame.display.set_icon(icone)
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Salve a Mai!")
clock = pygame.time.Clock()
life = 3

# Sons
arrowSound = pygame.mixer.Sound("BGM/arrow.wav")
die = pygame.mixer.Sound("BGM/die.wav")
gameover = pygame.mixer.Sound("BGM/gameover.wav")
hitSound = pygame.mixer.Sound("BGM/hit.wav")

## Sons/Monstros
snaildie = pygame.mixer.Sound("BGM/snaildie.wav")


# Personagem
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
        self.plathitbox = (self.x + 23, self.y + 100, 37, 26)
        self.health = 3
        self.onPlatform = False

    def draw(self, win):
        if self.attackCount + 1 >= 24:
            self.attackCount = 0

        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if self.left:
            if self.jumpCount < 10:
                win.blit(jumpL, (round(self.x), round(self.y)))
            else:
                win.blit(walkL[self.walkCount // 6], (round(self.x), round(self.y)))
                self.walkCount += 1

        elif self.right:
            if self.jumpCount < 10:
                win.blit(jumpR, (round(self.x), round(self.y)))
            else:
                win.blit(walkR[self.walkCount // 6], (round(self.x), round(self.y)))
                self.walkCount += 1

        elif self.jumpCount < 10 and self.facing == 0:
            win.blit(jumpL, (round(self.x), round(self.y)))

        elif self.jumpCount < 10 and self.facing == 1:
            win.blit(jumpR, (round(self.x), round(self.y)))

        elif self.attack:
            if self.facing == 0:
                win.blit(attackL[self.attackCount // 3], (round(self.x), round(self.y)))
                self.attackCount += 1
            elif self.facing == 1:
                win.blit(attackR[self.attackCount // 3], (round(self.x), round(self.y)))
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
        self.plathitbox = (self.x + 30, self.y + 75, 20, 1)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.plathitbox, 2)

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


# Flecha
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


# Objetos de Porto Lith #
## Plataformas Porto Lith
class platform1(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= 0:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform2(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= 0:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform3(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= 0:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform4(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform5(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform6(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform7(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform8(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform9(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform10(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform11(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform12(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform13(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform14(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform15(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False

class platform16(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if man.jumpCount <= -1:
            man.onPlatform = True
            man.jumpCount = 10
            man.isJump = False
        else:
            man.onPlatform = False
## Espinhos Porto Lith
class spike1(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class spike2(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

## Monstros Porto Lith
class snail(object):
    walkR = [pygame.image.load('imagens/Mob/Snail/R1S.png'), pygame.image.load('imagens/Mob/Snail/R2S.png'),
             pygame.image.load('imagens/Mob/Snail/R3S.png'), pygame.image.load('imagens/Mob/Snail/R4S.png'),
             pygame.image.load('imagens/Mob/Snail/R5S.png'), pygame.image.load('imagens/Mob/Snail/R6S.png')]

    walkL = [pygame.image.load('imagens/Mob/Snail/L1S.png'), pygame.image.load('imagens/Mob/Snail/L2S.png'),
             pygame.image.load('imagens/Mob/Snail/L3S.png'), pygame.image.load('imagens/Mob/Snail/L4S.png'),
             pygame.image.load('imagens/Mob/Snail/L5S.png'), pygame.image.load('imagens/Mob/Snail/L6S.png')]

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
                win.blit(self.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(self.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(self.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
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
    # Background (Mapa)
    win.blit(bg, (0 - camx, 0))
    #win.blit(bg2, (10920 - camx, 0))

    #HUD
    win.blit(teclas, (600, 5))
    if life == 3:
        win.blit(vidas3, (336, 5))
    elif life == 2:
        win.blit(vidas2, (336, 5))
    elif life == 1:
        win.blit(vidas1, (336, 5))
    elif life == 0:
        win.blit(vidas0, (336, 5))

    #Draw Player
    man.draw(win)
    for arrow in arrows:
        arrow.draw(win)

    #Draw Porto Lith
    #Draw Monstros Porto Lith
    snail.draw(win)

    #Draw Espinhos Porto Lith
    spike1.draw(win)
    spike2.draw(win)

    #Draw Plataformas Porto Lith
    platform1.draw(win)
    platform2.draw(win)
    platform3.draw(win)
    platform4.draw(win)
    platform5.draw(win)
    platform6.draw(win)
    platform7.draw(win)
    platform8.draw(win)
    platform9.draw(win)
    platform10.draw(win)
    platform11.draw(win)
    platform12.draw(win)
    platform13.draw(win)
    platform14.draw(win)
    platform15.draw(win)
    platform16.draw(win)

    pygame.display.update()


# Main loop
camx = 3870 #Camera

# Variavel Player
man = player(400, 470, 64, 64)
arrows = []
onGravity = False
checkpoint = 2065

# Variavel Monstros Porto Lith
snail = snail(100, 522, 64, 64, 300)

# Variavel Espinhos Porto Lith
spike1 = spike1(3735, 575, 115, 40)
spike2 = spike2(5245, 560, 925, 40)

# Variavel Plataformas Porto Lith
platform1 = platform1(4130, 445, 50, 20)
platform2 = platform2(4260, 445, 145, 20)
platform3 = platform3(4465, 400, 145, 20)
platform4 = platform4(4655, 340, 50, 20)
platform5 = platform5(4655, 240, 50, 20)
platform6 = platform6(4360, 170, 240, 20)
platform7 = platform7(5270, 475, 50, 20)
platform8 = platform8(5370, 420, 50, 20)
platform9 = platform9(5480, 355, 50, 20)
platform10 = platform10(5480, 265, 50, 20)
platform11 = platform11(5480, 180, 50, 20)
platform12 = platform12(5580, 180, 50, 20)
platform13 = platform13(5700, 355, 50, 20)
platform14 = platform14(5800, 270, 50, 20)
platform15 = platform15(5915, 415, 50, 20)
platform16 = platform16(6020, 470, 50, 20)

run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(27)

    #TESTES
    print("JumpCount:",man.jumpCount,"Camx:",camx,"onPlatform:",man.onPlatform,"isJump:",man.isJump)
    #print(camx)
    #print(man.y)
    #print(man.onPlatform)
    #print(man.isJump)

# BGM de cada cidade
    if camx == 0:
        music = pygame.mixer.music.load("BGM/BGMLOGIN.mp3")
        pygame.mixer.music.play(-1)

    if camx == 1500:
        music = pygame.mixer.music.load("BGM/BGM01.mp3")
        pygame.mixer.music.play(-1)

    if camx == 6400:
        music = pygame.mixer.music.load("BGM/BGM02.mp3")
        pygame.mixer.music.play(-1)

# Verificação de GameOver
    if man.health < 0:
        gameover.play()
        win.blit(gameoverpic, (0, 0))
        pygame.display.update()
        pygame.time.delay(5000)
        print(cor.VERMELHO + 'GAMEOVER! Boa sorte da próxima vez.' + cor.FIM)
        break

# Colisão Monstros Porto Lith
    if man.hitbox[1] < snail.hitbox[1] + snail.hitbox[3] and man.hitbox[1] + man.hitbox[3] > snail.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > snail.hitbox[0] and man.hitbox[0] < snail.hitbox[0] + snail.hitbox[2]:
            man.hit()
            life -= 1
            man.health -= 1
            camx = checkpoint
            man.x = 400
            man.y = 470

# Colisão Espinhos Porto Lith
    if man.hitbox[1] < spike1.hitbox[1] + spike1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > spike1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > spike1.hitbox[0] and man.hitbox[0] < spike1.hitbox[0] + spike1.hitbox[2]:
            man.hit()
            life -= 1
            man.health -= 1
            camx = checkpoint
            man.x = 400
            man.y = 470

    if man.hitbox[1] < spike2.hitbox[1] + spike2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > spike2.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > spike2.hitbox[0] and man.hitbox[0] < spike2.hitbox[0] + spike2.hitbox[2]:
            man.hit()
            life -= 1
            man.health -= 1
            camx = checkpoint
            man.x = 400
            man.y = 470
            
# Colisão Plataformas Porto Lith
    if man.plathitbox[1] < platform1.hitbox[1] + platform1.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform1.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform1.hitbox[0] and man.plathitbox[0] < platform1.hitbox[0] + platform1.hitbox[2]:
            platform1.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform2.hitbox[1] + platform2.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform2.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform2.hitbox[0] and man.plathitbox[0] < platform2.hitbox[0] + platform2.hitbox[2]:
            platform2.hit()
            man.onPlatform = True

    if man.plathitbox[1] < platform3.hitbox[1] + platform3.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform3.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform3.hitbox[0] and man.plathitbox[0] < platform3.hitbox[0] + platform3.hitbox[2]:
            platform3.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform4.hitbox[1] + platform4.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform4.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform4.hitbox[0] and man.plathitbox[0] < platform4.hitbox[0] + platform4.hitbox[2]:
            platform4.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False
            
    if man.plathitbox[1] < platform5.hitbox[1] + platform5.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform5.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform5.hitbox[0] and man.plathitbox[0] < platform5.hitbox[0] + platform5.hitbox[2]:
            platform5.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform6.hitbox[1] + platform6.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform6.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform6.hitbox[0] and man.plathitbox[0] < platform6.hitbox[0] + platform6.hitbox[2]:
            platform6.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform7.hitbox[1] + platform7.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform7.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform7.hitbox[0] and man.plathitbox[0] < platform7.hitbox[0] + platform7.hitbox[2]:
            platform7.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform8.hitbox[1] + platform8.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform8.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform8.hitbox[0] and man.plathitbox[0] < platform8.hitbox[0] + platform8.hitbox[2]:
            platform8.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform9.hitbox[1] + platform9.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform9.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform9.hitbox[0] and man.plathitbox[0] < platform9.hitbox[0] + platform9.hitbox[2]:
            platform9.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform10.hitbox[1] + platform10.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform10.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform10.hitbox[0] and man.plathitbox[0] < platform10.hitbox[0] + platform10.hitbox[2]:
            platform10.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform11.hitbox[1] + platform11.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform11.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform11.hitbox[0] and man.plathitbox[0] < platform11.hitbox[0] + platform11.hitbox[2]:
            platform11.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform12.hitbox[1] + platform12.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform12.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform12.hitbox[0] and man.plathitbox[0] < platform12.hitbox[0] + platform12.hitbox[2]:
            platform12.hit()
            man.onPlatform = True

    if man.plathitbox[1] < platform13.hitbox[1] + platform13.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform13.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform13.hitbox[0] and man.plathitbox[0] < platform13.hitbox[0] + platform13.hitbox[2]:
            platform13.hit()
            man.onPlatform = True

    if man.plathitbox[1] < platform14.hitbox[1] + platform14.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform14.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform14.hitbox[0] and man.plathitbox[0] < platform14.hitbox[0] + platform14.hitbox[2]:
            platform14.hit()
            man.onPlatform = True
        else:
            man.onPlatform = False

    if man.plathitbox[1] < platform15.hitbox[1] + platform15.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform15.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform15.hitbox[0] and man.plathitbox[0] < platform15.hitbox[0] + platform15.hitbox[2]:
            platform15.hit()
            man.onPlatform = True


    if man.plathitbox[1] < platform16.hitbox[1] + platform16.hitbox[3] and man.plathitbox[1] + man.plathitbox[3] > platform16.hitbox[1]:
        if man.plathitbox[0] + man.plathitbox[2] > platform16.hitbox[0] and man.plathitbox[0] < platform16.hitbox[0] + platform16.hitbox[2]:
            platform16.hit()
            man.onPlatform = True


# Funções da Gravidade
    if man.y < 470 and man.isJump == False and man.onPlatform == False:
        man.y = man.y + 10
        onGravity = True
    else:
        onGravity = False

# Gravidade / Buracos Porto Lith
    if camx > 3330 and camx < 3395 and man.isJump == False and man.onPlatform == False:
        man.y = man.y + 10

    if camx > 4815 and camx < 5660 and man.isJump == False and man.onPlatform == False:
        man.y = man.y + 10

    elif man.y > 470:
        man.y = 470

# Colisão Flechas
    for arrow in arrows:
        # Colisão Flechas Monstros Porto Lith
        if arrow.y - arrow.radius < snail.hitbox[1] + snail.hitbox[3] and arrow.y + arrow.radius > snail.hitbox[1]:
            if arrow.x + arrow.radius > snail.hitbox[0] and arrow.x - arrow.radius < snail.hitbox[0] + snail.hitbox[2]:
                snail.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.x < 800 and arrow.x > 0:
            arrow.x += arrow.vel
        else:
            arrows.pop(arrows.index(arrow))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print(cor.VERMELHO + "Finalizando o jogo..." + cor.FIM)

# Controles do jogo
    # Seta esquerda (Andar)
    if keys[pygame.K_LEFT] and man.x > man.vel and man.x - camx < 400:
        man.left = True
        man.right = False
        man.facing = 0
        camx -= 5

    # Seta direita (Andar)
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
        man.right = True
        man.left = False
        man.facing = 1
        camx += 5

    # Tecla X (Atacar)
    elif keys[pygame.K_x]:
        man.right = False
        man.left = False
        man.attack = True
        if man.facing == 0:
            facingB = -1
        else:
            facingB = 1
        if len(arrows) < 1:
            arrows.append(projectile(round(man.x + man.width // 1.6), round(man.y + man.height // 1.6), 13, facingB))
            arrowSound.play()

    # Tecla F2 (Emote sorrir)
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

    # Tecla espaço (Pular)
    if man.isJump == False:
        if onGravity == False:
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
            man.y -= round((man.jumpCount ** 2) / 4 * neg)
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()