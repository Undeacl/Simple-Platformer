import pygame
from Player_Final import Player
from World import World
from os import path
import pickle

#_________set_up_________

pygame.init()
pygame.font.init()

WIDTH = 1000

HEIGHT = 950

FPS = 60

SCALE = 1.4

SPEED = 10

TILE_SIZE = 50

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('image/Environment/sky.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

tile_size = 50

player = Player(100, HEIGHT - 100, SCALE, SPEED, HEIGHT)

#_________functions_________

#move the player and also animations
def move_and_animations(key):
    
    #only move if the player is not dead (duh)
    if not player.death:

        #starts charging the jump only if the player has not jump
        if key[pygame.K_SPACE] and player.jump_count < 1:

            player.time_down += 100

            #indicate max jump height
            if player.time_down >= 6000:

                player.update_animations(player.animations_types.index("MAX_Launch"))

            else:
 
                player.update_animations(player.animations_types.index("Launch"))
            
        #move the player left
        elif key[pygame.K_a] or key[pygame.K_LEFT]:
        
            player.move_left(world, WIDTH, HEIGHT)

            #normal animation
            if not player.in_air:
        
                player.update_animations(player.animations_types.index("Run"))
        
            #if player is in air, still move the player, but animation is jumping
            elif player.in_air:
        
                player.update_animations(player.animations_types.index("Jumping"))

        #move the player right
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        
            player.move_right(world, WIDTH, HEIGHT)
            
            #normal animation
            if not player.in_air:
        
                player.update_animations(player.animations_types.index("Run"))

            #if player is in air, still move the player, but animation is jumping
            elif player.in_air:
        
                player.update_animations(player.animations_types.index("Jumping"))

        #player is in air and not moving. Jumping in place
        elif player.in_air:
        
            player.update_animations(player.animations_types.index("Jumping"))

        else:
            
            #idle animation
            player.update_animations(player.animations_types.index("Idle"))

        player.jumping(world, WIDTH, HEIGHT)

# draw the grid
def draw_grid():
	for line in range(0, 24):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (WIDTH, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, HEIGHT))

#loading in a world from CSV
def reset_level(level):
    #load the next level
    
    if path.exists(f'levels/level{level}_data'):
    
        pickle_in = open(f'levels/level{level}_data', 'rb')
    
        world_map = pickle.load(pickle_in)

    world = World(world_map, tile_size, WIDTH/(WIDTH/TILE_SIZE), HEIGHT/(HEIGHT/TILE_SIZE))
    
    return world

#first level
if path.exists(f'levels/level{player.level}_data'):
    
    pickle_in = open(f'levels/level{player.level}_data', 'rb')
    
    world_map = pickle.load(pickle_in)

#original
world = World(world_map, tile_size, WIDTH/(WIDTH/TILE_SIZE), HEIGHT/(HEIGHT/TILE_SIZE))

#_________run_________

def game():
    global world
    run = True
    
    while run:

        screen.blit(background, (0,0))

        clock.tick(FPS)

        # draw_grid()

        world.draw(screen)
    
        player.check_death()
    
        world.exit_group.draw(screen)

        player.draw(screen)
    
        world.lava_group.draw(screen)
        world.flag_group.draw(screen)
        
        world.flag_group.update(screen, tile_size)

        #load the next level when player hit the portal. Level is complete
        if player.level_complete:

            if player.level <= 2:

                player.rect.x = 50

                player.rect.y = HEIGHT - 100

                player.last_x = 50

                player.last_y = HEIGHT - 100
                
                player.dx = 0
                
                player.dy = 0
                
                world.lava_group.empty()
                
                world.exit_group.empty()
                
                world = []
                
                world = reset_level(player.level)
                
                player.level_complete = False

        key = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

            #actual jumping
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_SPACE and player.jump_count < 1:

                    player.jump = True

                    player.in_air = True

        move_and_animations(key)

        pygame.display.update()

if __name__ == "__main__":
    game()

pygame.quit()