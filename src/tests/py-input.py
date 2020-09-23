import pygame

screen = pygame.display.set_mode((500,500))

running = True
left = False
right = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    input_state = pygame.key.get_pressed()

    if input_state[pygame.K_LEFT]:
        print('lefting')