import pygame
from Animations_Final import SpriteSheet


class Player(pygame.sprite.Sprite):

    JUMP_HEIGHT = 5

    #create the player
    def __init__(self, x, y, scale, speed, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        #character setup
        self.speed = speed
        
        self.flip = False
        
        self.jump = False
        
        self.in_air = False

        self.death = False

        self.animation_complete = False
        
        self.time_down = 0
        
        self.vel_y = 0
        
        self.dy = 0
        
        self.dx = 0
        
        self.jump_count = 0

        self.last_x = 50

        self.last_y = HEIGHT - 100

        self.check_happen = 0

        #levels
        self.level = 1

        self.level_complete = False

        #animation for character
        self.animate = 0
        
        self.master_animation_list = []
        
        self.last_update = pygame.time.get_ticks()
        
        self.frame = 0

        self.animations_types = ["Idle", "Run", "Launch", "MAX_Launch", "Jumping", "Falling", "Fall", "Death"]

        #creating all the animation and putting them into seperate list
        for animations in self.animations_types:
            
            empty_list = []

            type = pygame.image.load(f'image/Characters/Pink/Pink_Monster_{animations}.png').convert_alpha()
            
            sprite = SpriteSheet(type, 32)
            
            #iterate how many sprite is being added
            for image in range(int(sprite.total)):

                empty_list.append(sprite.get_image(image, 32, 32, scale))
            
            self.master_animation_list.append(empty_list)

        #define the character
        self.image = self.master_animation_list[self.animate][self.frame]

        self.width = self.image.get_width()
        
        self.height = self.image.get_height()
        
        self.rect = self.image.get_rect()
        
        #character's position
        self.rect.x = x
        
        self.rect.y = y
        
        #character's mask
        self.mask = pygame.mask.from_surface(self.image)

    #move the player left
    def move_left(self, world, WIDTH, HEIGHT):
        
        self.dx = 0
        self.dx -= 5
        self.flip = True

        self.check_collisions(world, WIDTH, HEIGHT)

        self.rect.x += self.dx

    #move the player right
    def move_right(self, world, WIDTH, HEIGHT):
    
        self.dx = 0
        self.dx += 5
        self.flip = False

        self.check_collisions(world, WIDTH, HEIGHT)

        self.rect.x += self.dx

    #make the player jump
    def jumping(self, world, WIDTH, HEIGHT):

        self.dy = 0

        #check to see if they have jump. If no, then jump
        if self.jump:
            
            #Charge the jump. Decide how high the player will jump
            if self.time_down <= 2200:

                self.vel_y = -self.JUMP_HEIGHT * 2.2

            elif self.time_down > 2200 and self.time_down < 4000:

                self.vel_y = -self.JUMP_HEIGHT * (self.time_down/1000)

            elif self.time_down >= 4000:

                self.time_down = 5000

                self.vel_y = -self.JUMP_HEIGHT * (self.time_down/1000)

            self.time_down = 0
            
            self.jump_count += 1
            
            self.jump = False

        #add gravity
        self.vel_y += 1
        
        if self.vel_y > 1:
            
            #Falling animations
            self.update_animations(self.animations_types.index("Falling"))
            
            self.vel_y += 1
        
        self.dy += self.vel_y
        
        self.check_collisions(world, WIDTH, HEIGHT)

        self.rect.y += self.dy
        
  
    #checking for collisions
    def check_collisions(self, world, WIDTH, HEIGHT):

        #check collisions b/w the player and object within the map
        for tile in world.tile_list:

            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):

                #if the player is falling. Player had jumped and landed on block
                if self.vel_y > 0:
                    self.in_air = False
                    self.dy = tile[1].top - self.rect.bottom
                    self.jump_count = 0
                    self.vel_y = 0

                #if player is jumping. Player has hit their head
                elif self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0

            #if player has ran into something
            elif tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0

        #player has fallen into lava
        if pygame.sprite.spritecollide(self, world.lava_group, False):
            self.death = True

        #player has reach the portal to enter the next level
        elif pygame.sprite.spritecollide(self, world.exit_group, False):
            self.level_complete = True
            self.level += 1
            if self.level > 2:
                self.level = 1
        
        #player has reached a checkpoint. Record the checkpoint coordinate and delete the sprite
        elif pygame.sprite.spritecollide(self, world.flag_group, True):
            if not self.flip:
                self.last_x = self.rect.x + 40
            elif self.flip:
                self.last_x = self.rect.x - 40
            self.last_y = self.rect.y

        #make the player not go below the screen
        elif self.rect.bottom + self.dy > HEIGHT:
            self.in_air = False
            self.jump_count = 0
            self.dy = 0
            self.vel_y = 0
            self.dy =  HEIGHT - self.rect.bottom

        #prevent player from going off screen
        elif self.rect.right + self.dx > WIDTH:
            self.dx =  WIDTH - self.rect.right

        elif self.rect.left + self.dx < 0:
            self.dx = 0 

    #animate the character
    def update_animations(self, action):

        COOLDOWN = 110

        #new action. reset frame
        if self.animate != action:
            self.frame = 0
            self.animate = action
            self.last_update = pygame.time.get_ticks()
            self.animation_complete = False
        
        #cycle through the frame/sprite
        if pygame.time.get_ticks() - self.last_update >= COOLDOWN:
            self.frame += 1
            self.last_update = pygame.time.get_ticks()

            if self.frame >= len(self.master_animation_list[self.animate]):
                self.frame = 0
                #check to see if the animation has run once
                self.animation_complete = True
        
        self.image = self.master_animation_list[self.animate][self.frame]

    #the player is dead
    def check_death(self):
        
        if self.death:

            self.update_animations(self.animations_types.index("Death"))

            #must complete the death animation before continuing
            if self.animation_complete:

                self.rect.x = self.last_x

                self.rect.y = self.last_y

                self.vel_y = 0

                self.flip = False
                
                self.death = False

    #draw the character on-screen
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)