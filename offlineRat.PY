import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 600, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dinosaur Game")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Dinosaurio
dino_width, dino_height = 50, 50
dino_x, dino_y = 50, height - dino_height - 10
dino_jump = False
dino_jump_count = 10

# Obstáculo
cactus_width, cactus_height = 20, 50
cactus_x, cactus_y = width, height - cactus_height - 10
cactus_speed = 5

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

def draw_dino():
    pygame.draw.rect(screen, white, [dino_x, dino_y, dino_width, dino_height])

def draw_cactus():
    pygame.draw.rect(screen, white, [cactus_x, cactus_y, cactus_width, cactus_height])

def draw_score():
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not dino_jump:
            dino_jump = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not dino_jump:
        dino_jump = True

    # Movimiento del dinosaurio
    if dino_jump:
        if dino_jump_count >= -10:
            neg = 1
            if dino_jump_count < 0:
                neg = -1
            dino_y -= (dino_jump_count ** 2) * 0.5 * neg
            dino_jump_count -= 1
        else:
            dino_jump = False
            dino_jump_count = 10

    # Movimiento del cactus
    cactus_x -= cactus_speed
    if cactus_x < 0:
        cactus_x = width
        score += 1

    # Colisiones
    if dino_x < cactus_x + cactus_width and dino_x + dino_width > cactus_x and dino_y < cactus_y + cactus_height and dino_y + dino_height > cactus_y:
        print("Game Over")
        running = False

    # Dibujar elementos en la pantalla
    screen.fill(black)
    draw_dino()
    draw_cactus()
    draw_score()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
      