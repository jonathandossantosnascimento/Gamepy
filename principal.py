import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(1024, 768))
print('setup end')

print('start Loop')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
