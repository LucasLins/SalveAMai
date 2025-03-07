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
bg3 = pygame.image.load('imagens/Mapa/mapa3.png')
bg4 = pygame.image.load('imagens/Mapa/mapa4.png')
parede = pygame.image.load('imagens/Mapa/Parede.png')
teclas = pygame.image.load('imagens/Misc/keys.png')
icone = pygame.image.load('imagens/Misc/icone.png')
diepic = pygame.image.load('imagens/Mapa/die.png')
gameoverpic = pygame.image.load('imagens/Mapa/gameover.png')
vidas3 = pygame.image.load('imagens/Mapa/vidas3.png')
vidas2 = pygame.image.load('imagens/Mapa/vidas2.png')
vidas1 = pygame.image.load('imagens/Mapa/vidas1.png')
vidas0 = pygame.image.load('imagens/Mapa/vidas0.png')
keys0 = pygame.image.load('imagens/Misc/keys0.png')
keys1 = pygame.image.load('imagens/Misc/keys1.png')
keys2 = pygame.image.load('imagens/Misc/keys2.png')
keys3 = pygame.image.load('imagens/Misc/keys3.png')
keys4 = pygame.image.load('imagens/Misc/keys4.png')
keys5 = pygame.image.load('imagens/Misc/keys5.png')
keys6 = pygame.image.load('imagens/Misc/keys6.png')
keys7 = pygame.image.load('imagens/Misc/keys7.png')
detonado = pygame.image.load('imagens/Mapa/detonado.png')
errado = pygame.image.load('imagens/Mapa/errado.png')
faltakeys = pygame.image.load('imagens/Mapa/faltakeys.png')
quest = pygame.image.load('imagens/Misc/quest.png')
skybg = pygame.image.load('imagens/Mapa/skybg.png')

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
tp = pygame.mixer.Sound("BGM/tp.wav")
portal = pygame.mixer.Sound("BGM/portal.wav")
leverturn = pygame.mixer.Sound("BGM/leverturn.wav")
portalopen1 = pygame.mixer.Sound("BGM/gate1.wav")
portalopen2 = pygame.mixer.Sound("BGM/gate2.wav")
loot = pygame.mixer.Sound("BGM/loot.wav")

