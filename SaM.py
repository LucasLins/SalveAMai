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
bg2 = pygame.image.load('imagens/Mapa/mapa2.png')
teclas = pygame.image.load('imagens/Misc/keys.png')
icone = pygame.image.load('imagens/Misc/icone.png')
diepic = pygame.image.load('imagens/Mapa/die.png')
gameoverpic = pygame.image.load('imagens/Mapa/gameover.png')
vidas3 = pygame.image.load('imagens/Mapa/vidas3.png')
vidas2 = pygame.image.load('imagens/Mapa/vidas2.png')
vidas1 = pygame.image.load('imagens/Mapa/vidas1.png')
vidas0 = pygame.image.load('imagens/Mapa/vidas0.png')
detonado = pygame.image.load('imagens/Mapa/detonado.png')
errado = pygame.image.load('imagens/Mapa/errado.png')

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
sucesso = pygame.mixer.Sound("BGM/sucesso.wav")
fail = pygame.mixer.Sound("BGM/fail.wav")

## Sons/Monstros
hitSound = pygame.mixer.Sound("BGM/hit.wav")
snaildie = pygame.mixer.Sound("BGM/snaildie.wav")
cogudie = pygame.mixer.Sound("BGM/cogudie.wav")
tocodie = pygame.mixer.Sound("BGM/tocodie.wav")
tocohit = pygame.mixer.Sound("BGM/tocohit.wav")
stumpyhit = pygame.mixer.Sound("BGM/stumpyhit.wav")
stumpydie = pygame.mixer.Sound("BGM/stumpydie.wav")
stumpyskill = pygame.mixer.Sound("BGM/stumpyskill.wav")

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
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
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
        if player.jumpCount <= 0:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= 0:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= 0:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


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
class snail1(object):
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
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
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
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class snail2(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(snail1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(snail1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(snail1.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(snail1.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class snail3(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(snail1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(snail1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(snail1.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(snail1.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class snail4(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(snail1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(snail1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(snail1.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(snail1.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class snail5(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(snail1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(snail1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(snail1.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(snail1.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class snail6(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(snail1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(snail1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(snail1.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(snail1.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class snail7(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
        self.washit = 0
        self.health = 3
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(snail1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(snail1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(snail1.RHS, (round(self.x - camx - 2), round(self.y - 8)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(snail1.LHS, (round(self.x - camx - 5), round(self.y - 8)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 2, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 45 - (15 * (3 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y - 3, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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

# Objetos Henesys
## Espinhos Henesys
class spike3(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class spike4(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class spike5(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class spike6(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

## Plataformas Henesys
class platform17(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform18(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform19(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform20(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform21(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform22(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform23(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform24(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform25(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform26(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform27(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform28(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform29(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform30(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform31(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform32(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform33(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform34(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform35(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform36(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform37(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform38(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform39(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform40(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform41(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform42(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

## Monstros Henesys
class cogu1(object):
    walkR = [pygame.image.load('imagens/Mob/Cogu/RC1.png'), pygame.image.load('imagens/Mob/Cogu/RC2.png'),
             pygame.image.load('imagens/Mob/Cogu/RC3.png'), pygame.image.load('imagens/Mob/Cogu/RC4.png'),
             pygame.image.load('imagens/Mob/Cogu/RC5.png'), pygame.image.load('imagens/Mob/Cogu/RC6.png')]

    walkL = [pygame.image.load('imagens/Mob/Cogu/LC1.png'), pygame.image.load('imagens/Mob/Cogu/LC2.png'),
             pygame.image.load('imagens/Mob/Cogu/LC3.png'), pygame.image.load('imagens/Mob/Cogu/LC4.png'),
             pygame.image.load('imagens/Mob/Cogu/LC5.png'), pygame.image.load('imagens/Mob/Cogu/LC6.png')]

    RHS = pygame.image.load('imagens/Mob/Cogu/RHC.png')
    LHS = pygame.image.load('imagens/Mob/Cogu/LHC.png')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
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
                win.blit(self.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(self.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu2(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu3(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu4(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu5(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu6(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu7(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu8(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu9(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu10(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu11(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0
class cogu12(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu13(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

class cogu14(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(cogu1.walkR[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(cogu1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(cogu1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(cogu1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 13, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                cogudie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                cogudie.play()
            else:
                self.washit = 0

# Espinhos Perion
class spike7(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class spike8(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class spike9(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    # Plataformas Perion
class platform43(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform44(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform45(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform46(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform47(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform48(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform49(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform50(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform51(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform52(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform53(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform54(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform55(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform56(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform57(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform58(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform59(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform60(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform61(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform62(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform63(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform64(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform65(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform66(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

    # Objetos Parede Perion
class wall1(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall2(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

# Objetos Plataformas Ellinia
class platform67(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform68(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform69(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform70(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform71(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform72(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform73(object):

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
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


# Objetos Parede Ellinia
class wall3(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall4(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        
    # Objetos Gate Perion
class gate1(object):
    walkR = [pygame.image.load('imagens/Mob/Gate/1.png'), pygame.image.load('imagens/Mob/Gate/2.png'),
             pygame.image.load('imagens/Mob/Gate/3.png'), pygame.image.load('imagens/Mob/Gate/4.png'),
             pygame.image.load('imagens/Mob/Gate/5.png'), pygame.image.load('imagens/Mob/Gate/6.png'),
             pygame.image.load('imagens/Mob/Gate/7.png'), pygame.image.load('imagens/Mob/Gate/8.png')]

    walkL = [pygame.image.load('imagens/Mob/Gate/1.png'), pygame.image.load('imagens/Mob/Gate/2.png'),
             pygame.image.load('imagens/Mob/Gate/3.png'), pygame.image.load('imagens/Mob/Gate/4.png'),
             pygame.image.load('imagens/Mob/Gate/5.png'), pygame.image.load('imagens/Mob/Gate/6.png'),
             pygame.image.load('imagens/Mob/Gate/7.png'), pygame.image.load('imagens/Mob/Gate/8.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        #self.move()
        if stumpy.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                self.washit = 0
            elif self.washit == 2:
                self.washit = 0

# Altar Perion

class altar1(object):
    walkR = [pygame.image.load('imagens/Mapa/altar1.png'), pygame.image.load('imagens/Mapa/altar2.png')]

    walkL = [pygame.image.load('imagens/Mapa/altar1.png'), pygame.image.load('imagens/Mapa/altar2.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 6
        self.visible = True

    def draw(self, win):
        #self.move()
        if self.visible:
            if self.walkCount + 1 >= 4:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 2], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkL[self.walkCount // 2], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                self.washit = 0
            elif self.washit == 2:
                self.washit = 0

# Monstros Perion
class toco1(object):
    walkR = [pygame.image.load('imagens/Mob/Toco/TR1.png'), pygame.image.load('imagens/Mob/Toco/TR2.png'),
             pygame.image.load('imagens/Mob/Toco/TR3.png'), pygame.image.load('imagens/Mob/Toco/TR4.png')]

    walkL = [pygame.image.load('imagens/Mob/Toco/TL1.png'), pygame.image.load('imagens/Mob/Toco/TL2.png'),
             pygame.image.load('imagens/Mob/Toco/TL3.png'), pygame.image.load('imagens/Mob/Toco/TL4.png')]

    RHS = pygame.image.load('imagens/Mob/Toco/THR.png')
    LHS = pygame.image.load('imagens/Mob/Toco/THL.png')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(self.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(self.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco2(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco3(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco4(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0

class toco5(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0

class toco6(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0

class toco7(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco8(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco9(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco10(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco11(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco12(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco13(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco14(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco15(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0


class toco16(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(toco1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(toco1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(toco1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(toco1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        tocohit.play()
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
                tocodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                tocodie.play()
            else:
                self.washit = 0

class stumpy(object): # Boss perion
    walkR = [pygame.image.load('imagens/Mob/Stumpy/1.png'), pygame.image.load('imagens/Mob/Stumpy/2.png'),
             pygame.image.load('imagens/Mob/Stumpy/3.png'), pygame.image.load('imagens/Mob/Stumpy/4.png'),
             pygame.image.load('imagens/Mob/Stumpy/5.png'), pygame.image.load('imagens/Mob/Stumpy/6.png'),
             pygame.image.load('imagens/Mob/Stumpy/7.png'), pygame.image.load('imagens/Mob/Stumpy/8.png'),
             pygame.image.load('imagens/Mob/Stumpy/9.png'), pygame.image.load('imagens/Mob/Stumpy/10.png'),
             pygame.image.load('imagens/Mob/Stumpy/11.png'), pygame.image.load('imagens/Mob/Stumpy/12.png'),
             pygame.image.load('imagens/Mob/Stumpy/13.png'), pygame.image.load('imagens/Mob/Stumpy/14.png'),
             pygame.image.load('imagens/Mob/Stumpy/15.png'), pygame.image.load('imagens/Mob/Stumpy/16.png'),
             pygame.image.load('imagens/Mob/Stumpy/17.png'), pygame.image.load('imagens/Mob/Stumpy/18.png'),
             pygame.image.load('imagens/Mob/Stumpy/19.png'), pygame.image.load('imagens/Mob/Stumpy/20.png'),
             pygame.image.load('imagens/Mob/Stumpy/21.png'), pygame.image.load('imagens/Mob/Stumpy/22.png'),
             pygame.image.load('imagens/Mob/Stumpy/23.png'), pygame.image.load('imagens/Mob/Stumpy/24.png')]

    walkL = [pygame.image.load('imagens/Mob/Stumpy/1.png'), pygame.image.load('imagens/Mob/Stumpy/2.png'),
             pygame.image.load('imagens/Mob/Stumpy/3.png'), pygame.image.load('imagens/Mob/Stumpy/4.png'),
             pygame.image.load('imagens/Mob/Stumpy/5.png'), pygame.image.load('imagens/Mob/Stumpy/6.png'),
             pygame.image.load('imagens/Mob/Stumpy/7.png'), pygame.image.load('imagens/Mob/Stumpy/8.png'),
             pygame.image.load('imagens/Mob/Stumpy/9.png'), pygame.image.load('imagens/Mob/Stumpy/10.png'),
             pygame.image.load('imagens/Mob/Stumpy/11.png'), pygame.image.load('imagens/Mob/Stumpy/12.png'),
             pygame.image.load('imagens/Mob/Stumpy/13.png'), pygame.image.load('imagens/Mob/Stumpy/14.png'),
             pygame.image.load('imagens/Mob/Stumpy/15.png'), pygame.image.load('imagens/Mob/Stumpy/16.png'),
             pygame.image.load('imagens/Mob/Stumpy/17.png'), pygame.image.load('imagens/Mob/Stumpy/18.png'),
             pygame.image.load('imagens/Mob/Stumpy/19.png'), pygame.image.load('imagens/Mob/Stumpy/20.png'),
             pygame.image.load('imagens/Mob/Stumpy/21.png'), pygame.image.load('imagens/Mob/Stumpy/22.png'),
             pygame.image.load('imagens/Mob/Stumpy/23.png'), pygame.image.load('imagens/Mob/Stumpy/24.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 89
        self.visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 96:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                self.washit = 0
            elif self.washit == 2:
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 50, self.hitbox[1] - 80, 187, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0]- 48, self.hitbox[1] - 78, 183 - (2 * (89 - self.health)), 4))
            self.hitbox = (self.x - camx + 50, self.y + 80, self.width, self.height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        stumpyhit.play()
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
                stumpydie.play()
                sucesso.play()
                win.blit(detonado, (57, 232))
                pygame.display.update()
                pygame.time.delay(2000)

            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                stumpydie.play()
            else:
                self.washit = 0

# Objetos Spike Ellinia
class spike10(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


def GameWindow():
    # Background (Mapa)
    win.blit(bg2, (10920 - camx, 0))
    win.blit(bg, (0 - camx, 0))


    # HUD
    win.blit(teclas, (600, 5))
    if life == 3:
        win.blit(vidas3, (336, 5))
    elif life == 2:
        win.blit(vidas2, (336, 5))
    elif life == 1:
        win.blit(vidas1, (336, 5))
    elif life == 0:
        win.blit(vidas0, (336, 5))

    # Draw Gate Perion
    gate1.draw(win)
    # Draw Objetos Mapa Perion
    altar1.draw(win)
    # Draw Player
    player.draw(win)
    for arrow in arrows:
        arrow.draw(win)

    # Draw Porto Lith
    # Draw Monstros Porto Lith
    snail1.draw(win)
    snail2.draw(win)
    snail3.draw(win)
    snail4.draw(win)
    snail5.draw(win)
    snail6.draw(win)
    snail7.draw(win)

    # Draw Espinhos Porto Lith
    spike1.draw(win)
    spike2.draw(win)

    # Draw Plataformas Porto Lith
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

    # Draw Henesys
    # Draw Espinhos Henesys
    spike3.draw(win)
    spike4.draw(win)
    spike5.draw(win)
    spike6.draw(win)

    #Draw Plataformas Henesys
    platform16.draw(win)
    platform17.draw(win)
    platform18.draw(win)
    platform19.draw(win)
    platform20.draw(win)
    platform21.draw(win)
    platform22.draw(win)
    platform23.draw(win)
    platform24.draw(win)
    platform25.draw(win)
    platform26.draw(win)
    platform27.draw(win)
    platform28.draw(win)
    platform29.draw(win)
    platform30.draw(win)
    platform31.draw(win)
    platform32.draw(win)
    platform33.draw(win)
    platform34.draw(win)
    platform35.draw(win)
    platform36.draw(win)
    platform37.draw(win)
    platform38.draw(win)
    platform39.draw(win)
    platform40.draw(win)
    platform41.draw(win)
    platform42.draw(win)

# Draw Monstros Henesys
    cogu1.draw(win)
    cogu2.draw(win)
    cogu3.draw(win)
    cogu4.draw(win)
    cogu5.draw(win)
    cogu6.draw(win)
    cogu7.draw(win)
    cogu8.draw(win)
    cogu9.draw(win)
    cogu10.draw(win)
    cogu11.draw(win)
    cogu12.draw(win)
    cogu13.draw(win)
    cogu14.draw(win)

# Draw Espinhos Perion
    spike7.draw(win)
    spike8.draw(win)
    spike9.draw(win)

# Draw Plataformas Perion
    platform43.draw(win)
    platform44.draw(win)
    platform45.draw(win)
    platform46.draw(win)
    platform47.draw(win)
    platform48.draw(win)
    platform49.draw(win)
    platform50.draw(win)
    platform51.draw(win)
    platform52.draw(win)
    platform53.draw(win)
    platform54.draw(win)
    platform55.draw(win)
    platform56.draw(win)
    platform57.draw(win)
    platform58.draw(win)
    platform59.draw(win)
    platform60.draw(win)
    platform61.draw(win)
    platform62.draw(win)
    platform63.draw(win)
    platform64.draw(win)
    platform65.draw(win)
    platform66.draw(win)

# Draw Monstros Perion
    toco1.draw(win)
    toco2.draw(win)
    toco3.draw(win)
    toco4.draw(win)
    toco5.draw(win)
    toco6.draw(win)
    toco7.draw(win)
    toco8.draw(win)
    toco9.draw(win)
    toco10.draw(win)
    toco11.draw(win)
    toco12.draw(win)
    toco13.draw(win)
    toco14.draw(win)
    toco15.draw(win)
    toco16.draw(win)
    stumpy.draw(win)
# Draw Paredes Perion
    wall1.draw(win)
    wall2.draw(win)

# Draw Spikes Ellinia
    spike10.draw(win)

#Draw Parede Ellinia
    wall3.draw(win)
    wall4.draw(win)

#Draw Plataformas Ellinia
    platform67.draw(win)
    platform68.draw(win)
    platform69.draw(win)
    platform70.draw(win)
    platform71.draw(win)
    platform72.draw(win)
    platform73.draw(win)
    pygame.display.update()


# Main loop
camx = 13500  # Camera

# Variavel Player
player = player(400, 470, 64, 64)
arrows = []
onGravity = False
checkpoint = 2065

# Variavel Monstros Porto Lith
snail1 = snail1(3195, 522, 37, 26, 3430)
snail2 = snail2(3850, 522, 37, 26, 4080)
snail3 = snail3(4270, 424, 37, 26, 4363)
snail4 = snail4(4465, 384, 37, 26, 4563)
snail5 = snail5(4435, 152, 37, 26, 4563)
snail6 = snail6(4980, 522, 37, 26, 5163)
snail7 = snail7(5690, 334, 37, 26, 5718)

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

# Variavel Espinhos Henesys
spike3 = spike3(7635, 500, 30, 40)
spike4 = spike4(7725, 560, 90, 40)
spike5 = spike5(7855, 560, 90, 40)
spike6 = spike6(8345, 560, 790, 40)

# Variavel Plataformas Henesys
platform17 = platform17(8415, 485, 50, 20)
platform18 = platform18(8535, 435, 50, 20)
platform19 = platform19(8415, 375, 50, 30)
platform20 = platform20(8315, 310, 50, 20)
platform21 = platform21(8200, 245, 50, 20)
platform22 = platform22(8200, 155, 50, 20)
platform23 = platform23(8310, 140, 50, 20)
platform24 = platform24(8430, 140, 50, 20)
platform25 = platform25(8550, 140, 50, 20)
platform26 = platform26(8680, 140, 50, 20)
platform27 = platform27(8800, 435, 50, 20)
platform28 = platform28(8910, 400, 50, 20)
platform29 = platform29(9035, 450, 50, 20)
platform30 = platform30(9880, 450, 50, 20)
platform31 = platform31(9700, 375, 145, 20)
platform32 = platform32(9505, 375, 145, 20)
platform33 = platform33(9325, 290, 145, 20)
platform34 = platform34(9505, 225, 145, 20)
platform35 = platform35(9700, 225, 145, 20)
platform36 = platform36(9905, 225, 145, 20)
platform37 = platform37(10085, 300, 145, 20)
platform38 = platform38(10245, 380, 145, 20)
platform39 = platform39(10425, 300, 145, 20)
platform40 = platform40(10350, 190, 50, 20)
platform41 = platform41(10350, 105, 50, 20)
platform42 = platform42(10130, 105, 145, 20)

# Variavel Monstros Henesys
cogu1 = cogu1(7100, 483, 64, 64, 7325)
cogu2 = cogu2(7390, 483, 64, 64, 7556)
cogu3 = cogu3(7930, 483, 64, 64, 8282)
cogu4 = cogu4(8290, 78, 64, 64, 8325)
cogu5 = cogu5(8530, 78, 64, 64, 8565)
cogu6 = cogu6(8775, 372, 64, 64, 8810)
cogu7 = cogu7(9208, 452, 64, 64, 9441)
cogu8 = cogu8(9135, 483, 64, 64, 10707)
cogu9 = cogu9(9700, 311, 64, 64, 9805)
cogu10 = cogu10(9505, 311, 64, 64, 9615)
cogu11 = cogu11(9700, 160, 64, 64, 9805)
cogu12 = cogu12(9505, 160, 64, 64, 9615)
cogu13 = cogu13(10090, 238, 64, 64, 10195)
cogu14 = cogu14(10425, 238, 64, 64, 10530)

# Variável Espinhos Perion
spike7 = spike7(11568, 495, 30, 50)
spike8 = spike8(11795, 507, 35, 40)
spike9 = spike9(11658, 553, 94, 46)

# Variável Plataformas Perion
platform43 = platform43(11980, 460, 30, 20)
platform44 = platform44(12062, 400, 213, 20)
platform45 = platform45(11920, 305, 125, 20)
platform46 = platform46(12062, 212, 213, 20)
platform47 = platform47(12310, 305, 125, 20)
platform48 = platform48(12450, 400, 213, 20)
platform49 = platform49(12450, 212, 213, 20)
platform50 = platform50(12670, 305, 125, 20)
platform51 = platform51(12810, 400, 213, 20)
platform52 = platform52(12810, 212, 213, 20)
platform53 = platform53(13030, 305, 125, 20)
platform54 = platform54(13170, 400, 213, 20)
platform55 = platform55(13170, 212, 213, 20)
platform56 = platform56(13952, 480, 30, 20)
platform57 = platform57(13884, 430, 30, 20)
platform58 = platform58(14020, 430, 30, 20)
platform59 = platform59(13833, 350, 30, 20)
platform60 = platform60(14082, 350, 30, 20)
platform61 = platform61(13790, 270, 30, 20)
platform62 = platform62(14130, 270, 30, 20)
platform63 = platform63(13750, 190, 30, 20)
platform64 = platform64(13900, 120, 900, 20)
platform65 = platform65(13820, 130, 38, 20)
platform66 = platform66(14725, 500, 215, 20)

# Variável Parede Perion
wall1 = wall1(13507, 305, 15, 295)
wall2 = wall2(14802, 0, 48, 600)

# Variável Gate Perion
gate1 = gate1(14691, 281, 64, 64, 14708)

# Variável Objetos Mapa Perion
altar1 = altar1(14637, 453, 64, 64, 14708)

# Variável Monstros Perion
toco1 = toco1(11354, 490, 66, 54, 11501)
toco2 = toco2(12063, 348, 66, 54, 12206)
toco3 = toco3(12063, 159, 66, 54, 12206)
toco4 = toco4(12313, 255, 66, 54, 12362)
toco5 = toco5(12452, 348, 66, 54, 12593)
toco6 = toco6(12452, 159, 66, 54, 12593)
toco7 = toco7(12672, 255, 66, 54, 12722)
toco8 = toco8(12811, 348, 66, 54, 12954)
toco9 = toco9(12811, 159, 66, 54, 12954)
toco10 = toco10(13029, 255, 66, 54, 13083)
toco11 = toco11(13172, 348, 66, 54, 13314)
toco12 = toco12(13172, 159, 66, 54, 13314)
toco13 = toco13(11950, 490, 66, 54, 12654)
toco14 = toco14(12743, 490, 66, 54, 13439)
toco15 = toco15(13903, 67, 66, 54, 14127)
toco16 = toco16(14127, 67, 66, 54, 14417)
stumpy = stumpy(14680, 345, 82, 117, 14426)

# Variável Spikes Ellinias
spike10 = spike10(15485, 555, 2050, 35)

# Variável Wall Ellinia
wall3 = wall3(17861, 61, 26, 496)
wall4 = wall4(18635, 0, 48, 600)

# Variável Plataformas Ellinia
platform67 = platform67(17939, 455, 38, 20)
platform68 = platform68(18420, 449, 38, 20)
platform69 = platform69(17939, 359, 38, 20)
platform70 = platform70(18057, 359, 38, 20)
platform71 = platform71(18181, 359, 38, 20)
platform72 = platform72(18304, 359, 38, 20)
platform73 = platform73(18420, 359, 38, 20)

run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(27)

    # TESTES
    #print("JumpCount:", player.jumpCount, "Camx:", camx, "onPlatform:", player.onPlatform, "isJump:", player.isJump)
    print(camx)
    # print(player.y)
    # print(player.onPlatform)
    # print(player.isJump)
    #print(stumpy.walkCount)


    # Checkpoints
    if camx == 6545:
        checkpoint = 6545

    if camx == 10610:
        checkpoint = 10610

    if camx == 14740:
        checkpoint = 14740

    # BGM de cada cidade
    if camx == 0:
        music = pygame.mixer.music.load("BGM/BGMLOGIN.mp3")
        pygame.mixer.music.play(-1)

    if camx == 1370:
        music = pygame.mixer.music.load("BGM/BGM01.mp3")
        pygame.mixer.music.play(-1)

    if camx == 6400:
        music = pygame.mixer.music.load("BGM/BGM02.mp3")
        pygame.mixer.music.play(-1)

    if camx == 10485:
        music = pygame.mixer.music.load("BGM/BGM03.mp3")
        pygame.mixer.music.play(-1)

    if camx == 14430:
        music = pygame.mixer.music.load("BGM/BGM04.mp3")
        pygame.mixer.music.play(-1)

    # Verificação de GameOver
    if player.health < 0:
        gameover.play()
        win.blit(gameoverpic, (0, 0))
        pygame.display.update()
        pygame.time.delay(5000)
        print(cor.VERMELHO + 'GAMEOVER! Boa sorte da próxima vez.' + cor.FIM)
        break

    # Colisão Monstros Porto Lith
    if player.hitbox[1] < snail1.hitbox[1] + snail1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail1.hitbox[0] and player.hitbox[0] < snail1.hitbox[0] + \
                snail1.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < snail2.hitbox[1] + snail2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail2.hitbox[0] and player.hitbox[0] < snail2.hitbox[0] + \
                snail2.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < snail3.hitbox[1] + snail3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail3.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail3.hitbox[0] and player.hitbox[0] < snail3.hitbox[0] + \
                snail3.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < snail4.hitbox[1] + snail4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail4.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail4.hitbox[0] and player.hitbox[0] < snail4.hitbox[0] + \
                snail4.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < snail5.hitbox[1] + snail5.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail5.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail5.hitbox[0] and player.hitbox[0] < snail5.hitbox[0] + \
                snail5.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < snail6.hitbox[1] + snail6.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail6.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail6.hitbox[0] and player.hitbox[0] < snail6.hitbox[0] + \
                snail6.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < snail7.hitbox[1] + snail7.hitbox[3] and player.hitbox[1] + player.hitbox[3] > snail7.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > snail7.hitbox[0] and player.hitbox[0] < snail7.hitbox[0] + \
                snail7.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Espinhos Porto Lith
    if player.hitbox[1] < spike1.hitbox[1] + spike1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike1.hitbox[0] and player.hitbox[0] < spike1.hitbox[0] + \
                spike1.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < spike2.hitbox[1] + spike2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike2.hitbox[0] and player.hitbox[0] < spike2.hitbox[0] + \
                spike2.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Plataformas Porto Lith
    if player.plathitbox[1] < platform1.hitbox[1] + platform1.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform1.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform1.hitbox[0] and player.plathitbox[0] < \
                platform1.hitbox[0] + platform1.hitbox[2]:
            platform1.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform2.hitbox[1] + platform2.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform2.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform2.hitbox[0] and player.plathitbox[0] < \
                platform2.hitbox[0] + platform2.hitbox[2]:
            platform2.hit()
            player.onPlatform = True

    if player.plathitbox[1] < platform3.hitbox[1] + platform3.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform3.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform3.hitbox[0] and player.plathitbox[0] < \
                platform3.hitbox[0] + platform3.hitbox[2]:
            platform3.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform4.hitbox[1] + platform4.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform4.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform4.hitbox[0] and player.plathitbox[0] < \
                platform4.hitbox[0] + platform4.hitbox[2]:
            platform4.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform5.hitbox[1] + platform5.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform5.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform5.hitbox[0] and player.plathitbox[0] < \
                platform5.hitbox[0] + platform5.hitbox[2]:
            platform5.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform6.hitbox[1] + platform6.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform6.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform6.hitbox[0] and player.plathitbox[0] < \
                platform6.hitbox[0] + platform6.hitbox[2]:
            platform6.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform7.hitbox[1] + platform7.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform7.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform7.hitbox[0] and player.plathitbox[0] < \
                platform7.hitbox[0] + platform7.hitbox[2]:
            platform7.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform8.hitbox[1] + platform8.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform8.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform8.hitbox[0] and player.plathitbox[0] < \
                platform8.hitbox[0] + platform8.hitbox[2]:
            platform8.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform9.hitbox[1] + platform9.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform9.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform9.hitbox[0] and player.plathitbox[0] < \
                platform9.hitbox[0] + platform9.hitbox[2]:
            platform9.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform10.hitbox[1] + platform10.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform10.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform10.hitbox[0] and player.plathitbox[0] < \
                platform10.hitbox[0] + platform10.hitbox[2]:
            platform10.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform11.hitbox[1] + platform11.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform11.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform11.hitbox[0] and player.plathitbox[0] < \
                platform11.hitbox[0] + platform11.hitbox[2]:
            platform11.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform12.hitbox[1] + platform12.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform12.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform12.hitbox[0] and player.plathitbox[0] < \
                platform12.hitbox[0] + platform12.hitbox[2]:
            platform12.hit()
            player.onPlatform = True

    if player.plathitbox[1] < platform13.hitbox[1] + platform13.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform13.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform13.hitbox[0] and player.plathitbox[0] < \
                platform13.hitbox[0] + platform13.hitbox[2]:
            platform13.hit()
            player.onPlatform = True

    if player.plathitbox[1] < platform14.hitbox[1] + platform14.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform14.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform14.hitbox[0] and player.plathitbox[0] < \
                platform14.hitbox[0] + platform14.hitbox[2]:
            platform14.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform15.hitbox[1] + platform15.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform15.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform15.hitbox[0] and player.plathitbox[0] < \
                platform15.hitbox[0] + platform15.hitbox[2]:
            platform15.hit()
            player.onPlatform = True

    if player.plathitbox[1] < platform16.hitbox[1] + platform16.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform16.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform16.hitbox[0] and player.plathitbox[0] < \
                platform16.hitbox[0] + platform16.hitbox[2]:
            platform16.hit()
            player.onPlatform = True

    #Colisão Monstros Henesys
    if player.hitbox[1] < cogu1.hitbox[1] + cogu1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu1.hitbox[0] and player.hitbox[0] < cogu1.hitbox[0] + \
                cogu1.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    if player.hitbox[1] < cogu2.hitbox[1] + cogu2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu2.hitbox[0] and player.hitbox[0] < cogu2.hitbox[0] + \
                cogu2.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu3.hitbox[1] + cogu3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu3.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu3.hitbox[0] and player.hitbox[0] < cogu3.hitbox[0] + \
                cogu3.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu4.hitbox[1] + cogu4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu4.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu4.hitbox[0] and player.hitbox[0] < cogu4.hitbox[0] + \
                cogu4.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu5.hitbox[1] + cogu5.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu5.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu5.hitbox[0] and player.hitbox[0] < cogu5.hitbox[0] + \
                cogu5.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu6.hitbox[1] + cogu6.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu6.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu6.hitbox[0] and player.hitbox[0] < cogu6.hitbox[0] + \
                cogu6.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu7.hitbox[1] + cogu7.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu7.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu7.hitbox[0] and player.hitbox[0] < cogu7.hitbox[0] + \
                cogu7.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu8.hitbox[1] + cogu8.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu8.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu8.hitbox[0] and player.hitbox[0] < cogu8.hitbox[0] + \
                cogu8.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu9.hitbox[1] + cogu9.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu9.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu9.hitbox[0] and player.hitbox[0] < cogu9.hitbox[0] + \
                cogu9.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu10.hitbox[1] + cogu10.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu10.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu10.hitbox[0] and player.hitbox[0] < cogu10.hitbox[0] + \
                cogu10.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu11.hitbox[1] + cogu11.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu11.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu11.hitbox[0] and player.hitbox[0] < cogu11.hitbox[0] + \
                cogu11.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu12.hitbox[1] + cogu12.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu12.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu12.hitbox[0] and player.hitbox[0] < cogu12.hitbox[0] + \
                cogu12.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu13.hitbox[1] + cogu13.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu13.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu13.hitbox[0] and player.hitbox[0] < cogu13.hitbox[0] + \
                cogu13.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < cogu14.hitbox[1] + cogu14.hitbox[3] and player.hitbox[1] + player.hitbox[3] > cogu14.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > cogu14.hitbox[0] and player.hitbox[0] < cogu14.hitbox[0] + \
                cogu14.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Plataformas Henesys
    if player.plathitbox[1] < platform17.hitbox[1] + platform17.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform17.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform17.hitbox[0] and player.plathitbox[0] < \
                platform17.hitbox[0] + platform17.hitbox[2]:
            platform17.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False


    if player.plathitbox[1] < platform18.hitbox[1] + platform18.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform18.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform18.hitbox[0] and player.plathitbox[0] < \
                platform18.hitbox[0] + platform18.hitbox[2]:
            platform18.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform19.hitbox[1] + platform19.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform19.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform19.hitbox[0] and player.plathitbox[0] < \
                platform19.hitbox[0] + platform19.hitbox[2]:
            platform19.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform20.hitbox[1] + platform20.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform20.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform20.hitbox[0] and player.plathitbox[0] < \
                platform20.hitbox[0] + platform20.hitbox[2]:
            platform20.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform21.hitbox[1] + platform21.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform21.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform21.hitbox[0] and player.plathitbox[0] < \
                platform21.hitbox[0] + platform21.hitbox[2]:
            platform21.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform22.hitbox[1] + platform22.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform22.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform22.hitbox[0] and player.plathitbox[0] < \
                platform22.hitbox[0] + platform22.hitbox[2]:
            platform22.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform23.hitbox[1] + platform23.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform23.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform23.hitbox[0] and player.plathitbox[0] < \
                platform23.hitbox[0] + platform23.hitbox[2]:
            platform23.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform24.hitbox[1] + platform24.hitbox[3] and player.plathitbox[1] + player.plathitbox[
        3] > platform24.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform24.hitbox[0] and player.plathitbox[0] < \
                platform24.hitbox[0] + platform24.hitbox[2]:
            platform24.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform25.hitbox[1] + platform25.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform25.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform25.hitbox[0] and player.plathitbox[0] < \
                platform25.hitbox[0] + platform25.hitbox[2]:
            platform25.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform26.hitbox[1] + platform26.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform26.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform26.hitbox[0] and player.plathitbox[0] < \
                platform26.hitbox[0] + platform26.hitbox[2]:
            platform26.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform27.hitbox[1] + platform27.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform27.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform27.hitbox[0] and player.plathitbox[0] < \
                platform27.hitbox[0] + platform27.hitbox[2]:
            platform27.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform28.hitbox[1] + platform28.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform28.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform28.hitbox[0] and player.plathitbox[0] < \
                platform28.hitbox[0] + platform28.hitbox[2]:
            platform28.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform29.hitbox[1] + platform29.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform29.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform29.hitbox[0] and player.plathitbox[0] < \
                platform29.hitbox[0] + platform29.hitbox[2]:
            platform29.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform30.hitbox[1] + platform30.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform30.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform30.hitbox[0] and player.plathitbox[0] < \
                platform30.hitbox[0] + platform30.hitbox[2]:
            platform30.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform31.hitbox[1] + platform31.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform31.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform31.hitbox[0] and player.plathitbox[0] < \
                platform31.hitbox[0] + platform31.hitbox[2]:
            platform31.hit()
            player.onPlatform = True
#        else:
#            player.onPlatform = False

    if player.plathitbox[1] < platform32.hitbox[1] + platform32.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform32.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform32.hitbox[0] and player.plathitbox[0] < \
                platform32.hitbox[0] + platform32.hitbox[2]:
            platform32.hit()
            player.onPlatform = True
#        else:
#            player.onPlatform = False

    if player.plathitbox[1] < platform33.hitbox[1] + platform33.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform33.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform33.hitbox[0] and player.plathitbox[0] < \
                platform33.hitbox[0] + platform33.hitbox[2]:
            platform33.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform34.hitbox[1] + platform34.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform34.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform34.hitbox[0] and player.plathitbox[0] < \
                platform34.hitbox[0] + platform34.hitbox[2]:
            platform34.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform35.hitbox[1] + platform35.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform35.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform35.hitbox[0] and player.plathitbox[0] < \
                platform35.hitbox[0] + platform35.hitbox[2]:
            platform35.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform36.hitbox[1] + platform36.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform36.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform36.hitbox[0] and player.plathitbox[0] < \
                platform36.hitbox[0] + platform36.hitbox[2]:
            platform36.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform37.hitbox[1] + platform37.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform37.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform37.hitbox[0] and player.plathitbox[0] < \
                platform37.hitbox[0] + platform37.hitbox[2]:
            platform37.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform38.hitbox[1] + platform38.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform38.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform38.hitbox[0] and player.plathitbox[0] < \
                platform38.hitbox[0] + platform38.hitbox[2]:
            platform38.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform39.hitbox[1] + platform39.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform39.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform39.hitbox[0] and player.plathitbox[0] < \
                platform39.hitbox[0] + platform39.hitbox[2]:
            platform39.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform40.hitbox[1] + platform40.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform40.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform40.hitbox[0] and player.plathitbox[0] < \
                platform40.hitbox[0] + platform40.hitbox[2]:
            platform40.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform41.hitbox[1] + platform41.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform41.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform41.hitbox[0] and player.plathitbox[0] < \
                platform41.hitbox[0] + platform41.hitbox[2]:
            platform41.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform42.hitbox[1] + platform42.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform42.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform42.hitbox[0] and player.plathitbox[0] < \
                platform42.hitbox[0] + platform42.hitbox[2]:
            platform42.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False
            
            # Colisão Espinhos Henesys
    if player.hitbox[1] < spike3.hitbox[1] + spike3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike3.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike3.hitbox[0] and player.hitbox[0] < spike3.hitbox[0] + \
                spike3.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    if player.hitbox[1] < spike4.hitbox[1] + spike4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike4.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike4.hitbox[0] and player.hitbox[0] < spike4.hitbox[0] + \
                spike4.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    if player.hitbox[1] < spike5.hitbox[1] + spike5.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike5.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike5.hitbox[0] and player.hitbox[0] < spike5.hitbox[0] + \
                spike5.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < spike6.hitbox[1] + spike6.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike6.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike6.hitbox[0] and player.hitbox[0] < spike6.hitbox[0] + \
                spike6.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
    
    # Colisão Espinhos Perion
    if player.hitbox[1] < spike7.hitbox[1] + spike7.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike7.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike7.hitbox[0] and player.hitbox[0] < spike7.hitbox[0] + \
                spike7.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    if player.hitbox[1] < spike8.hitbox[1] + spike8.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike8.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike8.hitbox[0] and player.hitbox[0] < spike8.hitbox[0] + \
                spike8.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    if player.hitbox[1] < spike9.hitbox[1] + spike9.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike9.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike9.hitbox[0] and player.hitbox[0] < spike9.hitbox[0] + \
                spike9.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    # Colisão Plataformas Perion
    if player.plathitbox[1] < platform43.hitbox[1] + platform43.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform43.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform43.hitbox[0] and player.plathitbox[0] < \
                platform43.hitbox[0] + platform43.hitbox[2]:
            platform43.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform44.hitbox[1] + platform44.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform44.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform44.hitbox[0] and player.plathitbox[0] < \
                platform44.hitbox[0] + platform44.hitbox[2]:
            platform44.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform45.hitbox[1] + platform45.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform45.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform45.hitbox[0] and player.plathitbox[0] < \
                platform45.hitbox[0] + platform45.hitbox[2]:
            platform45.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform46.hitbox[1] + platform46.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform46.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform46.hitbox[0] and player.plathitbox[0] < \
                platform46.hitbox[0] + platform46.hitbox[2]:
            platform46.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False

    if player.plathitbox[1] < platform47.hitbox[1] + platform47.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform47.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform47.hitbox[0] and player.plathitbox[0] < \
                platform47.hitbox[0] + platform47.hitbox[2]:
            platform47.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform48.hitbox[1] + platform48.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform48.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform48.hitbox[0] and player.plathitbox[0] < \
                platform48.hitbox[0] + platform48.hitbox[2]:
            platform48.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform49.hitbox[1] + platform49.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform49.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform49.hitbox[0] and player.plathitbox[0] < \
                platform49.hitbox[0] + platform49.hitbox[2]:
            platform49.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform50.hitbox[1] + platform50.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform50.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform50.hitbox[0] and player.plathitbox[0] < \
                platform50.hitbox[0] + platform50.hitbox[2]:
            platform50.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform51.hitbox[1] + platform51.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform51.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform51.hitbox[0] and player.plathitbox[0] < \
                platform51.hitbox[0] + platform51.hitbox[2]:
            platform51.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform52.hitbox[1] + platform52.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform52.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform52.hitbox[0] and player.plathitbox[0] < \
                platform52.hitbox[0] + platform52.hitbox[2]:
            platform52.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform53.hitbox[1] + platform53.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform53.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform53.hitbox[0] and player.plathitbox[0] < \
                platform53.hitbox[0] + platform53.hitbox[2]:
            platform53.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform54.hitbox[1] + platform54.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform54.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform54.hitbox[0] and player.plathitbox[0] < \
                platform54.hitbox[0] + platform54.hitbox[2]:
            platform54.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform55.hitbox[1] + platform55.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform55.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform55.hitbox[0] and player.plathitbox[0] < \
                platform55.hitbox[0] + platform55.hitbox[2]:
            platform55.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform56.hitbox[1] + platform56.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform56.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform56.hitbox[0] and player.plathitbox[0] < \
                platform56.hitbox[0] + platform56.hitbox[2]:
            platform56.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform57.hitbox[1] + platform57.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform57.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform57.hitbox[0] and player.plathitbox[0] < \
                platform57.hitbox[0] + platform57.hitbox[2]:
            platform57.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform58.hitbox[1] + platform58.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform58.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform58.hitbox[0] and player.plathitbox[0] < \
                platform58.hitbox[0] + platform58.hitbox[2]:
            platform58.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform59.hitbox[1] + platform59.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform59.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform59.hitbox[0] and player.plathitbox[0] < \
                platform59.hitbox[0] + platform59.hitbox[2]:
            platform59.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform60.hitbox[1] + platform60.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform60.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform60.hitbox[0] and player.plathitbox[0] < \
                platform60.hitbox[0] + platform60.hitbox[2]:
            platform60.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform61.hitbox[1] + platform61.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform61.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform61.hitbox[0] and player.plathitbox[0] < \
                platform61.hitbox[0] + platform61.hitbox[2]:
            platform61.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform62.hitbox[1] + platform62.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform62.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform62.hitbox[0] and player.plathitbox[0] < \
                platform62.hitbox[0] + platform62.hitbox[2]:
            platform62.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform63.hitbox[1] + platform63.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform63.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform63.hitbox[0] and player.plathitbox[0] < \
                platform63.hitbox[0] + platform63.hitbox[2]:
            platform63.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform64.hitbox[1] + platform64.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform64.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform64.hitbox[0] and player.plathitbox[0] < \
                platform64.hitbox[0] + platform64.hitbox[2]:
            platform64.hit()
            player.onPlatform = True
        else:
            player.onPlatform = False
        
    if player.plathitbox[1] < platform65.hitbox[1] + platform65.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform65.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform65.hitbox[0] and player.plathitbox[0] < \
                platform65.hitbox[0] + platform65.hitbox[2]:
            platform65.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform66.hitbox[1] + platform66.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform66.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform66.hitbox[0] and player.plathitbox[0] < \
                platform66.hitbox[0] + platform66.hitbox[2]:
            platform66.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

#Colisão Plataformas Ellinia
    if player.plathitbox[1] < platform67.hitbox[1] + platform67.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform67.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform67.hitbox[0] and player.plathitbox[0] < \
                platform67.hitbox[0] + platform67.hitbox[2]:
            platform67.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform68.hitbox[1] + platform68.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform68.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform68.hitbox[0] and player.plathitbox[0] < \
                platform68.hitbox[0] + platform68.hitbox[2]:
            platform68.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform69.hitbox[1] + platform69.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform69.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform69.hitbox[0] and player.plathitbox[0] < \
                platform69.hitbox[0] + platform69.hitbox[2]:
            platform69.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform70.hitbox[1] + platform70.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform70.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform70.hitbox[0] and player.plathitbox[0] < \
                platform70.hitbox[0] + platform70.hitbox[2]:
            platform70.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform71.hitbox[1] + platform71.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform71.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform71.hitbox[0] and player.plathitbox[0] < \
                platform71.hitbox[0] + platform71.hitbox[2]:
            platform71.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform72.hitbox[1] + platform72.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform72.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform72.hitbox[0] and player.plathitbox[0] < \
                platform72.hitbox[0] + platform72.hitbox[2]:
            platform72.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform73.hitbox[1] + platform73.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform73.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform73.hitbox[0] and player.plathitbox[0] < \
                platform73.hitbox[0] + platform73.hitbox[2]:
            platform73.hit()
            player.onPlatform = True
        #else:
            #player.onPlatform = False
        
# Colisão Monstros Perion
    if player.hitbox[1] < toco1.hitbox[1] + toco1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco1.hitbox[0] and player.hitbox[0] < toco1.hitbox[0] + \
                toco1.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco2.hitbox[1] + toco2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco2.hitbox[0] and player.hitbox[0] < toco2.hitbox[0] + \
                toco2.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco3.hitbox[1] + toco3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco3.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco3.hitbox[0] and player.hitbox[0] < toco3.hitbox[0] + \
                toco3.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco4.hitbox[1] + toco4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco4.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco4.hitbox[0] and player.hitbox[0] < toco4.hitbox[0] + \
                toco4.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco5.hitbox[1] + toco5.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco5.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco5.hitbox[0] and player.hitbox[0] < toco5.hitbox[0] + \
                toco5.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco6.hitbox[1] + toco6.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco6.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco6.hitbox[0] and player.hitbox[0] < toco6.hitbox[0] + \
                toco6.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco7.hitbox[1] + toco7.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco7.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco7.hitbox[0] and player.hitbox[0] < toco7.hitbox[0] + \
                toco7.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco8.hitbox[1] + toco8.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco8.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco8.hitbox[0] and player.hitbox[0] < toco8.hitbox[0] + \
                toco8.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco9.hitbox[1] + toco9.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco9.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco9.hitbox[0] and player.hitbox[0] < toco9.hitbox[0] + \
                toco9.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco10.hitbox[1] + toco10.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco10.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco10.hitbox[0] and player.hitbox[0] < toco10.hitbox[0] + \
                toco10.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco11.hitbox[1] + toco11.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco11.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco11.hitbox[0] and player.hitbox[0] < toco11.hitbox[0] + \
                toco11.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco12.hitbox[1] + toco12.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco12.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco12.hitbox[0] and player.hitbox[0] < toco12.hitbox[0] + \
                toco12.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco13.hitbox[1] + toco13.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco13.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco13.hitbox[0] and player.hitbox[0] < toco13.hitbox[0] + \
                toco13.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco14.hitbox[1] + toco14.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco14.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco14.hitbox[0] and player.hitbox[0] < toco14.hitbox[0] + \
                toco14.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco15.hitbox[1] + toco15.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco15.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco15.hitbox[0] and player.hitbox[0] < toco15.hitbox[0] + \
                toco15.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < toco16.hitbox[1] + toco16.hitbox[3] and player.hitbox[1] + player.hitbox[3] > toco16.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > toco16.hitbox[0] and player.hitbox[0] < toco16.hitbox[0] + \
                toco16.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
    
    #Colisão Hitbox Stumpy
    if player.hitbox[1] < stumpy.hitbox[1] + stumpy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > stumpy.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > stumpy.hitbox[0] and player.hitbox[0] < stumpy.hitbox[0] + \
                stumpy.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    # Colisão Skill Stumpy
    if stumpy.walkCount == 40 and player.y == 470 and camx > 13955 and stumpy.visible == True:
        player.hit()
        life -= 1
        player.health -= 1
        camx = checkpoint
        player.x = 400
        player.y = 470

    if stumpy.walkCount == 80 and stumpy.visible == True and camx > 13910:
        stumpyskill.play()

    if stumpy.walkCount == 40 and camx >= 14225 and player.y > 300 and stumpy.visible == True:
        player.hit()
        life -= 1
        player.health -= 1
        camx = checkpoint
        player.x = 400
        player.y = 470

# Colisão Parede Perion
    if player.plathitbox[1] < wall1.hitbox[1] + wall1.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall1.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall1.hitbox[0] and player.plathitbox[0] < \
                wall1.hitbox[0] + wall1.hitbox[2]:
            camx -= 5
            player.walkCount = 0

    if stumpy.visible:
        if player.plathitbox[1] < wall2.hitbox[1] + wall2.hitbox[3] and player.plathitbox[1] + \
                player.plathitbox[
                    3] > wall2.hitbox[1]:
            if player.plathitbox[0] + player.plathitbox[2] > wall2.hitbox[0] and player.plathitbox[0] < \
                    wall2.hitbox[0] + wall2.hitbox[2]:
                camx -= 5
                player.walkCount = 0

# Colisão Parede Ellinia
    if player.plathitbox[1] < wall3.hitbox[1] + wall3.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall3.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall3.hitbox[0] and player.plathitbox[0] < \
                wall3.hitbox[0] + wall3.hitbox[2]:
            camx += 5
            player.walkCount = 0
            
    if player.plathitbox[1] < wall4.hitbox[1] + wall4.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall4.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall4.hitbox[0] and player.plathitbox[0] < \
                wall4.hitbox[0] + wall4.hitbox[2]:
            camx -= 5
            player.walkCount = 0
            
    # Colisão Spike Ellinia
    if player.hitbox[1] < spike10.hitbox[1] + spike10.hitbox[3] and player.hitbox[1] + player.hitbox[3] > spike10.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > spike10.hitbox[0] and player.hitbox[0] < spike10.hitbox[0] + \
                spike10.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Funções da Gravidade
    if player.y < 470 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 10
        onGravity = True
    else:
        onGravity = False

    # Gravidade / Buracos Porto Lith
    if camx > 3330 and camx <= 3395 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 4815 and camx < 5660 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    # Gravidade / Buracos Henesys
    elif camx > 7295 and camx <= 7365 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 7425 and camx <= 7495 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 7915 and camx <= 8685 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    # Gravidade / Buracos Perion
    elif camx > 11220 and camx <= 11310 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    # Gravidade / Buracos Ellinia
    elif camx > 15060 and camx <= 15145 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 15210 and camx <= 15300 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 15360 and camx <= 15460 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 15520 and camx <= 15610 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 15670 and camx <= 15770 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 16350 and camx <= 16440 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 16510 and camx <= 16595 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 16660 and camx <= 16755 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 16820 and camx <= 16905 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 16970 and camx <= 17060 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif player.y > 470:
        player.y = 470



    # Colisão Flechas
    for arrow in arrows:
        # Colisão Flechas Monstros Porto Lith
        if arrow.y - arrow.radius < snail1.hitbox[1] + snail1.hitbox[3] and arrow.y + arrow.radius > snail1.hitbox[1]:
            if arrow.x + arrow.radius > snail1.hitbox[0] and arrow.x - arrow.radius < snail1.hitbox[0] + snail1.hitbox[
                2]:
                snail1.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail2.hitbox[1] + snail2.hitbox[3] and arrow.y + arrow.radius > snail2.hitbox[1]:
            if arrow.x + arrow.radius > snail2.hitbox[0] and arrow.x - arrow.radius < snail2.hitbox[0] + snail2.hitbox[
                2]:
                snail2.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail3.hitbox[1] + snail3.hitbox[3] and arrow.y + arrow.radius > snail3.hitbox[1]:
            if arrow.x + arrow.radius > snail3.hitbox[0] and arrow.x - arrow.radius < snail3.hitbox[0] + snail3.hitbox[
                2]:
                snail3.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail4.hitbox[1] + snail4.hitbox[3] and arrow.y + arrow.radius > snail4.hitbox[1]:
            if arrow.x + arrow.radius > snail4.hitbox[0] and arrow.x - arrow.radius < snail4.hitbox[0] + snail4.hitbox[
                2]:
                snail4.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail5.hitbox[1] + snail5.hitbox[3] and arrow.y + arrow.radius > snail5.hitbox[1]:
            if arrow.x + arrow.radius > snail5.hitbox[0] and arrow.x - arrow.radius < snail5.hitbox[0] + snail5.hitbox[
                2]:
                snail5.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail6.hitbox[1] + snail6.hitbox[3] and arrow.y + arrow.radius > snail6.hitbox[1]:
            if arrow.x + arrow.radius > snail6.hitbox[0] and arrow.x - arrow.radius < snail6.hitbox[0] + snail6.hitbox[
                2]:
                snail6.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail7.hitbox[1] + snail7.hitbox[3] and arrow.y + arrow.radius > snail7.hitbox[1]:
            if arrow.x + arrow.radius > snail7.hitbox[0] and arrow.x - arrow.radius < snail7.hitbox[0] + snail7.hitbox[
                2]:
                snail7.hit()
                arrows.pop(arrows.index(arrow))

        # Colisão Flechas Henesys
        if arrow.y - arrow.radius < cogu1.hitbox[1] + cogu1.hitbox[3] and arrow.y + arrow.radius > cogu1.hitbox[1]:
            if arrow.x + arrow.radius > cogu1.hitbox[0] and arrow.x - arrow.radius < cogu1.hitbox[0] + cogu1.hitbox[
                2]:
                cogu1.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu2.hitbox[1] + cogu2.hitbox[3] and arrow.y + arrow.radius > cogu2.hitbox[1]:
            if arrow.x + arrow.radius > cogu2.hitbox[0] and arrow.x - arrow.radius < cogu2.hitbox[0] + cogu2.hitbox[
                2]:
                cogu2.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu3.hitbox[1] + cogu3.hitbox[3] and arrow.y + arrow.radius > cogu3.hitbox[1]:
            if arrow.x + arrow.radius > cogu3.hitbox[0] and arrow.x - arrow.radius < cogu3.hitbox[0] + cogu3.hitbox[
                2]:
                cogu3.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu4.hitbox[1] + cogu4.hitbox[3] and arrow.y + arrow.radius > cogu4.hitbox[1]:
            if arrow.x + arrow.radius > cogu4.hitbox[0] and arrow.x - arrow.radius < cogu4.hitbox[0] + cogu4.hitbox[
                2]:
                cogu4.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu5.hitbox[1] + cogu5.hitbox[3] and arrow.y + arrow.radius > cogu5.hitbox[1]:
            if arrow.x + arrow.radius > cogu5.hitbox[0] and arrow.x - arrow.radius < cogu5.hitbox[0] + cogu5.hitbox[
                2]:
                cogu5.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu6.hitbox[1] + cogu6.hitbox[3] and arrow.y + arrow.radius > cogu6.hitbox[1]:
            if arrow.x + arrow.radius > cogu6.hitbox[0] and arrow.x - arrow.radius < cogu6.hitbox[0] + cogu6.hitbox[
                2]:
                cogu6.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu7.hitbox[1] + cogu7.hitbox[3] and arrow.y + arrow.radius > cogu7.hitbox[1]:
            if arrow.x + arrow.radius > cogu7.hitbox[0] and arrow.x - arrow.radius < cogu7.hitbox[0] + cogu7.hitbox[
                2]:
                cogu7.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu8.hitbox[1] + cogu8.hitbox[3] and arrow.y + arrow.radius > cogu8.hitbox[1]:
            if arrow.x + arrow.radius > cogu8.hitbox[0] and arrow.x - arrow.radius < cogu8.hitbox[0] + cogu8.hitbox[
                2]:
                cogu8.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu9.hitbox[1] + cogu9.hitbox[3] and arrow.y + arrow.radius > cogu9.hitbox[1]:
            if arrow.x + arrow.radius > cogu9.hitbox[0] and arrow.x - arrow.radius < cogu9.hitbox[0] + cogu9.hitbox[
                2]:
                cogu9.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu10.hitbox[1] + cogu10.hitbox[3] and arrow.y + arrow.radius > cogu10.hitbox[1]:
            if arrow.x + arrow.radius > cogu10.hitbox[0] and arrow.x - arrow.radius < cogu10.hitbox[0] + cogu10.hitbox[
                2]:
                cogu10.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu11.hitbox[1] + cogu11.hitbox[3] and arrow.y + arrow.radius > cogu11.hitbox[1]:
            if arrow.x + arrow.radius > cogu11.hitbox[0] and arrow.x - arrow.radius < cogu11.hitbox[0] + cogu11.hitbox[
                2]:
                cogu11.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu12.hitbox[1] + cogu12.hitbox[3] and arrow.y + arrow.radius > cogu12.hitbox[1]:
            if arrow.x + arrow.radius > cogu12.hitbox[0] and arrow.x - arrow.radius < cogu12.hitbox[0] + cogu12.hitbox[
                2]:
                cogu12.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu13.hitbox[1] + cogu13.hitbox[3] and arrow.y + arrow.radius > cogu13.hitbox[1]:
            if arrow.x + arrow.radius > cogu13.hitbox[0] and arrow.x - arrow.radius < cogu13.hitbox[0] + cogu13.hitbox[
                2]:
                cogu13.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu14.hitbox[1] + cogu14.hitbox[3] and arrow.y + arrow.radius > cogu14.hitbox[1]:
            if arrow.x + arrow.radius > cogu14.hitbox[0] and arrow.x - arrow.radius < cogu14.hitbox[0] + cogu14.hitbox[
                2]:
                cogu14.hit()
                arrows.pop(arrows.index(arrow))

    # Colisão Flechas Perion
        if arrow.y - arrow.radius < toco1.hitbox[1] + toco1.hitbox[3] and arrow.y + arrow.radius > toco1.hitbox[1]:
            if arrow.x + arrow.radius > toco1.hitbox[0] and arrow.x - arrow.radius < toco1.hitbox[0] + toco1.hitbox[
                2]:
                toco1.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco2.hitbox[1] + toco2.hitbox[3] and arrow.y + arrow.radius > toco2.hitbox[1]:
            if arrow.x + arrow.radius > toco2.hitbox[0] and arrow.x - arrow.radius < toco2.hitbox[0] + toco2.hitbox[
                2]:
                toco2.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco3.hitbox[1] + toco3.hitbox[3] and arrow.y + arrow.radius > toco3.hitbox[1]:
            if arrow.x + arrow.radius > toco3.hitbox[0] and arrow.x - arrow.radius < toco3.hitbox[0] + toco3.hitbox[
                2]:
                toco3.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco4.hitbox[1] + toco4.hitbox[3] and arrow.y + arrow.radius > toco4.hitbox[1]:
            if arrow.x + arrow.radius > toco4.hitbox[0] and arrow.x - arrow.radius < toco4.hitbox[0] + toco4.hitbox[
                2]:
                toco4.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco5.hitbox[1] + toco5.hitbox[3] and arrow.y + arrow.radius > toco5.hitbox[1]:
            if arrow.x + arrow.radius > toco5.hitbox[0] and arrow.x - arrow.radius < toco5.hitbox[0] + toco5.hitbox[
                2]:
                toco5.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco6.hitbox[1] + toco6.hitbox[3] and arrow.y + arrow.radius > toco6.hitbox[1]:
            if arrow.x + arrow.radius > toco6.hitbox[0] and arrow.x - arrow.radius < toco6.hitbox[0] + toco6.hitbox[
                2]:
                toco6.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco7.hitbox[1] + toco7.hitbox[3] and arrow.y + arrow.radius > toco7.hitbox[1]:
            if arrow.x + arrow.radius > toco7.hitbox[0] and arrow.x - arrow.radius < toco7.hitbox[0] + toco7.hitbox[
                2]:
                toco7.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco8.hitbox[1] + toco8.hitbox[3] and arrow.y + arrow.radius > toco8.hitbox[1]:
            if arrow.x + arrow.radius > toco8.hitbox[0] and arrow.x - arrow.radius < toco8.hitbox[0] + toco8.hitbox[
                2]:
                toco8.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco9.hitbox[1] + toco9.hitbox[3] and arrow.y + arrow.radius > toco9.hitbox[1]:
            if arrow.x + arrow.radius > toco9.hitbox[0] and arrow.x - arrow.radius < toco9.hitbox[0] + toco9.hitbox[
                2]:
                toco9.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco10.hitbox[1] + toco10.hitbox[3] and arrow.y + arrow.radius > toco10.hitbox[1]:
            if arrow.x + arrow.radius > toco10.hitbox[0] and arrow.x - arrow.radius < toco10.hitbox[0] + toco10.hitbox[
                2]:
                toco10.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco11.hitbox[1] + toco11.hitbox[3] and arrow.y + arrow.radius > toco11.hitbox[1]:
            if arrow.x + arrow.radius > toco11.hitbox[0] and arrow.x - arrow.radius < toco11.hitbox[0] + toco11.hitbox[
                2]:
                toco11.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco12.hitbox[1] + toco12.hitbox[3] and arrow.y + arrow.radius > toco12.hitbox[1]:
            if arrow.x + arrow.radius > toco12.hitbox[0] and arrow.x - arrow.radius < toco12.hitbox[0] + toco12.hitbox[
                2]:
                toco12.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco13.hitbox[1] + toco13.hitbox[3] and arrow.y + arrow.radius > toco13.hitbox[1]:
            if arrow.x + arrow.radius > toco13.hitbox[0] and arrow.x - arrow.radius < toco13.hitbox[0] + toco13.hitbox[
                2]:
                toco13.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco14.hitbox[1] + toco14.hitbox[3] and arrow.y + arrow.radius > toco14.hitbox[1]:
            if arrow.x + arrow.radius > toco14.hitbox[0] and arrow.x - arrow.radius < toco14.hitbox[0] + toco14.hitbox[
                2]:
                toco14.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco15.hitbox[1] + toco15.hitbox[3] and arrow.y + arrow.radius > toco15.hitbox[1]:
            if arrow.x + arrow.radius > toco15.hitbox[0] and arrow.x - arrow.radius < toco15.hitbox[0] + toco15.hitbox[
                2]:
                toco15.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco16.hitbox[1] + toco16.hitbox[3] and arrow.y + arrow.radius > toco16.hitbox[1]:
            if arrow.x + arrow.radius > toco16.hitbox[0] and arrow.x - arrow.radius < toco16.hitbox[0] + toco16.hitbox[
                2]:
                toco16.hit()
                arrows.pop(arrows.index(arrow))

        #Colisão Flecha Stumpy
        if arrow.y - arrow.radius < stumpy.hitbox[1] + stumpy.hitbox[3] and arrow.y + arrow.radius > stumpy.hitbox[1]:
            if arrow.x + arrow.radius > stumpy.hitbox[0] and arrow.x - arrow.radius < stumpy.hitbox[0] + stumpy.hitbox[
                2]:
                stumpy.hit()
                arrows.pop(arrows.index(arrow))

        if arrow.x < 780 and arrow.x > 0:
            arrow.x += arrow.vel
        else:
            if arrows != []: # if utilizado para corrigir o bug que tenta deletar uma flecha que já foi deletada ao colidir com um monstro.
                arrows.pop(arrows.index(arrow))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print(cor.VERMELHO + "Finalizando o jogo..." + cor.FIM)

    # Controles do jogo
    # Seta esquerda (Andar)
    if keys[pygame.K_LEFT] and player.x > player.vel and player.x - camx < 400:
        player.left = True
        player.right = False
        player.facing = 0
        camx -= 5

    # Seta direita (Andar)
    elif keys[pygame.K_RIGHT] and player.x < 800 - player.width - player.vel:
        player.right = True
        player.left = False
        player.facing = 1
        camx += 5

    # Tecla X (Atacar)
    elif keys[pygame.K_x]:
        player.right = False
        player.left = False
        player.attack = True
        if player.facing == 0:
            facingB = -1
        else:
            facingB = 1
        if player.jumpCount == 10:
            if len(arrows) < 1:
                arrows.append(
                    projectile(round(player.x + player.width // 2), round(player.y + player.height // 1.7), 13, facingB))
                arrowSound.play()

    # Tecla F2 (Emote sorrir)
    elif keys[pygame.K_F2]:
        player.smile = True
        player.right = False
        player.left = False
        player.attack = False
    else:
        player.right = False
        player.left = False
        player.attack = False
        player.smile = False
        player.walkCount = 0
        player.attackCount = 0

    # Tecla espaço (Pular)
    if player.isJump == False:
        if onGravity == False:
            if keys[pygame.K_SPACE]:
                player.isJump = True
                player.right = False
                player.left = False
                player.walkCount = 0
                player.attackCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= round((player.jumpCount ** 2) / 4 * neg)
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    GameWindow()

pygame.quit()
