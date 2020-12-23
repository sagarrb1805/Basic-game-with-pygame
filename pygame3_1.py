import pygame
pygame.init()
window = pygame.display.set_mode((600, 450))
pygame.display.set_caption("my game")
walkRight = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),
             pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png")]
walkLeft = [pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),
            pygame.image.load("L6.png"), pygame.image.load("L7.png"), pygame.image.load("L8.png"), pygame.image.load("L9.png")]
bg = pygame.image.load("bg.jpg")
char = pygame.image.load("standing.png")
height = 60
width = 40
x = 30
y = 350
vel = 15
isJump = False
jumpCount = 10
run = True
right = False
left = False
walkcount = 0
def screen_draw():
    global walkcount
    window.blit(bg,(0,0))
    if walkcount+1 >= 36:
        walkcount = 0
    if left:
        window.blit(walkLeft[walkcount//4], (x, y))
        walkcount += 1
    elif right:
        window.blit(walkRight[walkcount//4], (x, y))
        walkcount += 1
    else:
        window.blit(char, (x,y))
    pygame.display.update()


while run:
    #pygame.time.delay(100)
    pygame.time.Clock().tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not(isJump):

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            direction = 1
            if jumpCount < 0:
                direction = -1
            y -= (jumpCount**2)*direction
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    if keys[pygame.K_RIGHT] and x < 600 - width:
        right = True
        left = False
        x += vel

    elif keys[pygame.K_LEFT] and x > 0:
        left = True
        right = False
        x -= vel
    else:
        left = False
        right = False
        walkcount = 0
    screen_draw()

pygame.quit()