## Sons/Monstros
hitSound = pygame.mixer.Sound("BGM/hit.wav")
snaildie = pygame.mixer.Sound("BGM/snaildie.wav")
cogudie = pygame.mixer.Sound("BGM/cogudie.wav")
tocodie = pygame.mixer.Sound("BGM/tocodie.wav")
tocohit = pygame.mixer.Sound("BGM/tocohit.wav")
stumpyhit = pygame.mixer.Sound("BGM/stumpyhit.wav")
stumpydie = pygame.mixer.Sound("BGM/stumpydie.wav")
stumpyskill = pygame.mixer.Sound("BGM/stumpyskill.wav")
kslimeskill = pygame.mixer.Sound("BGM/kslimeskill.wav")
kslimehit = pygame.mixer.Sound("BGM/kslimehit.wav")
slimedie = pygame.mixer.Sound("BGM/slimedie.wav")
slimehit = pygame.mixer.Sound("BGM/slimehit.wav")
laserhit = pygame.mixer.Sound("BGM/laser.wav")
digaodie = pygame.mixer.Sound("BGM/digaodie.wav")
digaohit = pygame.mixer.Sound("BGM/digaohit.wav")
jailopen = pygame.mixer.Sound("BGM/jailopen.wav")
digaoskill1 = pygame.mixer.Sound("BGM/digaoskill1.wav")
digaoskill2 = pygame.mixer.Sound("BGM/digaoskill2.wav")
digaoskill3 = pygame.mixer.Sound("BGM/digaoskill3.wav")
jarexp = pygame.mixer.Sound("BGM/jarexp.wav")

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
        self.keys = 0

    def draw(self, win):
        if self.attackCount + 1 >= 24:
            self.attackCount = 0

        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if self.left:
            if self.jumpCount < 10:
                win.blit(jumpL, (round(self.x), round(self.y)))
            else:
                if onGravity == False:
                    win.blit(walkL[self.walkCount // 6], (round(self.x), round(self.y)))
                    self.walkCount += 1
            if onGravity == True:
                win.blit(jumpL, (round(self.x), round(self.y)))

        elif self.right:
            if self.jumpCount < 10:
                win.blit(jumpR, (round(self.x), round(self.y)))
            else:
                if onGravity == False:
                    win.blit(walkR[self.walkCount // 6], (round(self.x), round(self.y)))
                    self.walkCount += 1
            if onGravity == True:
                win.blit(jumpR, (round(self.x), round(self.y)))
        elif self.jumpCount < 10 and self.facing == 0:
            win.blit(jumpL, (round(self.x), round(self.y)))

        elif self.jumpCount < 10 and self.facing == 1:
            win.blit(jumpR, (round(self.x), round(self.y)))

        elif onGravity == True and self.facing == 1:
            win.blit(jumpR, (round(self.x), round(self.y)))

        elif onGravity == True and self.facing == 0:
            win.blit(jumpL, (round(self.x), round(self.y)))

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
        #pygame.draw.rect(win, (255, 0, 0), self.plathitbox, 2)

    def hit(self):
        if self.health >= 1:
            die.play()
            win.blit(diepic, (0, 0))
            pygame.display.update()
            self.x = 654
            self.y = 361
            self.walkCount = 0
            self.jumpCount = 10
            self.isJump = False
            pygame.time.delay(3000)


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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class spike2(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class spike4(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class spike5(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class spike6(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 15, self.hitbox[1] - 15, 45 - (7 * (6 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class spike8(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class spike9(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class wall2(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class wall4(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        # self.move()
        if stumpy.visible:
            if self.walkCount + 1 >= 32:
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


# Gate Ellinia
class gate2(object):
    walkR = [pygame.image.load('imagens/Mob/Gate2/1.png'), pygame.image.load('imagens/Mob/Gate2/2.png'),
             pygame.image.load('imagens/Mob/Gate2/3.png'), pygame.image.load('imagens/Mob/Gate2/4.png'),
             pygame.image.load('imagens/Mob/Gate2/5.png'), pygame.image.load('imagens/Mob/Gate2/6.png'),
             pygame.image.load('imagens/Mob/Gate2/7.png'), pygame.image.load('imagens/Mob/Gate2/8.png')]

    walkL = [pygame.image.load('imagens/Mob/Gate2/1.png'), pygame.image.load('imagens/Mob/Gate2/2.png'),
             pygame.image.load('imagens/Mob/Gate2/3.png'), pygame.image.load('imagens/Mob/Gate2/4.png'),
             pygame.image.load('imagens/Mob/Gate2/5.png'), pygame.image.load('imagens/Mob/Gate2/6.png'),
             pygame.image.load('imagens/Mob/Gate2/7.png'), pygame.image.load('imagens/Mob/Gate2/8.png')]

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
        if slime9.visible or slime10.visible or KSlime.visible:
            if self.walkCount + 1 >= 32:
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
        # self.move()
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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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


class stumpy(object):  # Boss perion
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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] - 48, self.hitbox[1] - 78, 183 - (2 * (89 - self.health)), 4))
            self.hitbox = (self.x - camx + 50, self.y + 80, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
                key4.visible = True
                stumpydie.play()
                sucesso.play()

            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                key4.visible = True
                stumpydie.play()
                sucesso.play()
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
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# Objetos Monstros Ellinia
class slime1(object):
    walkR = [pygame.image.load('imagens/Mob/Slime/SR1.png'), pygame.image.load('imagens/Mob/Slime/SR2.png'),
             pygame.image.load('imagens/Mob/Slime/SR3.png'), pygame.image.load('imagens/Mob/Slime/SR4.png'),
             pygame.image.load('imagens/Mob/Slime/SR5.png'), pygame.image.load('imagens/Mob/Slime/SR6.png'),
             pygame.image.load('imagens/Mob/Slime/SR7.png')]

    walkL = [pygame.image.load('imagens/Mob/Slime/SL1.png'), pygame.image.load('imagens/Mob/Slime/SL2.png'),
             pygame.image.load('imagens/Mob/Slime/SL3.png'), pygame.image.load('imagens/Mob/Slime/SL4.png'),
             pygame.image.load('imagens/Mob/Slime/SL5.png'), pygame.image.load('imagens/Mob/Slime/SL6.png'),
             pygame.image.load('imagens/Mob/Slime/SL7.png')]

    RHS = pygame.image.load('imagens/Mob/Slime/SHR.png')
    LHS = pygame.image.load('imagens/Mob/Slime/SHL.png')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
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
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime2(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime3(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime4(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime5(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime6(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime7(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime8(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
            else:
                self.washit = 0


class slime9(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
                if slime10.visible == False and KSlime.visible == False:
                    sucesso.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
                if slime10.visible == False and KSlime.visible == False:
                    sucesso.play()
            else:
                self.washit = 0


class slime10(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 28:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(slime1.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(slime1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            if self.washit == 1:
                win.blit(slime1.RHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            elif self.washit == 2:
                win.blit(slime1.LHS, (round(self.x - camx), round(self.y)))
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 17, 49, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 10, self.hitbox[1] - 15, 45 - (4 * (10 - self.health)), 4))
            self.hitbox = (self.x - camx, self.y + 30, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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
        slimehit.play()
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
                slimedie.play()
                if slime9.visible == False and KSlime.visible == False:
                    sucesso.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                slimedie.play()
                if slime9.visible == False and KSlime.visible == False:
                    sucesso.play()
            else:
                self.washit = 0


class KSlime(object):  # Boss Ellinia
    walkR = [pygame.image.load('imagens/Mob/KSlime/SR1.png'), pygame.image.load('imagens/Mob/KSlime/SR2.png'),
             pygame.image.load('imagens/Mob/KSlime/SR3.png'), pygame.image.load('imagens/Mob/KSlime/SR4.png'),
             pygame.image.load('imagens/Mob/KSlime/SR5.png'), pygame.image.load('imagens/Mob/KSlime/SR6.png'),
             pygame.image.load('imagens/Mob/KSlime/SR7.png')]

    walkL = [pygame.image.load('imagens/Mob/KSlime/SL1.png'), pygame.image.load('imagens/Mob/KSlime/SL2.png'),
             pygame.image.load('imagens/Mob/KSlime/SL3.png'), pygame.image.load('imagens/Mob/KSlime/SL4.png'),
             pygame.image.load('imagens/Mob/KSlime/SL5.png'), pygame.image.load('imagens/Mob/KSlime/SL6.png'),
             pygame.image.load('imagens/Mob/KSlime/SL7.png')]

    skillR = [pygame.image.load('imagens/Mob/KSlime/KR1.png'), pygame.image.load('imagens/Mob/KSlime/KR2.png'),
              pygame.image.load('imagens/Mob/KSlime/KR3.png'), pygame.image.load('imagens/Mob/KSlime/KR4.png'),
              pygame.image.load('imagens/Mob/KSlime/KR5.png'), pygame.image.load('imagens/Mob/KSlime/KR6.png'),
              pygame.image.load('imagens/Mob/KSlime/KR7.png'), pygame.image.load('imagens/Mob/KSlime/KR8.png'),
              pygame.image.load('imagens/Mob/KSlime/KR9.png'), pygame.image.load('imagens/Mob/KSlime/KR10.png'),
              pygame.image.load('imagens/Mob/KSlime/KR11.png')]

    skillL = [pygame.image.load('imagens/Mob/KSlime/KL1.png'), pygame.image.load('imagens/Mob/KSlime/KL2.png'),
              pygame.image.load('imagens/Mob/KSlime/KL3.png'), pygame.image.load('imagens/Mob/KSlime/KL4.png'),
              pygame.image.load('imagens/Mob/KSlime/KL5.png'), pygame.image.load('imagens/Mob/KSlime/KL6.png'),
              pygame.image.load('imagens/Mob/KSlime/KL7.png'), pygame.image.load('imagens/Mob/KSlime/KL8.png'),
              pygame.image.load('imagens/Mob/KSlime/KL9.png'), pygame.image.load('imagens/Mob/KSlime/KL10.png'),
              pygame.image.load('imagens/Mob/KSlime/KL11.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.skillCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 89
        self.visible = True
        self.skill = False

    def draw(self, win):
        self.move()
        self.Skill()
        if self.visible and self.skill == False:
            if self.walkCount + 1 >= 28:
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
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] - 30, self.hitbox[1] - 80, 187, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] - 28, self.hitbox[1] - 78, 183 - (2 * (89 - self.health)), 4))
            self.hitbox = (self.x - camx + 30, self.y + 80, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.skill == False:
                if self.x < self.path[1] + self.vel:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    self.walkCount = 0
        else:
            if self.skill == False:
                if self.x > self.path[0] - self.vel:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.x += self.vel
                    self.walkCount = 0

    def Skill(self):
        if self.visible and self.skill == True:
            if self.skillCount + 1 >= 55:
                self.skillCount = 0

            if self.vel > 0:
                win.blit(self.skillR[self.skillCount // 5], (self.x - camx, self.y - 40))
                self.skillCount += 1
            else:
                win.blit(self.skillL[self.skillCount // 5], (self.x - camx, self.y - 40))
                self.skillCount += 1

    def hit(self):
        kslimehit.play()
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
                key5.visible = True
                slimedie.play()
                if slime10.visible == False and slime9.visible == False:
                    sucesso.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.visible = False
                key5.visible = True
                slimedie.play()
                if slime10.visible == False and slime9.visible == False:
                    sucesso.play()
            else:
                self.washit = 0

class spike11(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

# Objetos Plataformas ?
class platform74(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform75(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform76(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform77(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform78(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform79(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform80(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform81(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform82(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform83(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform84(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 17
            #player.isJump = True
            if player.jumpCount >= -17:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= round((player.jumpCount ** 2) / 4 * neg)
                player.jumpCount -= 1
        else:
            player.onPlatform = False

class platform85(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform86(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False


class platform87(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform88(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform89(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform90(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform91(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform92(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform93(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform94(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform95(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform96(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform97(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform98(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform99(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform100(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform101(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform102(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform103(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform104(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform105(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform106(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform107(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform108(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

# Laser Nave ?
class laser(object):
    walkR = [pygame.image.load('imagens/Mob/Laser/1.png'), pygame.image.load('imagens/Mob/Laser/2.png'),
             pygame.image.load('imagens/Mob/Laser/3.png'), pygame.image.load('imagens/Mob/Laser/4.png'),
             pygame.image.load('imagens/Mob/Laser/5.png'), pygame.image.load('imagens/Mob/Laser/6.png'),
             pygame.image.load('imagens/Mob/Laser/7.png'), pygame.image.load('imagens/Mob/Laser/8.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 64:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 8], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 8)

# Trap ?
class alien(object):
    walkR = [pygame.image.load('imagens/Mob/Alien/AR1.png'), pygame.image.load('imagens/Mob/Alien/AR2.png')]

    walkL = [pygame.image.load('imagens/Mob/Alien/AL1.png'), pygame.image.load('imagens/Mob/Alien/AL2.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 10
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 8:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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

# Parede ?
class wall5(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall6(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

# Plataformas Jail
class platform109(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform110(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform111(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform112(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform113(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform114(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform115(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform116(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

class platform117(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if player.jumpCount <= -1:
            player.onPlatform = True
            player.jumpCount = 10
            player.isJump = False
        else:
            player.onPlatform = False

# Parede Jail
class wall7(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall8(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall9(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall10(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall11(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class wall12(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class lever1(object):
    walkR = [pygame.image.load('imagens/Mob/Lever/LD.png'), pygame.image.load('imagens/Mob/Lever/LD.png')]

    walkL = [pygame.image.load('imagens/Mob/Lever/LU.png'), pygame.image.load('imagens/Mob/Lever/LU.png')]

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
        self.cont = 0
        self.visible = True

    def draw(self, win):
        if self.walkCount + 1 >= 4:
            self.walkCount = 0

        if (self.cont % 2) == 0:
            win.blit(self.walkR[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkL[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        if self.washit == 1:
            self.washit = 0
        elif self.washit == 2:
            self.washit = 0
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.cont += 1
        leverturn.play()

class lever2(object):
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
        self.cont = 0
        self.visible = True

    def draw(self, win):
        if self.walkCount + 1 >= 4:
            self.walkCount = 0

        if (self.cont % 2) == 0:
            win.blit(lever1.walkR[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        else:
            win.blit(lever1.walkL[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        if self.washit == 1:
            self.washit = 0
        elif self.washit == 2:
            self.washit = 0
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.cont += 1
        leverturn.play()

class lever3(object):
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
        self.cont = 0
        self.visible = True

    def draw(self, win):
        if self.walkCount + 1 >= 4:
            self.walkCount = 0

        if (self.cont % 2) == 0:
            win.blit(lever1.walkR[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        else:
            win.blit(lever1.walkL[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        if self.washit == 1:
            self.washit = 0
        elif self.washit == 2:
            self.washit = 0
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.cont += 1
        leverturn.play()

class lever4(object):
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
        self.cont = 0
        self.visible = True

    def draw(self, win):
        if self.walkCount + 1 >= 4:
            self.walkCount = 0

        if (self.cont % 2) == 0:
            win.blit(lever1.walkR[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        else:
            win.blit(lever1.walkL[self.walkCount // 2], (self.x - camx, self.y))
            self.walkCount += 1
        if self.washit == 1:
            self.washit = 0
        elif self.washit == 2:
            self.washit = 0
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.cont += 1
        leverturn.play()

class activator(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.enigma = False
        self.kenigma = False

    def draw(self, win):
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class portal1(object): 

    walkL = [pygame.image.load('imagens/Mob/Portal/1.0.png'), pygame.image.load('imagens/Mob/Portal/1.1.png'),
             pygame.image.load('imagens/Mob/Portal/1.2.png'),
             pygame.image.load('imagens/Mob/Portal/1.3.png'), pygame.image.load('imagens/Mob/Portal/1.4.png'),
             pygame.image.load('imagens/Mob/Portal/1.5.png'), pygame.image.load('imagens/Mob/Portal/1.6.png'),
             pygame.image.load('imagens/Mob/Portal/1.7.png'), pygame.image.load('imagens/Mob/Portal/1.8.png'),
             pygame.image.load('imagens/Mob/Portal/1.9.png'), pygame.image.load('imagens/Mob/Portal/1.10.png'),
             pygame.image.load('imagens/Mob/Portal/1.11.png')]

    skillL = [pygame.image.load('imagens/Mob/Portal/0.hit.0.png'), pygame.image.load('imagens/Mob/Portal/0.hit.1.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.2.png'), pygame.image.load('imagens/Mob/Portal/0.hit.3.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.4.png'), pygame.image.load('imagens/Mob/Portal/0.hit.5.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.6.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.7.png'), pygame.image.load('imagens/Mob/Portal/0.hit.8.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.9.png'), pygame.image.load('imagens/Mob/Portal/0.hit.10.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.11.png'), pygame.image.load('imagens/Mob/Portal/0.hit.12.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.13.png'), pygame.image.load('imagens/Mob/Portal/0.hit.14.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.15.png'), pygame.image.load('imagens/Mob/Portal/0.hit.16.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.17.png'), pygame.image.load('imagens/Mob/Portal/0.hit.18.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.19.png'), pygame.image.load('imagens/Mob/Portal/0.hit.20.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.21.png'), pygame.image.load('imagens/Mob/Portal/0.hit.22.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.23.png'), pygame.image.load('imagens/Mob/Portal/0.hit.24.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.25.png'), pygame.image.load('imagens/Mob/Portal/0.hit.26.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.27.png'), pygame.image.load('imagens/Mob/Portal/0.hit.28.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.29.png'), pygame.image.load('imagens/Mob/Portal/0.hit.30.png'),
              pygame.image.load('imagens/Mob/Portal/0.hit.31.png'), pygame.image.load('imagens/Mob/Portal/0.hit.32.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.skillCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.visible = False
        self.skill = False

    def draw(self, win):
        self.Skill()
        if self.visible and self.skill == False:
            if self.walkCount + 1 >= 48:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def Skill(self):
        if self.skill == True:
            if self.skillCount + 1 >= 132:
                self.skillCount = 0

            if self.vel > 0:
                win.blit(self.skillL[self.skillCount // 4], (self.x - camx, self.y))
                self.skillCount += 1

class portal2(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.skillCount = 0
        self.vel = 5
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.visible = False
        self.skill = False

    def draw(self, win):
        self.Skill()
        if self.visible and self.skill == False:
            if self.walkCount + 1 >= 48:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(portal1.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def Skill(self):
        if self.skill == True:
            if self.skillCount + 1 >= 132:
                self.skillCount = 0

            if self.vel > 0:
                win.blit(portal1.skillL[self.skillCount // 4], (self.x - camx, self.y))
                self.skillCount += 1

class digao(object):  # Boss Final
    walkR = [pygame.image.load('imagens/Mob/Digao/DR1.png'), pygame.image.load('imagens/Mob/Digao/DR2.png'),
             pygame.image.load('imagens/Mob/Digao/DR3.png'), pygame.image.load('imagens/Mob/Digao/DR4.png'),
             pygame.image.load('imagens/Mob/Digao/DR5.png'), pygame.image.load('imagens/Mob/Digao/DR6.png')]

    walkL = [pygame.image.load('imagens/Mob/Digao/DL1.png'), pygame.image.load('imagens/Mob/Digao/DL2.png'),
             pygame.image.load('imagens/Mob/Digao/DL3.png'), pygame.image.load('imagens/Mob/Digao/DL4.png'),
             pygame.image.load('imagens/Mob/Digao/DL5.png'), pygame.image.load('imagens/Mob/Digao/DL6.png')]

    dieL = [pygame.image.load('imagens/Mob/Digao/die/1.png'), pygame.image.load('imagens/Mob/Digao/die/2.png'),
              pygame.image.load('imagens/Mob/Digao/die/3.png'), pygame.image.load('imagens/Mob/Digao/die/4.png'),
              pygame.image.load('imagens/Mob/Digao/die/5.png'), pygame.image.load('imagens/Mob/Digao/die/6.png'),
              pygame.image.load('imagens/Mob/Digao/die/7.png'), pygame.image.load('imagens/Mob/Digao/die/8.png'),
              pygame.image.load('imagens/Mob/Digao/die/9.png'), pygame.image.load('imagens/Mob/Digao/die/10.png'),
              pygame.image.load('imagens/Mob/Digao/die/11.png'), pygame.image.load('imagens/Mob/Digao/die/12.png'),
              pygame.image.load('imagens/Mob/Digao/die/13.png'), pygame.image.load('imagens/Mob/Digao/die/14.png'),
              pygame.image.load('imagens/Mob/Digao/die/15.png'), pygame.image.load('imagens/Mob/Digao/die/16.png'),
              pygame.image.load('imagens/Mob/Digao/die/17.png'), pygame.image.load('imagens/Mob/Digao/die/18.png'),
              pygame.image.load('imagens/Mob/Digao/die/19.png'), pygame.image.load('imagens/Mob/Digao/die/20.png'),
              pygame.image.load('imagens/Mob/Digao/die/21.png'), pygame.image.load('imagens/Mob/Digao/die/22.png'),
              pygame.image.load('imagens/Mob/Digao/die/23.png'), pygame.image.load('imagens/Mob/Digao/die/24.png'),
              pygame.image.load('imagens/Mob/Digao/die/25.png'), pygame.image.load('imagens/Mob/Digao/die/26.png'),
              pygame.image.load('imagens/Mob/Digao/die/27.png'), pygame.image.load('imagens/Mob/Digao/die/28.png'),
              pygame.image.load('imagens/Mob/Digao/die/29.png'), pygame.image.load('imagens/Mob/Digao/die/30.png'),
              pygame.image.load('imagens/Mob/Digao/die/31.png'), pygame.image.load('imagens/Mob/Digao/die/32.png'),
              pygame.image.load('imagens/Mob/Digao/die/33.png'), pygame.image.load('imagens/Mob/Digao/die/34.png'),
              pygame.image.load('imagens/Mob/Digao/die/35.png'), pygame.image.load('imagens/Mob/Digao/die/36.png'),
              pygame.image.load('imagens/Mob/Digao/die/37.png'), pygame.image.load('imagens/Mob/Digao/die/38.png'),
              pygame.image.load('imagens/Mob/Digao/die/39.png')]

    dieR = [pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/1.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/2.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/3.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/4.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/5.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/6.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/7.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/8.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/9.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/10.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/11.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/12.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/13.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/14.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/15.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/16.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/17.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/18.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/19.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/20.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/21.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/22.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/23.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/24.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/25.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/26.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/27.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/28.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/29.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/30.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/31.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/32.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/33.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/34.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/35.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/36.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/37.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/38.png'), True, False),
            pygame.transform.flip(pygame.image.load('imagens/Mob/Digao/die/39.png'), True, False)]

    imgskill1 = [pygame.image.load('imagens/Mob/Digao/skill1/1.png'), pygame.image.load('imagens/Mob/Digao/skill1/2.png'),
              pygame.image.load('imagens/Mob/Digao/skill1/3.png'), pygame.image.load('imagens/Mob/Digao/skill1/4.png'),
              pygame.image.load('imagens/Mob/Digao/skill1/5.png'), pygame.image.load('imagens/Mob/Digao/skill1/6.png'),
              pygame.image.load('imagens/Mob/Digao/skill1/7.png'), pygame.image.load('imagens/Mob/Digao/skill1/8.png'),
              pygame.image.load('imagens/Mob/Digao/skill1/9.png'), pygame.image.load('imagens/Mob/Digao/skill1/10.png'),
              pygame.image.load('imagens/Mob/Digao/skill1/11.png'), pygame.image.load('imagens/Mob/Digao/skill1/12.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/13.png'), pygame.image.load('imagens/Mob/Digao/skill1/14.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/15.png'), pygame.image.load('imagens/Mob/Digao/skill1/16.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/17.png'), pygame.image.load('imagens/Mob/Digao/skill1/18.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/19.png'), pygame.image.load('imagens/Mob/Digao/skill1/20.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/21.png'), pygame.image.load('imagens/Mob/Digao/skill1/22.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/23.png'), pygame.image.load('imagens/Mob/Digao/skill1/24.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/25.png'), pygame.image.load('imagens/Mob/Digao/skill1/26.png'), 
              pygame.image.load('imagens/Mob/Digao/skill1/27.png')]

    explosionskill1 = pygame.image.load('imagens/Mob/Digao/skill1/explosion.png')
    
    imgskill2 = [pygame.image.load('imagens/Mob/Digao/skill2/1.png'), pygame.image.load('imagens/Mob/Digao/skill2/2.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/3.png'), pygame.image.load('imagens/Mob/Digao/skill2/4.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/5.png'), pygame.image.load('imagens/Mob/Digao/skill2/6.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/7.png'), pygame.image.load('imagens/Mob/Digao/skill2/8.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/9.png'), pygame.image.load('imagens/Mob/Digao/skill2/10.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/11.png'), pygame.image.load('imagens/Mob/Digao/skill2/12.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/13.png'), pygame.image.load('imagens/Mob/Digao/skill2/14.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/15.png'), pygame.image.load('imagens/Mob/Digao/skill2/16.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/17.png'), pygame.image.load('imagens/Mob/Digao/skill2/18.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/19.png'), pygame.image.load('imagens/Mob/Digao/skill2/20.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/21.png'), pygame.image.load('imagens/Mob/Digao/skill2/22.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/23.png'), pygame.image.load('imagens/Mob/Digao/skill2/24.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/25.png'), pygame.image.load('imagens/Mob/Digao/skill2/26.png'), 
              pygame.image.load('imagens/Mob/Digao/skill2/27.png'), pygame.image.load('imagens/Mob/Digao/skill2/28.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/29.png'), pygame.image.load('imagens/Mob/Digao/skill2/30.png'),
              pygame.image.load('imagens/Mob/Digao/skill2/31.png')]

    imgskill3 = [pygame.image.load('imagens/Mob/Digao/skill3/1.png'), pygame.image.load('imagens/Mob/Digao/skill3/2.png'),
              pygame.image.load('imagens/Mob/Digao/skill3/3.png'), pygame.image.load('imagens/Mob/Digao/skill3/4.png'),
              pygame.image.load('imagens/Mob/Digao/skill3/5.png'), pygame.image.load('imagens/Mob/Digao/skill3/6.png'),
              pygame.image.load('imagens/Mob/Digao/skill3/7.png'), pygame.image.load('imagens/Mob/Digao/skill3/8.png'),
              pygame.image.load('imagens/Mob/Digao/skill3/9.png'), pygame.image.load('imagens/Mob/Digao/skill3/10.png'),
              pygame.image.load('imagens/Mob/Digao/skill3/11.png'), pygame.image.load('imagens/Mob/Digao/skill3/12.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/13.png'), pygame.image.load('imagens/Mob/Digao/skill3/14.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/15.png'), pygame.image.load('imagens/Mob/Digao/skill3/16.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/17.png'), pygame.image.load('imagens/Mob/Digao/skill3/18.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/19.png'), pygame.image.load('imagens/Mob/Digao/skill3/20.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/21.png'), pygame.image.load('imagens/Mob/Digao/skill3/22.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/23.png'), pygame.image.load('imagens/Mob/Digao/skill3/24.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/25.png'), pygame.image.load('imagens/Mob/Digao/skill3/26.png'), 
              pygame.image.load('imagens/Mob/Digao/skill3/27.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.dieCount = 0
        self.skill1Count = 0
        self.skill2Count = 0
        self.skill3Count = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.health = 181
        self.visible = True
        self.ondie = False
        self.onskill1 = False
        self.onskill2 = False
        self.onskill3 = False

    def draw(self, win):
        self.move()
        self.skill1()
        self.skill2()
        self.skill3()
        self.die()
        if self.visible and self.ondie == False and self.onskill1 == False and self.onskill2 == False and self.onskill3 == False:
            if self.walkCount + 1 >= 24:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkR[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
                self.hitbox = (self.x - camx + 65, self.y + 30, self.width, self.height)
            else:
                win.blit(self.walkL[self.walkCount // 4], (self.x - camx, self.y))
                self.walkCount += 1
                self.hitbox = (self.x - camx + 23, self.y + 30, self.width, self.height)
            if self.washit == 1:
                self.washit = 0
            elif self.washit == 2:
                self.washit = 0
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0], self.hitbox[1] - 12, 187, 8))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 2, self.hitbox[1] - 10 , 183 - (1 * (181 - self.health)), 4))
            #self.hitbox = (self.x - camx, self.y + 20, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.ondie == False and self.onskill1 == False and self.onskill2 == False and self.onskill3 == False:
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

    def skill1(self):
        if self.skill1Count >= 88:
            win.blit(self.explosionskill1, (self.x - camx - 525, 420))

        if self.visible and self.onskill1 == True and self.ondie == False:
            if self.skill1Count + 1 >= 108:
                self.skill1Count = 0

            if self.vel < 0:
                win.blit(self.imgskill1[self.skill1Count // 4], (self.x - camx - 100, self.y - 80))
                self.skill1Count += 1

    def skill2(self):
        if self.visible and self.onskill2 == True and self.ondie == False:
            if self.skill2Count + 1 >= 124:
                self.skill2Count = 0

            if self.vel < 0:
                win.blit(self.imgskill2[self.skill2Count // 4], (self.x - camx - 100, self.y - 215))
                self.skill2Count += 1

    def skill3(self):
        if self.visible and self.onskill3 == True and self.ondie == False:
            if self.skill3Count + 1 >= 108:
                self.skill3Count = 0

            if self.vel < 0:
                win.blit(self.imgskill3[self.skill3Count // 4], (self.x - camx - 130, self.y - 120))
                self.skill3Count += 1
    
    def die(self):
        if self.visible and self.ondie == True:
            if self.dieCount + 1 >= 156:
                self.dieCount = 0

            if self.vel > 0:
                win.blit(self.dieR[self.dieCount // 4], (self.x - camx - 200, self.y - 120))
                self.dieCount += 1
            else:
                win.blit(self.dieL[self.dieCount // 4], (self.x - camx, self.y - 120))
                self.dieCount += 1
                    
    def hit(self):
        #digaohit.play()
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
                self.ondie = True
                key7.visible = True
                #self.visible = False
                digaodie.play()
            elif self.vel < 0:
                self.hitbox = (0, 0, 0, 0)
                self.washit = 2
                self.ondie = True
                key7.visible = True
                #self.visible = False
                digaodie.play()
            else:
                self.washit = 0

class arrow1(object):
    walkL = [pygame.image.load('imagens/Mob/Digao/skill2/arrow/1.png'), pygame.image.load('imagens/Mob/Digao/skill2/arrow/2.png'),
          pygame.image.load('imagens/Mob/Digao/skill2/arrow/3.png'), pygame.image.load('imagens/Mob/Digao/skill2/arrow/4.png'),
          pygame.image.load('imagens/Mob/Digao/skill2/arrow/5.png')]
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible and digao.ondie == False:
            if self.walkCount + 1 >= 25:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 5], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class arrow2(object):
    walkL = [pygame.image.load('imagens/Mob/Digao/skill2/arrow/1.png'),
             pygame.image.load('imagens/Mob/Digao/skill2/arrow/2.png'),
             pygame.image.load('imagens/Mob/Digao/skill2/arrow/3.png'),
             pygame.image.load('imagens/Mob/Digao/skill2/arrow/4.png'),
             pygame.image.load('imagens/Mob/Digao/skill2/arrow/5.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible and digao.ondie == False:
            if self.walkCount + 1 >= 25:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 5], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class jar1(object):
    walkL = [pygame.image.load('imagens/Mob/Digao/skill3/explosion/1.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/2.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/3.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/4.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/5.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/6.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/7.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/8.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/9.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/10.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/11.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/12.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/13.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/14.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/15.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/16.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/17.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/18.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/19.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/20.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/21.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/22.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/23.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/24.png'),
             pygame.image.load('imagens/Mob/Digao/skill3/explosion/25.png'), pygame.image.load('imagens/Mob/Digao/skill3/explosion/26.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible and digao.ondie == False:
            if self.walkCount + 1 >= 78:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx + 39, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class jar2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible and digao.ondie == False:
            if self.walkCount + 1 >= 78:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(jar1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx + 39, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class jar3(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible and digao.ondie == False:
            if self.walkCount + 1 >= 78:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(jar1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx + 39, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class jar4(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible and digao.ondie == False:
            if self.walkCount + 1 >= 78:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(jar1.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx + 39, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class jail(object):
    walkL = [pygame.image.load('imagens/Mapa/jail.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = True
        self.open = False

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key1(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key2(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key3(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key4(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key5(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key6(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class key7(object):
    walkL = [pygame.image.load('imagens/Mob/Keys/key.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = False

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 1:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 1], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx, self.y, self.width, self.height)
            ##pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class fim(object):
    walkL = [pygame.image.load('imagens/Mapa/Fim/1.png'), pygame.image.load('imagens/Mapa/Fim/2.png'),
             pygame.image.load('imagens/Mapa/Fim/3.png'), pygame.image.load('imagens/Mapa/Fim/4.png'),
             pygame.image.load('imagens/Mapa/Fim/5.png'), pygame.image.load('imagens/Mapa/Fim/6.png'),
             pygame.image.load('imagens/Mapa/Fim/7.png'), pygame.image.load('imagens/Mapa/Fim/8.png'),
             pygame.image.load('imagens/Mapa/Fim/9.png'), pygame.image.load('imagens/Mapa/Fim/10.png'),
             pygame.image.load('imagens/Mapa/Fim/11.png'), pygame.image.load('imagens/Mapa/Fim/12.png'),
             pygame.image.load('imagens/Mapa/Fim/13.png'), pygame.image.load('imagens/Mapa/Fim/14.png'),
             pygame.image.load('imagens/Mapa/Fim/15.png'), pygame.image.load('imagens/Mapa/Fim/16.png'),
             pygame.image.load('imagens/Mapa/Fim/17.png'), pygame.image.load('imagens/Mapa/Fim/18.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x - camx, self.y, self.width, self.height)
        self.washit = 0
        self.visible = True

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 54:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkL[self.walkCount // 3], (self.x - camx, self.y))
                self.walkCount += 1

            self.hitbox = (self.x - camx + 39, self.y, self.width, self.height)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            
def GameWindow():
    # Background (Mapa)
    win.blit(bg4, (27358 - camx, 0))
    win.blit(skybg, (29358 - camx, 0))
    win.blit(skybg, (31468 - camx, 0))
    jail.draw(win)
    win.blit(parede, (29347 - camx, 0))
    win.blit(bg3, (18675 - camx, 0))
    win.blit(bg2, (10920 - camx, 0))
    win.blit(bg, (0 - camx, 0))

    # HUD
    win.blit(teclas, (550, 5))
    if life == 3:
        win.blit(vidas3, (336, 5))
    elif life == 2:
        win.blit(vidas2, (336, 5))
    elif life == 1:
        win.blit(vidas1, (336, 5))
    elif life == 0:
        win.blit(vidas0, (336, 5))

    if player.keys == 0:
        win.blit(keys0, (5, 5))
    elif player.keys == 1:
        win.blit(keys1, (5, 5))
    elif player.keys == 2:
        win.blit(keys2, (5, 5))
    elif player.keys == 3:
        win.blit(keys3, (5, 5))
    elif player.keys == 4:
        win.blit(keys4, (5, 5))
    elif player.keys == 5:
        win.blit(keys5, (5, 5))
    elif player.keys == 6:
        win.blit(keys6, (5, 5))
    elif player.keys == 7:
        win.blit(keys7, (5, 5))

    if camx >= 24871 and camx <= 26051 and activator.enigma == False and activator.kenigma == False:
        win.blit(quest, (0, 50))
        
    # Draw Gate Perion
    gate1.draw(win)
    # Draw Gate Ellinia
    gate2.draw(win)
    # Draw Objetos Mapa Perion
    altar1.draw(win)
    #Laser ?
    laser.draw(win)
    # Draw Lever
    lever1.draw(win)
    lever2.draw(win)
    lever3.draw(win)
    lever4.draw(win)

    portal1.draw(win)
    portal2.draw(win)

    #Mapa Final
    fim.draw(win)
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

    # Draw Plataformas Henesys
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

    # Draw Parede Ellinia
    wall3.draw(win)
    wall4.draw(win)

    # Draw Plataformas Ellinia
    platform67.draw(win)
    platform68.draw(win)
    platform69.draw(win)
    platform70.draw(win)
    platform71.draw(win)
    platform72.draw(win)
    platform73.draw(win)

    # Draw Monstros Ellinia
    slime1.draw(win)
    slime2.draw(win)
    slime3.draw(win)
    slime4.draw(win)
    slime5.draw(win)
    slime6.draw(win)
    slime7.draw(win)
    slime8.draw(win)
    slime9.draw(win)
    slime10.draw(win)
    KSlime.draw(win)

    # Draw Spike ?
    spike11.draw(win)

    #Draw Plataforma ?
    platform74.draw(win)
    platform75.draw(win)
    platform76.draw(win)
    platform77.draw(win)
    platform78.draw(win)
    platform79.draw(win)
    platform80.draw(win)
    platform81.draw(win)
    platform82.draw(win)
    platform83.draw(win)
    platform84.draw(win)
    platform85.draw(win)
    platform86.draw(win)
    platform87.draw(win)
    platform88.draw(win)
    platform89.draw(win)
    platform90.draw(win)
    platform91.draw(win)
    platform92.draw(win)
    platform93.draw(win)
    platform94.draw(win)
    platform95.draw(win)
    platform96.draw(win)
    platform97.draw(win)
    platform98.draw(win)
    platform99.draw(win)
    platform100.draw(win)
    platform101.draw(win)
    platform102.draw(win)
    platform103.draw(win)
    platform104.draw(win)
    platform105.draw(win)
    platform106.draw(win)
    platform107.draw(win)
    platform108.draw(win)

    # Draw Alien ?
    alien.draw(win)

    # Draw Parede ?
    wall5.draw(win)
    wall6.draw(win)

    # Draw Parede Jail
    wall7.draw(win)
    wall8.draw(win)
    wall9.draw(win)
    wall10.draw(win)

    # Boss Final Draw
    digao.draw(win)
    arrow1.draw(win)
    arrow2.draw(win)
    jar1.draw(win)
    jar2.draw(win)
    jar3.draw(win)
    jar4.draw(win)

    # Chaves
    key1.draw(win)
    key2.draw(win)
    key3.draw(win)
    key4.draw(win)
    key5.draw(win)
    key6.draw(win)
    key7.draw(win)

    # Plataformas Jail
    platform109.draw(win)
    platform110.draw(win)
    platform111.draw(win)
    platform112.draw(win)
    platform113.draw(win)
    platform114.draw(win)
    platform115.draw(win)
    platform116.draw(win)
    platform117.draw(win)

    activator.draw(win)

    wall11.draw(win)
    wall12.draw(win)

    pygame.display.update()


# Main loop
camx = 0  # Camera

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

# Variável Gate Ellinia
gate2 = gate2(18566, 395, 64, 64, 14708)

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
spike10 = spike10(15485, 549, 2050, 35)

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

# Variável Monstros Ellinia
slime1 = slime1(15240, 456, 60, 54, 15410)
slime2 = slime2(15708, 456, 60, 54, 15759)
slime3 = slime3(16018, 456, 60, 54, 16069)
slime4 = slime4(16220, 456, 60, 54, 16430)
slime5 = slime5(16500, 456, 60, 54, 16710)
slime6 = slime6(17007, 456, 60, 54, 17058)
slime7 = slime7(17317, 456, 60, 54, 17368)
slime8 = slime8(17520, 456, 60, 54, 17790)

slime9 = slime9(17890, 456, 60, 54, 18130)
slime10 = slime10(18200, 456, 60, 54, 18360)
KSlime = KSlime(17890, 300, 159, 165, 18360)

# Variável Spike ?
spike11 = spike11(18675, 550, 6565, 35)

# Variável PLataformas ?
platform74 = platform74(19480, 483, 50, 15)
platform75 = platform75(19601, 483, 50, 15)
platform76 = platform76(19939, 483, 50, 15)
platform77 = platform77(20022, 435, 50, 15)
platform78 = platform78(20848, 466, 50, 15)
platform79 = platform79(20848, 393, 50, 15)
platform80 = platform80(20966, 393, 50, 15)
platform81 = platform81(21084, 393, 50, 15)
platform82 = platform82(21202, 393, 50, 15)
platform83 = platform83(21202, 466, 50, 15)
platform84 = platform84(21463, 475, 50, 15)
platform85 = platform85(21463, 475, 50, 15)
platform86 = platform86(22200, 487, 50, 15)

#fila tp 1
platform87 = platform87(22304, 433, 50, 15)
platform88 = platform88(22304, 339, 50, 15)
platform89 = platform89(22304, 249, 50, 15)

#fila tp 2
platform90 = platform90(22563, 433, 50, 15)
platform91 = platform91(22563, 339, 50, 15)
platform92 = platform92(22563, 249, 50, 15)

#fila tp 3
platform93 = platform93(22804, 433, 50, 15)
platform94 = platform94(22804, 339, 50, 15)
platform95 = platform95(22804, 249, 50, 15)

#fila tp 4
platform96 = platform96(23032, 433, 50, 15)
platform97 = platform97(23032, 339, 50, 15)
platform98 = platform98(23032, 249, 50, 15)

#fila tp 5
platform99 = platform99(23263, 433, 50, 15)
platform100 = platform100(23263, 339, 50, 15)
platform101 = platform101(23263, 249, 50, 15)

#fila tp 6
platform102 = platform102(23477, 433, 50, 15)
platform103 = platform103(23477, 339, 50, 15)
platform104 = platform104(23477, 249, 50, 15)

# Fila trap ? 1
platform105 = platform105(24317, 487, 50, 15)
platform106 = platform106(24317, 415, 50, 15)

# Fila trap ? 2
platform107 = platform107(24435, 341, 50, 15)

# Fila trap ? 3
platform108 = platform108(24560, 487, 50, 15)

lever1 = lever1(25636, 463, 62, 62, 18360)
lever2 = lever2(25786, 463, 62, 62, 18360)
lever3 = lever3(25936, 463, 62, 62, 18360)
lever4 = lever4(26086, 463, 62, 62, 18360)

# Activator
activator = activator(26200, 478, 56, 76)

# Laser
laser = laser(20370, 160, 103, 440, 14417)

#Trap Alien ?
alien = alien(20848,366, 89, 103, 21173)

# Parede ?
wall5 = wall5(21705, 395, 55, 160)
wall6 = wall6(26500, 0, 55, 600)

# Parede Jail
wall7 = wall7(27288, 0, 70, 600)
wall8 = wall8(27648, 0, 20, 600)
wall9 = wall9(28608, 0, 20, 600)
wall10 = wall10(29358, 0, 70, 600)

# Variavel Boss Final
digao = digao(27645, 269, 110, 256, 28404)
arrow1 = arrow1(28611, 480, 57, 33)
arrow2 = arrow2(28611, 244, 57, 33)
jar1 = jar1(27318, 112, 138, 433)
jar2 = jar2(27708, 112, 138, 433)
jar3 = jar3(28088, 112, 138, 433)
jar4 = jar4(28438, 112, 138, 433)

# Plataformas Jail fila 1
platform109 = platform109(27753, 480, 60, 15)
platform110 = platform110(27753, 399, 60, 15)
platform111 = platform111(27753, 315, 60, 15)

# Plataformas Jail fila 2
platform112 = platform112(28129, 480, 60, 15)
platform113 = platform113(28129, 399, 60, 15)
platform114 = platform114(28129, 315, 60, 15)

# Plataformas Jail fila 3
platform115 = platform115(28490, 480, 60, 15)
platform116 = platform116(28490, 399, 60, 15)
platform117 = platform117(28490, 315, 60, 15)

portal1 = portal1(26305, 328, 196, 225)
portal2 = portal2(28773, 328, 196, 225)

jail = jail(29015, 139, 343, 406)

#Variaveis Keys
key1 = key1(4390, 145, 32, 31)
key2 = key2(10191, 79, 32, 31)
key3 = key3(14720, 89, 32, 31)
key4 = key4(stumpy.x, 513, 32, 31)
key5 = key5(KSlime.x, 509, 32, 31)
key6 = key6(26155, 516, 32, 31)
key7 = key7(digao.x, 515, 32, 31)

fim = fim(30068, 0, 0, 0)

wall11 = wall11(30490, 0, 10, 600)
wall12 = wall12(31070, 0, 10, 600)

run = True
while run:
    keys = pygame.key.get_pressed()
    clock.tick(27)

    # TESTES
    #print(camx)
    #print(digao.x)
    #print(digao.skill2Count)
    #print(arrow1.x)
    #print(digao.walkCount)
    # print(player.y)
    #print(player.onPlatform)
    # print(player.isJump)
    # print(stumpy.walkCount)
    #print(KSlime.skillCount)
    #print(laser.walkCount)
    #print(portal1.skillCount)

    # Checkpoints
    if camx == 6545:
        checkpoint = 6545

    if camx == 10610:
        checkpoint = 10610

    if camx == 14740:
        checkpoint = 14740

    if camx >= 18385 and camx <= 18441:
        checkpoint = 18429

    if camx == 27081:
        checkpoint = 27081

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

    if camx == 18275:
        music = pygame.mixer.music.load("BGM/BGM05.mp3")
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
        # else:
        # player.onPlatform = False

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

    # Colisão Monstros Henesys
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
        # else:
        # player.onPlatform = False

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
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform25.hitbox[1] + platform25.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform25.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform25.hitbox[0] and player.plathitbox[0] < \
                platform25.hitbox[0] + platform25.hitbox[2]:
            platform25.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform26.hitbox[1] + platform26.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform26.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform26.hitbox[0] and player.plathitbox[0] < \
                platform26.hitbox[0] + platform26.hitbox[2]:
            platform26.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform27.hitbox[1] + platform27.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform27.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform27.hitbox[0] and player.plathitbox[0] < \
                platform27.hitbox[0] + platform27.hitbox[2]:
            platform27.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform28.hitbox[1] + platform28.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform28.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform28.hitbox[0] and player.plathitbox[0] < \
                platform28.hitbox[0] + platform28.hitbox[2]:
            platform28.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform29.hitbox[1] + platform29.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform29.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform29.hitbox[0] and player.plathitbox[0] < \
                platform29.hitbox[0] + platform29.hitbox[2]:
            platform29.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform30.hitbox[1] + platform30.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform30.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform30.hitbox[0] and player.plathitbox[0] < \
                platform30.hitbox[0] + platform30.hitbox[2]:
            platform30.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

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
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform36.hitbox[1] + platform36.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform36.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform36.hitbox[0] and player.plathitbox[0] < \
                platform36.hitbox[0] + platform36.hitbox[2]:
            platform36.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

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
        # else:
        # player.onPlatform = False

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
        # else:
        # player.onPlatform = False

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
        # else:
        # player.onPlatform = False

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
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform66.hitbox[1] + platform66.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform66.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform66.hitbox[0] and player.plathitbox[0] < \
                platform66.hitbox[0] + platform66.hitbox[2]:
            platform66.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    # Colisão Plataformas Ellinia
    if player.plathitbox[1] < platform67.hitbox[1] + platform67.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform67.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform67.hitbox[0] and player.plathitbox[0] < \
                platform67.hitbox[0] + platform67.hitbox[2]:
            platform67.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform68.hitbox[1] + platform68.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform68.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform68.hitbox[0] and player.plathitbox[0] < \
                platform68.hitbox[0] + platform68.hitbox[2]:
            platform68.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform69.hitbox[1] + platform69.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform69.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform69.hitbox[0] and player.plathitbox[0] < \
                platform69.hitbox[0] + platform69.hitbox[2]:
            platform69.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform70.hitbox[1] + platform70.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform70.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform70.hitbox[0] and player.plathitbox[0] < \
                platform70.hitbox[0] + platform70.hitbox[2]:
            platform70.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform71.hitbox[1] + platform71.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform71.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform71.hitbox[0] and player.plathitbox[0] < \
                platform71.hitbox[0] + platform71.hitbox[2]:
            platform71.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform72.hitbox[1] + platform72.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform72.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform72.hitbox[0] and player.plathitbox[0] < \
                platform72.hitbox[0] + platform72.hitbox[2]:
            platform72.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform73.hitbox[1] + platform73.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform73.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform73.hitbox[0] and player.plathitbox[0] < \
                platform73.hitbox[0] + platform73.hitbox[2]:
            platform73.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

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

    # Colisão Hitbox Stumpy
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
    if stumpy.walkCount == 40 and player.y == 470 and camx > 13955 and stumpy.visible == True and camx < 14385:
        player.hit()
        life -= 1
        player.health -= 1
        camx = checkpoint
        player.x = 400
        player.y = 470

    if stumpy.walkCount == 80 and stumpy.visible == True and camx > 13910 and camx < 14385:
        stumpyskill.play()

    if stumpy.walkCount == 40 and camx >= 14225 and player.y > 300 and stumpy.visible == True and camx < 14385:
        player.hit()
        life -= 1
        player.health -= 1
        camx = checkpoint
        player.x = 400
        player.y = 470

    # Skill King Slime
    if slime9.visible == False:
        KSlime.skill = True
        if KSlime.skillCount == 1:
            kslimeskill.play()
        if KSlime.skillCount == 54:
            slime9.hitbox = (slime9.x - camx, slime9.y, slime9.width, slime9.height)
            slime9.washit = 0
            slime9.health = 10
            KSlime.skill = False
            slime9.visible = True
            KSlime.skillCount = 0

    if slime10.visible == False:
        KSlime.skill = True
        if KSlime.skillCount == 1:
            kslimeskill.play()
        if KSlime.skillCount == 54:
            slime10.hitbox = (slime10.x - camx, slime10.y, slime10.width, slime10.height)
            slime10.washit = 0
            slime10.health = 10
            KSlime.skill = False
            slime10.visible = True
            KSlime.skillCount = 0

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

    # Colisão Monstros Ellinia
    if player.hitbox[1] < slime1.hitbox[1] + slime1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime1.hitbox[0] and player.hitbox[0] < slime1.hitbox[0] + \
                slime1.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime2.hitbox[1] + slime2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime2.hitbox[0] and player.hitbox[0] < slime2.hitbox[0] + \
                slime2.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime3.hitbox[1] + slime3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime3.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime3.hitbox[0] and player.hitbox[0] < slime3.hitbox[0] + \
                slime3.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime4.hitbox[1] + slime4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime4.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime4.hitbox[0] and player.hitbox[0] < slime4.hitbox[0] + \
                slime4.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime5.hitbox[1] + slime5.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime5.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime5.hitbox[0] and player.hitbox[0] < slime5.hitbox[0] + \
                slime5.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime6.hitbox[1] + slime6.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime6.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime6.hitbox[0] and player.hitbox[0] < slime6.hitbox[0] + \
                slime6.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime7.hitbox[1] + slime7.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime7.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime7.hitbox[0] and player.hitbox[0] < slime7.hitbox[0] + \
                slime7.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime8.hitbox[1] + slime8.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime8.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime8.hitbox[0] and player.hitbox[0] < slime8.hitbox[0] + \
                slime8.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime9.hitbox[1] + slime9.hitbox[3] and player.hitbox[1] + player.hitbox[3] > slime9.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > slime9.hitbox[0] and player.hitbox[0] < slime9.hitbox[0] + \
                slime9.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < slime10.hitbox[1] + slime10.hitbox[3] and player.hitbox[1] + player.hitbox[3] > \
            slime10.hitbox[
                1]:
        if player.hitbox[0] + player.hitbox[2] > slime10.hitbox[0] and player.hitbox[0] < slime10.hitbox[0] + \
                slime10.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    if player.hitbox[1] < KSlime.hitbox[1] + KSlime.hitbox[3] and player.hitbox[1] + player.hitbox[3] > KSlime.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > KSlime.hitbox[0] and player.hitbox[0] < KSlime.hitbox[0] + \
                KSlime.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Parede Ellinia
    if player.plathitbox[1] < wall3.hitbox[1] + wall3.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall3.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall3.hitbox[0] and player.plathitbox[0] < \
                wall3.hitbox[0] + wall3.hitbox[2]:
            camx += 5
            player.walkCount = 0

    if slime9.visible or slime10.visible or KSlime.visible:
        if player.plathitbox[1] < wall4.hitbox[1] + wall4.hitbox[3] and player.plathitbox[1] + \
                player.plathitbox[
                    3] > wall4.hitbox[1]:
            if player.plathitbox[0] + player.plathitbox[2] > wall4.hitbox[0] and player.plathitbox[0] < \
                    wall4.hitbox[0] + wall4.hitbox[2]:
                camx -= 5
                player.walkCount = 0

    # Colisão Spike Ellinia
    if player.hitbox[1] < spike10.hitbox[1] + spike10.hitbox[3] and player.hitbox[1] + player.hitbox[3] > \
            spike10.hitbox[
                1]:
        if player.hitbox[0] + player.hitbox[2] > spike10.hitbox[0] and player.hitbox[0] < spike10.hitbox[0] + \
                spike10.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Spike ?
    if player.hitbox[1] < spike11.hitbox[1] + spike11.hitbox[3] and player.hitbox[1] + player.hitbox[3] > \
            spike11.hitbox[
                1]:
        if player.hitbox[0] + player.hitbox[2] > spike11.hitbox[0] and player.hitbox[0] < spike11.hitbox[0] + \
                spike11.hitbox[2]:
            tp.play()
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Alien ?
    if player.hitbox[1] < alien.hitbox[1] + alien.hitbox[3] and player.hitbox[1] + player.hitbox[3] > \
            alien.hitbox[
                1]:
        if player.hitbox[0] + player.hitbox[2] > alien.hitbox[0] and player.hitbox[0] < alien.hitbox[0] + \
                alien.hitbox[2]:
            tp.play()
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Colisão Plataformas ?
    if player.plathitbox[1] < platform74.hitbox[1] + platform74.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform74.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform74.hitbox[0] and player.plathitbox[0] < \
                platform74.hitbox[0] + platform74.hitbox[2]:
            platform74.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform75.hitbox[1] + platform75.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform75.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform75.hitbox[0] and player.plathitbox[0] < \
                platform75.hitbox[0] + platform75.hitbox[2]:
            platform75.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform76.hitbox[1] + platform76.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform76.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform76.hitbox[0] and player.plathitbox[0] < \
                platform76.hitbox[0] + platform76.hitbox[2]:
            platform76.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform77.hitbox[1] + platform77.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform77.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform77.hitbox[0] and player.plathitbox[0] < \
                platform77.hitbox[0] + platform77.hitbox[2]:
            tp.play()
            camx = checkpoint
            player.x = 400
            player.y = 470
            player.jumpCount = 10
            player.walkCount = 0
            player.isJump = False
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform78.hitbox[1] + platform78.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform78.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform78.hitbox[0] and player.plathitbox[0] < \
                platform78.hitbox[0] + platform78.hitbox[2]:
            platform78.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform79.hitbox[1] + platform79.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform79.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform79.hitbox[0] and player.plathitbox[0] < \
                platform79.hitbox[0] + platform79.hitbox[2]:
            platform79.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform80.hitbox[1] + platform80.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform80.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform80.hitbox[0] and player.plathitbox[0] < \
                platform80.hitbox[0] + platform80.hitbox[2]:
            platform80.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform81.hitbox[1] + platform81.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform81.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform81.hitbox[0] and player.plathitbox[0] < \
                platform81.hitbox[0] + platform81.hitbox[2]:
            platform81.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform82.hitbox[1] + platform82.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform82.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform82.hitbox[0] and player.plathitbox[0] < \
                platform82.hitbox[0] + platform82.hitbox[2]:
            platform82.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform83.hitbox[1] + platform83.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform83.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform83.hitbox[0] and player.plathitbox[0] < \
                platform83.hitbox[0] + platform83.hitbox[2]:
            platform83.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform84.hitbox[1] + platform84.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform84.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform84.hitbox[0] and player.plathitbox[0] < \
                platform84.hitbox[0] + platform84.hitbox[2]:
            platform84.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform85.hitbox[1] + platform85.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform85.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform85.hitbox[0] and player.plathitbox[0] < \
                platform85.hitbox[0] + platform85.hitbox[2]:
            platform85.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform86.hitbox[1] + platform86.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform86.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform86.hitbox[0] and player.plathitbox[0] < \
                platform86.hitbox[0] + platform86.hitbox[2]:
            platform86.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform87.hitbox[1] + platform87.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform87.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform87.hitbox[0] and player.plathitbox[0] < \
                platform87.hitbox[0] + platform87.hitbox[2]:
            platform87.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform88.hitbox[1] + platform88.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform88.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform88.hitbox[0] and player.plathitbox[0] < \
                platform88.hitbox[0] + platform88.hitbox[2]:
            platform88.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform89.hitbox[1] + platform89.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform89.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform89.hitbox[0] and player.plathitbox[0] < \
                platform89.hitbox[0] + platform89.hitbox[2]:
            platform89.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = platform90.x - 410
                player.y = platform90.y - 85
                pygame.time.delay(200)
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform90.hitbox[1] + platform90.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform90.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform90.hitbox[0] and player.plathitbox[0] < \
                platform90.hitbox[0] + platform90.hitbox[2]:
            platform90.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform91.hitbox[1] + platform91.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform91.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform91.hitbox[0] and player.plathitbox[0] < \
                platform91.hitbox[0] + platform91.hitbox[2]:
            platform91.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform92.hitbox[1] + platform92.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform92.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform92.hitbox[0] and player.plathitbox[0] < \
                platform92.hitbox[0] + platform92.hitbox[2]:
            platform92.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = platform93.x - 410
                player.y = platform93.y - 85
                pygame.time.delay(200)
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform93.hitbox[1] + platform93.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform93.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform93.hitbox[0] and player.plathitbox[0] < \
                platform93.hitbox[0] + platform93.hitbox[2]:
            platform93.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = platform96.x - 410
                player.y = platform96.y - 85
                pygame.time.delay(200)
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform94.hitbox[1] + platform94.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform94.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform94.hitbox[0] and player.plathitbox[0] < \
                platform94.hitbox[0] + platform94.hitbox[2]:
            platform94.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform95.hitbox[1] + platform95.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform95.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform95.hitbox[0] and player.plathitbox[0] < \
                platform95.hitbox[0] + platform95.hitbox[2]:
            platform95.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform96.hitbox[1] + platform96.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform96.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform96.hitbox[0] and player.plathitbox[0] < \
                platform96.hitbox[0] + platform96.hitbox[2]:
            platform96.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform97.hitbox[1] + platform97.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform97.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform97.hitbox[0] and player.plathitbox[0] < \
                platform97.hitbox[0] + platform97.hitbox[2]:
            platform97.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = platform99.x - 410
                player.y = platform99.y - 85
                pygame.time.delay(200)
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform98.hitbox[1] + platform98.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform98.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform98.hitbox[0] and player.plathitbox[0] < \
                platform98.hitbox[0] + platform98.hitbox[2]:
            platform98.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform99.hitbox[1] + platform99.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform99.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform99.hitbox[0] and player.plathitbox[0] < \
                platform99.hitbox[0] + platform99.hitbox[2]:
            platform99.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform100.hitbox[1] + platform100.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform100.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform100.hitbox[0] and player.plathitbox[0] < \
                platform100.hitbox[0] + platform100.hitbox[2]:
            platform100.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = platform102.x - 410
                player.y = platform102.y - 85
                pygame.time.delay(200)
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform101.hitbox[1] + platform101.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform101.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform101.hitbox[0] and player.plathitbox[0] < \
                platform101.hitbox[0] + platform101.hitbox[2]:
            platform101.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform102.hitbox[1] + platform102.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform102.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform102.hitbox[0] and player.plathitbox[0] < \
                platform102.hitbox[0] + platform102.hitbox[2]:
            platform102.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 23280
                player.y = 470
                player.onPlatform = False
        #else:
            #player.onPlatform = False

    if player.plathitbox[1] < platform103.hitbox[1] + platform103.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform103.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform103.hitbox[0] and player.plathitbox[0] < \
                platform103.hitbox[0] + platform103.hitbox[2]:
            platform103.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform104.hitbox[1] + platform104.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform104.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform104.hitbox[0] and player.plathitbox[0] < \
                platform104.hitbox[0] + platform104.hitbox[2]:
            platform104.hit()
            player.onPlatform = True
            if keys[pygame.K_UP]:
                portal.play()
                camx = 21790
                player.y = 400
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform105.hitbox[1] + platform105.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform105.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform105.hitbox[0] and player.plathitbox[0] < \
                platform105.hitbox[0] + platform105.hitbox[2]:
            platform105.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform106.hitbox[1] + platform106.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform106.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform106.hitbox[0] and player.plathitbox[0] < \
                platform106.hitbox[0] + platform106.hitbox[2]:
            platform106.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform107.hitbox[1] + platform107.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform107.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform107.hitbox[0] and player.plathitbox[0] < \
                platform107.hitbox[0] + platform107.hitbox[2]:
            platform107.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

    if player.plathitbox[1] < platform108.hitbox[1] + platform108.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform108.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform108.hitbox[0] and player.plathitbox[0] < \
                platform108.hitbox[0] + platform108.hitbox[2]:
            platform108.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False

# Colisão Parede ?
    if player.plathitbox[1] < wall5.hitbox[1] + wall5.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall5.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall5.hitbox[0] and player.plathitbox[0] < \
                wall5.hitbox[0] + wall5.hitbox[2]:
            camx -= 5
            player.walkCount = 0

    if player.plathitbox[1] < wall6.hitbox[1] + wall6.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall6.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall6.hitbox[0] and player.plathitbox[0] < \
                wall6.hitbox[0] + wall6.hitbox[2]:
            camx -= 5
            player.walkCount = 0

# Colisão Plataformas Jail
    if player.plathitbox[1] < platform109.hitbox[1] + platform109.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform109.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform109.hitbox[0] and player.plathitbox[0] < \
                platform109.hitbox[0] + platform109.hitbox[2]:
            platform109.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform110.hitbox[1] + platform110.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform110.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform110.hitbox[0] and player.plathitbox[0] < \
                platform110.hitbox[0] + platform110.hitbox[2]:
            platform110.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform111.hitbox[1] + platform111.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform111.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform111.hitbox[0] and player.plathitbox[0] < \
                platform111.hitbox[0] + platform111.hitbox[2]:
            platform111.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform112.hitbox[1] + platform112.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform112.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform112.hitbox[0] and player.plathitbox[0] < \
                platform112.hitbox[0] + platform112.hitbox[2]:
            platform112.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform113.hitbox[1] + platform113.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform113.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform113.hitbox[0] and player.plathitbox[0] < \
                platform113.hitbox[0] + platform113.hitbox[2]:
            platform113.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform114.hitbox[1] + platform114.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform114.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform114.hitbox[0] and player.plathitbox[0] < \
                platform114.hitbox[0] + platform114.hitbox[2]:
            platform114.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform115.hitbox[1] + platform115.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform115.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform115.hitbox[0] and player.plathitbox[0] < \
                platform115.hitbox[0] + platform115.hitbox[2]:
            platform115.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform116.hitbox[1] + platform116.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform116.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform116.hitbox[0] and player.plathitbox[0] < \
                platform116.hitbox[0] + platform116.hitbox[2]:
            platform116.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
    if player.plathitbox[1] < platform117.hitbox[1] + platform117.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > platform117.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > platform117.hitbox[0] and player.plathitbox[0] < \
                platform117.hitbox[0] + platform117.hitbox[2]:
            platform117.hit()
            player.onPlatform = True
        # else:
        # player.onPlatform = False
        
# Colisão Paredes Jail
    if player.plathitbox[1] < wall7.hitbox[1] + wall7.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall7.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall7.hitbox[0] and player.plathitbox[0] < \
                wall7.hitbox[0] + wall7.hitbox[2]:
            camx += 5
            player.walkCount = 0

    if player.plathitbox[1] < wall9.hitbox[1] + wall9.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall9.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall9.hitbox[0] and player.plathitbox[0] < \
                wall9.hitbox[0] + wall9.hitbox[2]:
            if digao.visible == True:
                camx -= 5
                player.walkCount = 0

    if player.plathitbox[1] < wall10.hitbox[1] + wall10.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall10.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall10.hitbox[0] and player.plathitbox[0] < \
                wall10.hitbox[0] + wall10.hitbox[2]:
            camx -= 5
            player.walkCount = 0

    if player.plathitbox[1] < wall11.hitbox[1] + wall11.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall11.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall11.hitbox[0] and player.plathitbox[0] < \
                wall11.hitbox[0] + wall11.hitbox[2]:
            camx += 5
            player.walkCount = 0
            
    if player.plathitbox[1] < wall12.hitbox[1] + wall12.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > wall12.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > wall12.hitbox[0] and player.plathitbox[0] < \
                wall12.hitbox[0] + wall12.hitbox[2]:
            camx -= 5
            player.walkCount = 0
# Interagir com alavancas
    if player.hitbox[1] < lever1.hitbox[1] + lever1.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > lever1.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > lever1.hitbox[0] and player.hitbox[0] < \
                lever1.hitbox[0] + lever1.hitbox[2]:
            if keys[pygame.K_UP]:
                lever1.hit()
                pygame.time.delay(100)
            
    if player.hitbox[1] < lever2.hitbox[1] + lever2.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > lever2.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > lever2.hitbox[0] and player.hitbox[0] < \
                lever2.hitbox[0] + lever2.hitbox[2]:
            if keys[pygame.K_UP]:
                lever2.hit()
                pygame.time.delay(100)
                
    if player.hitbox[1] < lever3.hitbox[1] + lever3.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > lever3.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > lever3.hitbox[0] and player.hitbox[0] < \
                lever3.hitbox[0] + lever3.hitbox[2]:
            if keys[pygame.K_UP]:
                lever3.hit()
                pygame.time.delay(100)
                
    if player.hitbox[1] < lever4.hitbox[1] + lever4.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > lever4.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > lever4.hitbox[0] and player.hitbox[0] < \
                lever4.hitbox[0] + lever4.hitbox[2]:
            if keys[pygame.K_UP]:
                lever4.hit()
                pygame.time.delay(100)
    
# Activator colisão
    if player.plathitbox[1] < activator.hitbox[1] + activator.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > activator.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > activator.hitbox[0] and player.plathitbox[0] < \
                activator.hitbox[0] + activator.hitbox[2]:
            if keys[pygame.K_UP]:
                if (lever1.cont % 2) == 0 and (lever2.cont % 2) != 0 and (lever3.cont % 2) != 0 and (lever4.cont % 2) == 0 and player.keys < 6:
                    if activator.kenigma == False:
                        sucesso.play()
                        win.blit(detonado, (58,232))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        key6.visible = True
                        activator.kenigma = True

                elif (lever1.cont % 2) != 0 and (lever2.cont % 2) == 0 and (lever3.cont % 2) != 0 and (lever4.cont % 2) != 0:
                    if player.keys < 6:
                        fail.play()
                        win.blit(faltakeys, (128,133))
                        pygame.display.update()
                        pygame.time.delay(2000)

                    if activator.enigma == False and player.keys == 6:
                        sucesso.play()
                        win.blit(detonado, (58,232))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        activator.enigma = True
                        portal1.skill = True
                else:
                    if activator.enigma == False:
                        fail.play()
                        win.blit(errado,(128,133))
                        pygame.display.update()
                        pygame.time.delay(2000)

# Funções do portal1
    if player.plathitbox[1] < portal1.hitbox[1] + portal1.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > portal1.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > portal1.hitbox[0] and player.plathitbox[0] < \
                portal1.hitbox[0] + portal1.hitbox[2]:
            if keys[pygame.K_UP]:
                camx = 27081
                music = pygame.mixer.music.load("BGM/BGM06.mp3")
                pygame.mixer.music.play(-1)
                if life < 3 and player.health < 3:
                    life = 3
                    player.health = 3

# Funções do portal2
    if player.plathitbox[1] < portal2.hitbox[1] + portal2.hitbox[3] and player.plathitbox[1] + \
            player.plathitbox[
                3] > portal2.hitbox[1]:
        if player.plathitbox[0] + player.plathitbox[2] > portal2.hitbox[0] and player.plathitbox[0] < \
                portal2.hitbox[0] + portal2.hitbox[2]:
            if keys[pygame.K_UP]:
                camx = 30075
                music = pygame.mixer.music.load("BGM/BGMendgame.mp3")
                pygame.mixer.music.play(-1)

    if portal1.skillCount == 131:
        portal1.skill = False
        portal1.visible = True

    if portal1.skillCount == 1:
        portalopen1.play()

    if portal1.skillCount == 80:
        portalopen2.play()

    if portal2.skillCount == 131:
        portal2.skill = False
        portal2.visible = True

    if portal2.skillCount == 80:
        portalopen2.play()
        
# Colisão Laser
    if player.hitbox[1] < laser.hitbox[1] + laser.hitbox[3] and player.hitbox[1] + player.hitbox[3] > \
            laser.hitbox[
                1]:
        if player.hitbox[0] + player.hitbox[2] > laser.hitbox[0] and player.hitbox[0] < laser.hitbox[0] + \
                laser.hitbox[2]:
            if laser.walkCount >= 33:
                camx = checkpoint
                player.x = 400
                player.y = 470
                player.jumpCount = 10
                player.walkCount = 0
                player.isJump = False

    if laser.walkCount == 20 and camx >= 19546 and camx <= 20400:
       laserhit.play()

    if player.hitbox[1] < digao.hitbox[1] + digao.hitbox[3] and player.hitbox[1] + player.hitbox[3] > digao.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > digao.hitbox[0] and player.hitbox[0] < digao.hitbox[0] + \
                digao.hitbox[2]:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470
            
    # Skill1 digão
    if digao.x == 28101 and digao.vel < 0:
        digao.onskill1 = True

    if digao.skill1Count == 1 and camx >= 26931:
        digaoskill1.play()

    if digao.skill1Count == 107:
        digao.onskill1 = False
        digao.skill1Count = 0

    if digao.skill1Count >= 90 and camx >= 27151 and camx <= 29615:
        if player.y >= 400:
            player.hit()
            life -= 1
            player.health -= 1
            camx = checkpoint
            player.x = 400
            player.y = 470

    # Skill2 Digão
    if player.hitbox[1] < arrow1.hitbox[1] + arrow1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > arrow1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > arrow1.hitbox[0] and player.hitbox[0] < arrow1.hitbox[0] + \
                arrow1.hitbox[2]:
            if arrow1.visible == True:
                player.hit()
                life -= 1
                player.health -= 1
                camx = checkpoint
                player.x = 400
                player.y = 470
                arrow1.visible = False
                arrow1.width = 0
                arrow1.heigth = 0
                arrow1.x = 28611
            
    if player.hitbox[1] < arrow2.hitbox[1] + arrow2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > arrow2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > arrow2.hitbox[0] and player.hitbox[0] < arrow2.hitbox[0] + \
                arrow2.hitbox[2]:
            if arrow2.visible == True:
                player.hit()
                life -= 1
                player.health -= 1
                camx = checkpoint
                player.x = 400
                player.y = 470
                arrow2.visible = False
                arrow2.width = 0
                arrow2.heigth = 0
                arrow2.x = 28611
            
    if digao.x == 27865 and digao.vel < 0:
        digao.onskill2 = True

    if digao.skill2Count == 1 and camx >= 26931:
        digaoskill2.play()
        
    if digao.skill2Count > 20 and digao.ondie == False:
        arrow1.visible = True
        arrow1.width = 57
        arrow1.heigth = 33
        arrow1.x -= 10

        arrow2.visible = True
        arrow2.width = 57
        arrow2.heigth = 33
        arrow2.x -= 10

    if arrow1.x == 27581:
        arrow1.visible = False
        arrow1.width = 0
        arrow1.heigth = 0
        arrow1.x = 28611

    if arrow2.x == 27581:
        arrow2.visible = False
        arrow2.width = 0
        arrow2.heigth = 0
        arrow2.x = 28611
        
    if digao.skill2Count == 123:
        digao.onskill2 = False
        digao.skill2Count = 0
        arrow1.visible = False
        arrow1.width = 0
        arrow1.heigth = 0
        arrow1.x = 28611

        arrow2.visible = False
        arrow2.width = 0
        arrow2.heigth = 0
        arrow2.x = 28611

    # Skill3 Digão
    if digao.x == 28405 and digao.vel < 0:
        digao.onskill3 = True

    if digao.skill3Count == 1 and camx >= 26931:
        digaoskill3.play()

    if digao.skill3Count == 107:
        digao.onskill3 = False
        digao.skill3Count = 0

    if digao.skill3Count >= 80:
        jar1.visible = True
        jar2.visible = True
        jar3.visible = True
        jar4.visible = True

    if jar1.walkCount == 77:
        jar1.walkCount = 0
        jar1.visible = False
        jar2.walkCount = 0
        jar2.visible = False
        jar3.walkCount = 0
        jar3.visible = False
        jar4.walkCount = 0
        jar4.visible = False

    if jar1.walkCount == 27 and camx >= 26931:
        jarexp.play()

    if player.hitbox[1] < jar1.hitbox[1] + jar1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > jar1.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > jar1.hitbox[0] and player.hitbox[0] < jar1.hitbox[0] + \
                jar1.hitbox[2]:
            if jar1.walkCount >= 53:
                player.hit()
                life -= 1
                player.health -= 1
                camx = checkpoint
                player.x = 400
                player.y = 470

    if player.hitbox[1] < jar2.hitbox[1] + jar2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > jar2.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > jar2.hitbox[0] and player.hitbox[0] < jar2.hitbox[0] + \
                jar2.hitbox[2]:
            if jar2.walkCount >= 53:
                player.hit()
                life -= 1
                player.health -= 1
                camx = checkpoint
                player.x = 400
                player.y = 470

    if player.hitbox[1] < jar3.hitbox[1] + jar3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > jar3.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > jar3.hitbox[0] and player.hitbox[0] < jar3.hitbox[0] + \
                jar3.hitbox[2]:
            if jar3.walkCount >= 53:
                player.hit()
                life -= 1
                player.health -= 1
                camx = checkpoint
                player.x = 400
                player.y = 470

    if player.hitbox[1] < jar4.hitbox[1] + jar4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > jar4.hitbox[
        1]:
        if player.hitbox[0] + player.hitbox[2] > jar4.hitbox[0] and player.hitbox[0] < jar4.hitbox[0] + \
                jar4.hitbox[2]:
            if jar4.walkCount >= 53:
                player.hit()
                life -= 1
                player.health -= 1
                camx = checkpoint
                player.x = 400
                player.y = 470

    if digao.dieCount >= 155:
        digao.visible = False

    key4.x = stumpy.x + 93
    if KSlime.visible == True:
        key5.x = KSlime.x + 103
    key6.x = portal1.x + 98
    key7.x = digao.x + 101

    # Colisão Keys
    if player.hitbox[1] < key1.hitbox[1] + key1.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key1.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key1.hitbox[0] and player.hitbox[0] < \
                key1.hitbox[0] + key1.hitbox[2]:
            if keys[pygame.K_UP]:
                if key1.visible == True:
                    key1.visible = False
                    loot.play()
                    player.keys += 1
    
    if player.hitbox[1] < key2.hitbox[1] + key2.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key2.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key2.hitbox[0] and player.hitbox[0] < \
                key2.hitbox[0] + key2.hitbox[2]:
            if keys[pygame.K_UP]:
                if key2.visible == True:
                    key2.visible = False
                    loot.play()
                    player.keys += 1
                
    if player.hitbox[1] < key3.hitbox[1] + key3.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key3.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key3.hitbox[0] and player.hitbox[0] < \
                key3.hitbox[0] + key3.hitbox[2]:
            if keys[pygame.K_UP]:
                if key3.visible == True:
                    key3.visible = False
                    loot.play()
                    player.keys += 1
                
    if player.hitbox[1] < key4.hitbox[1] + key4.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key4.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key4.hitbox[0] and player.hitbox[0] < \
                key4.hitbox[0] + key4.hitbox[2]:
            if keys[pygame.K_UP]:
                if key4.visible == True:
                    key4.visible = False
                    loot.play()
                    player.keys += 1
                
    if player.hitbox[1] < key5.hitbox[1] + key5.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key5.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key5.hitbox[0] and player.hitbox[0] < \
                key5.hitbox[0] + key5.hitbox[2]:
            if keys[pygame.K_UP]:
                if key5.visible == True:
                    key5.visible = False
                    loot.play()
                    player.keys += 1
                
    if player.hitbox[1] < key6.hitbox[1] + key6.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key6.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key6.hitbox[0] and player.hitbox[0] < \
                key6.hitbox[0] + key6.hitbox[2]:
            if keys[pygame.K_UP]:
                if key6.visible == True:
                    key6.visible = False
                    loot.play()
                    player.keys += 1
                
    if player.hitbox[1] < key7.hitbox[1] + key7.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > key7.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > key7.hitbox[0] and player.hitbox[0] < \
                key7.hitbox[0] + key7.hitbox[2]:
            if keys[pygame.K_UP]:
                if key7.visible == True:
                    key7.visible = False
                    loot.play()
                    player.keys += 1

    if player.hitbox[1] < jail.hitbox[1] + jail.hitbox[3] and player.hitbox[1] + \
            player.hitbox[
                3] > jail.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > jail.hitbox[0] and player.hitbox[0] < \
                jail.hitbox[0] + jail.hitbox[2]:
            if keys[pygame.K_UP] and jail.visible == True:
                if player.keys == 7:
                    jailopen.play()
                    portal2.skill = True
                    player.keys = 0
                    pygame.time.delay(100)
                    jail.open = True
                else:
                    fail.play()
                    win.blit(faltakeys, (128, 133))
                    pygame.display.update()
                    pygame.time.delay(2000)

    if jail.open == True:
        jail.visible = False

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

    #Buracos ?
    elif camx > 19055 and camx <= 19195 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 19960 and camx <= 20005 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 20425 and camx <= 20785 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 21775 and camx <= 23205 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

    elif camx > 23855 and camx <= 24230 and player.isJump == False and player.onPlatform == False:
        player.y = player.y + 5

# Esteiras ?
    elif camx > 18410 and camx <= 18950 and player.y == 470:
        camx -= 3

    elif camx > 18950 and camx <= 19051 and player.y == 470:
        camx += 3

    elif camx > 19202 and camx <= 19802 and player.y == 470:
        camx -= 3

    elif camx > 19802 and camx <= 20082 and player.y == 470:
        camx += 3

    elif camx > 20082 and camx <= 20282 and player.y == 470:
        camx -= 3

    elif camx > 20282 and camx <= 20417 and player.y == 470:
        camx += 3

    elif camx > 20837 and camx <= 21572 and player.y == 470:
        camx -= 3

    elif camx > 21572 and camx <= 21722 and player.y == 470:
        camx += 5

    elif camx > 23200 and camx <= 23831 and player.y == 470:
        camx -= 3

    elif player.y > 470:
        player.y = 470

    # Colisão Flechas
    for arrow in arrows:
        # Colisão Flechas Monstros Porto Lith
        if arrow.y - arrow.radius < snail1.hitbox[1] + snail1.hitbox[3] and arrow.y + arrow.radius > snail1.hitbox[1]:
            if arrow.x + arrow.radius > snail1.hitbox[0] and arrow.x - arrow.radius < snail1.hitbox[0] + snail1.hitbox[
                2]:
                snail1.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail2.hitbox[1] + snail2.hitbox[3] and arrow.y + arrow.radius > snail2.hitbox[1]:
            if arrow.x + arrow.radius > snail2.hitbox[0] and arrow.x - arrow.radius < snail2.hitbox[0] + snail2.hitbox[
                2]:
                snail2.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail3.hitbox[1] + snail3.hitbox[3] and arrow.y + arrow.radius > snail3.hitbox[1]:
            if arrow.x + arrow.radius > snail3.hitbox[0] and arrow.x - arrow.radius < snail3.hitbox[0] + snail3.hitbox[
                2]:
                snail3.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail4.hitbox[1] + snail4.hitbox[3] and arrow.y + arrow.radius > snail4.hitbox[1]:
            if arrow.x + arrow.radius > snail4.hitbox[0] and arrow.x - arrow.radius < snail4.hitbox[0] + snail4.hitbox[
                2]:
                snail4.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail5.hitbox[1] + snail5.hitbox[3] and arrow.y + arrow.radius > snail5.hitbox[1]:
            if arrow.x + arrow.radius > snail5.hitbox[0] and arrow.x - arrow.radius < snail5.hitbox[0] + snail5.hitbox[
                2]:
                snail5.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail6.hitbox[1] + snail6.hitbox[3] and arrow.y + arrow.radius > snail6.hitbox[1]:
            if arrow.x + arrow.radius > snail6.hitbox[0] and arrow.x - arrow.radius < snail6.hitbox[0] + snail6.hitbox[
                2]:
                snail6.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < snail7.hitbox[1] + snail7.hitbox[3] and arrow.y + arrow.radius > snail7.hitbox[1]:
            if arrow.x + arrow.radius > snail7.hitbox[0] and arrow.x - arrow.radius < snail7.hitbox[0] + snail7.hitbox[
                2]:
                snail7.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        # Colisão Flechas Henesys
        if arrow.y - arrow.radius < cogu1.hitbox[1] + cogu1.hitbox[3] and arrow.y + arrow.radius > cogu1.hitbox[1]:
            if arrow.x + arrow.radius > cogu1.hitbox[0] and arrow.x - arrow.radius < cogu1.hitbox[0] + cogu1.hitbox[
                2]:
                cogu1.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu2.hitbox[1] + cogu2.hitbox[3] and arrow.y + arrow.radius > cogu2.hitbox[1]:
            if arrow.x + arrow.radius > cogu2.hitbox[0] and arrow.x - arrow.radius < cogu2.hitbox[0] + cogu2.hitbox[
                2]:
                cogu2.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu3.hitbox[1] + cogu3.hitbox[3] and arrow.y + arrow.radius > cogu3.hitbox[1]:
            if arrow.x + arrow.radius > cogu3.hitbox[0] and arrow.x - arrow.radius < cogu3.hitbox[0] + cogu3.hitbox[
                2]:
                cogu3.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu4.hitbox[1] + cogu4.hitbox[3] and arrow.y + arrow.radius > cogu4.hitbox[1]:
            if arrow.x + arrow.radius > cogu4.hitbox[0] and arrow.x - arrow.radius < cogu4.hitbox[0] + cogu4.hitbox[
                2]:
                cogu4.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu5.hitbox[1] + cogu5.hitbox[3] and arrow.y + arrow.radius > cogu5.hitbox[1]:
            if arrow.x + arrow.radius > cogu5.hitbox[0] and arrow.x - arrow.radius < cogu5.hitbox[0] + cogu5.hitbox[
                2]:
                cogu5.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu6.hitbox[1] + cogu6.hitbox[3] and arrow.y + arrow.radius > cogu6.hitbox[1]:
            if arrow.x + arrow.radius > cogu6.hitbox[0] and arrow.x - arrow.radius < cogu6.hitbox[0] + cogu6.hitbox[
                2]:
                cogu6.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu7.hitbox[1] + cogu7.hitbox[3] and arrow.y + arrow.radius > cogu7.hitbox[1]:
            if arrow.x + arrow.radius > cogu7.hitbox[0] and arrow.x - arrow.radius < cogu7.hitbox[0] + cogu7.hitbox[
                2]:
                cogu7.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu8.hitbox[1] + cogu8.hitbox[3] and arrow.y + arrow.radius > cogu8.hitbox[1]:
            if arrow.x + arrow.radius > cogu8.hitbox[0] and arrow.x - arrow.radius < cogu8.hitbox[0] + cogu8.hitbox[
                2]:
                cogu8.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu9.hitbox[1] + cogu9.hitbox[3] and arrow.y + arrow.radius > cogu9.hitbox[1]:
            if arrow.x + arrow.radius > cogu9.hitbox[0] and arrow.x - arrow.radius < cogu9.hitbox[0] + cogu9.hitbox[
                2]:
                cogu9.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu10.hitbox[1] + cogu10.hitbox[3] and arrow.y + arrow.radius > cogu10.hitbox[1]:
            if arrow.x + arrow.radius > cogu10.hitbox[0] and arrow.x - arrow.radius < cogu10.hitbox[0] + cogu10.hitbox[
                2]:
                cogu10.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu11.hitbox[1] + cogu11.hitbox[3] and arrow.y + arrow.radius > cogu11.hitbox[1]:
            if arrow.x + arrow.radius > cogu11.hitbox[0] and arrow.x - arrow.radius < cogu11.hitbox[0] + cogu11.hitbox[
                2]:
                cogu11.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu12.hitbox[1] + cogu12.hitbox[3] and arrow.y + arrow.radius > cogu12.hitbox[1]:
            if arrow.x + arrow.radius > cogu12.hitbox[0] and arrow.x - arrow.radius < cogu12.hitbox[0] + cogu12.hitbox[
                2]:
                cogu12.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu13.hitbox[1] + cogu13.hitbox[3] and arrow.y + arrow.radius > cogu13.hitbox[1]:
            if arrow.x + arrow.radius > cogu13.hitbox[0] and arrow.x - arrow.radius < cogu13.hitbox[0] + cogu13.hitbox[
                2]:
                cogu13.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < cogu14.hitbox[1] + cogu14.hitbox[3] and arrow.y + arrow.radius > cogu14.hitbox[1]:
            if arrow.x + arrow.radius > cogu14.hitbox[0] and arrow.x - arrow.radius < cogu14.hitbox[0] + cogu14.hitbox[
                2]:
                cogu14.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        # Colisão Flechas Perion
        if arrow.y - arrow.radius < toco1.hitbox[1] + toco1.hitbox[3] and arrow.y + arrow.radius > toco1.hitbox[1]:
            if arrow.x + arrow.radius > toco1.hitbox[0] and arrow.x - arrow.radius < toco1.hitbox[0] + toco1.hitbox[
                2]:
                toco1.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco2.hitbox[1] + toco2.hitbox[3] and arrow.y + arrow.radius > toco2.hitbox[1]:
            if arrow.x + arrow.radius > toco2.hitbox[0] and arrow.x - arrow.radius < toco2.hitbox[0] + toco2.hitbox[
                2]:
                toco2.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco3.hitbox[1] + toco3.hitbox[3] and arrow.y + arrow.radius > toco3.hitbox[1]:
            if arrow.x + arrow.radius > toco3.hitbox[0] and arrow.x - arrow.radius < toco3.hitbox[0] + toco3.hitbox[
                2]:
                toco3.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco4.hitbox[1] + toco4.hitbox[3] and arrow.y + arrow.radius > toco4.hitbox[1]:
            if arrow.x + arrow.radius > toco4.hitbox[0] and arrow.x - arrow.radius < toco4.hitbox[0] + toco4.hitbox[
                2]:
                toco4.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco5.hitbox[1] + toco5.hitbox[3] and arrow.y + arrow.radius > toco5.hitbox[1]:
            if arrow.x + arrow.radius > toco5.hitbox[0] and arrow.x - arrow.radius < toco5.hitbox[0] + toco5.hitbox[
                2]:
                toco5.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco6.hitbox[1] + toco6.hitbox[3] and arrow.y + arrow.radius > toco6.hitbox[1]:
            if arrow.x + arrow.radius > toco6.hitbox[0] and arrow.x - arrow.radius < toco6.hitbox[0] + toco6.hitbox[
                2]:
                toco6.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco7.hitbox[1] + toco7.hitbox[3] and arrow.y + arrow.radius > toco7.hitbox[1]:
            if arrow.x + arrow.radius > toco7.hitbox[0] and arrow.x - arrow.radius < toco7.hitbox[0] + toco7.hitbox[
                2]:
                toco7.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco8.hitbox[1] + toco8.hitbox[3] and arrow.y + arrow.radius > toco8.hitbox[1]:
            if arrow.x + arrow.radius > toco8.hitbox[0] and arrow.x - arrow.radius < toco8.hitbox[0] + toco8.hitbox[
                2]:
                toco8.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco9.hitbox[1] + toco9.hitbox[3] and arrow.y + arrow.radius > toco9.hitbox[1]:
            if arrow.x + arrow.radius > toco9.hitbox[0] and arrow.x - arrow.radius < toco9.hitbox[0] + toco9.hitbox[
                2]:
                toco9.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco10.hitbox[1] + toco10.hitbox[3] and arrow.y + arrow.radius > toco10.hitbox[1]:
            if arrow.x + arrow.radius > toco10.hitbox[0] and arrow.x - arrow.radius < toco10.hitbox[0] + toco10.hitbox[
                2]:
                toco10.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco11.hitbox[1] + toco11.hitbox[3] and arrow.y + arrow.radius > toco11.hitbox[1]:
            if arrow.x + arrow.radius > toco11.hitbox[0] and arrow.x - arrow.radius < toco11.hitbox[0] + toco11.hitbox[
                2]:
                toco11.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco12.hitbox[1] + toco12.hitbox[3] and arrow.y + arrow.radius > toco12.hitbox[1]:
            if arrow.x + arrow.radius > toco12.hitbox[0] and arrow.x - arrow.radius < toco12.hitbox[0] + toco12.hitbox[
                2]:
                toco12.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco13.hitbox[1] + toco13.hitbox[3] and arrow.y + arrow.radius > toco13.hitbox[1]:
            if arrow.x + arrow.radius > toco13.hitbox[0] and arrow.x - arrow.radius < toco13.hitbox[0] + toco13.hitbox[
                2]:
                toco13.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco14.hitbox[1] + toco14.hitbox[3] and arrow.y + arrow.radius > toco14.hitbox[1]:
            if arrow.x + arrow.radius > toco14.hitbox[0] and arrow.x - arrow.radius < toco14.hitbox[0] + toco14.hitbox[
                2]:
                toco14.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco15.hitbox[1] + toco15.hitbox[3] and arrow.y + arrow.radius > toco15.hitbox[1]:
            if arrow.x + arrow.radius > toco15.hitbox[0] and arrow.x - arrow.radius < toco15.hitbox[0] + toco15.hitbox[
                2]:
                toco15.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < toco16.hitbox[1] + toco16.hitbox[3] and arrow.y + arrow.radius > toco16.hitbox[1]:
            if arrow.x + arrow.radius > toco16.hitbox[0] and arrow.x - arrow.radius < toco16.hitbox[0] + toco16.hitbox[
                2]:
                toco16.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        # Colisão Flecha Stumpy
        if arrow.y - arrow.radius < stumpy.hitbox[1] + stumpy.hitbox[3] and arrow.y + arrow.radius > stumpy.hitbox[1]:
            if arrow.x + arrow.radius > stumpy.hitbox[0] and arrow.x - arrow.radius < stumpy.hitbox[0] + stumpy.hitbox[
                2]:
                stumpy.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        # Colisão Flechas Ellinia
        if arrow.y - arrow.radius < slime1.hitbox[1] + slime1.hitbox[3] and arrow.y + arrow.radius > slime1.hitbox[1]:
            if arrow.x + arrow.radius > slime1.hitbox[0] and arrow.x - arrow.radius < slime1.hitbox[0] + slime1.hitbox[
                2]:
                slime1.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime2.hitbox[1] + slime2.hitbox[3] and arrow.y + arrow.radius > slime2.hitbox[1]:
            if arrow.x + arrow.radius > slime2.hitbox[0] and arrow.x - arrow.radius < slime2.hitbox[0] + slime2.hitbox[
                2]:
                slime2.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime3.hitbox[1] + slime3.hitbox[3] and arrow.y + arrow.radius > slime3.hitbox[1]:
            if arrow.x + arrow.radius > slime3.hitbox[0] and arrow.x - arrow.radius < slime3.hitbox[0] + slime3.hitbox[
                2]:
                slime3.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime4.hitbox[1] + slime4.hitbox[3] and arrow.y + arrow.radius > slime4.hitbox[1]:
            if arrow.x + arrow.radius > slime4.hitbox[0] and arrow.x - arrow.radius < slime4.hitbox[0] + slime4.hitbox[
                2]:
                slime4.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime5.hitbox[1] + slime5.hitbox[3] and arrow.y + arrow.radius > slime5.hitbox[1]:
            if arrow.x + arrow.radius > slime5.hitbox[0] and arrow.x - arrow.radius < slime5.hitbox[0] + slime5.hitbox[
                2]:
                slime5.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime6.hitbox[1] + slime6.hitbox[3] and arrow.y + arrow.radius > slime6.hitbox[1]:
            if arrow.x + arrow.radius > slime6.hitbox[0] and arrow.x - arrow.radius < slime6.hitbox[0] + slime6.hitbox[
                2]:
                slime6.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime7.hitbox[1] + slime7.hitbox[3] and arrow.y + arrow.radius > slime7.hitbox[1]:
            if arrow.x + arrow.radius > slime7.hitbox[0] and arrow.x - arrow.radius < slime7.hitbox[0] + slime7.hitbox[
                2]:
                slime7.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime8.hitbox[1] + slime8.hitbox[3] and arrow.y + arrow.radius > slime8.hitbox[1]:
            if arrow.x + arrow.radius > slime8.hitbox[0] and arrow.x - arrow.radius < slime8.hitbox[0] + slime8.hitbox[
                2]:
                slime8.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime9.hitbox[1] + slime9.hitbox[3] and arrow.y + arrow.radius > slime9.hitbox[1]:
            if arrow.x + arrow.radius > slime9.hitbox[0] and arrow.x - arrow.radius < slime9.hitbox[0] + slime9.hitbox[
                2]:
                slime9.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < slime10.hitbox[1] + slime10.hitbox[3] and arrow.y + arrow.radius > slime10.hitbox[
            1]:
            if arrow.x + arrow.radius > slime10.hitbox[0] and arrow.x - arrow.radius < slime10.hitbox[0] + \
                    slime10.hitbox[
                        2]:
                slime10.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))

        if arrow.y - arrow.radius < KSlime.hitbox[1] + KSlime.hitbox[3] and arrow.y + arrow.radius > KSlime.hitbox[1]:
            if arrow.x + arrow.radius > KSlime.hitbox[0] and arrow.x - arrow.radius < KSlime.hitbox[0] + KSlime.hitbox[
                2]:
                KSlime.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))
        
        # Colisão Paredes Jail
        if arrow.y - arrow.radius < wall8.hitbox[1] + wall8.hitbox[3] and arrow.y + arrow.radius > wall8.hitbox[1]:
            if arrow.x + arrow.radius > wall8.hitbox[0] and arrow.x - arrow.radius < wall8.hitbox[0] + wall8.hitbox[
                2]:
                if arrows != []:
                    arrows.pop(arrows.index(arrow))
                    
        if arrow.y - arrow.radius < wall9.hitbox[1] + wall9.hitbox[3] and arrow.y + arrow.radius > wall9.hitbox[1]:
            if arrow.x + arrow.radius > wall9.hitbox[0] and arrow.x - arrow.radius < wall9.hitbox[0] + wall9.hitbox[
                2]:
                if arrows != []:
                    arrows.pop(arrows.index(arrow))
                    
        if arrow.y - arrow.radius < digao.hitbox[1] + digao.hitbox[3] and arrow.y + arrow.radius > digao.hitbox[1]:
            if arrow.x + arrow.radius > digao.hitbox[0] and arrow.x - arrow.radius < digao.hitbox[0] + digao.hitbox[
                2]:
                digao.hit()
                if arrows != []:
                    arrows.pop(arrows.index(arrow))
        
        if arrow.x < 780 and arrow.x > 0:
            arrow.x += arrow.vel
        else:
            if arrows != []:  # if utilizado para corrigir o bug que tenta deletar uma flecha que já foi deletada ao colidir com um monstro.
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
                    projectile(round(player.x + player.width // 2), round(player.y + player.height // 1.7), 13,
                               facingB))
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
