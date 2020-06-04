import pygame
import numpy

from Actors.Terrain import Terrain
from Actors.Food import Food 
from Actors.Colony import Colony


# Return true if ant and food at an the same position        
def is_ant_found_food( ant, food ):

    if( ant[0] == food[0] \
        and ant[1]==food[1]):

        return True

    return False


# Main

width, height = 800, 600
cols, rows = 40, 30


show_grid = False
show_board = True
show_footprint = True
game_pause = False
done = False
fullscreen = False
modify = False

frame_rate = 25


    
if __name__ == "__main__":

    terrain = Terrain( (cols, rows) )
    colony  = Colony( (cols, rows) )
    food    = Food( ( cols, rows ) )

    pygame.init()
    screen = pygame.display.set_mode( (width, height) )
    clock  = pygame.time.Clock()

 
    terrain.create_terrain( (2,2), 5, 1242 ) # 343 )
    colony.set_colony( (8,6), 1 )
    food.set_position( 24, 20 )


    while not done:
                
        clock.tick( frame_rate )

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True

            mouseClick = pygame.mouse.get_pressed()
        
            if pygame.mouse.get_pressed()[2] and  modify == True :
                posX, posY = pygame.mouse.get_pos()
                dimCW = int(height/rows)
                dimCH = int(width/cols)
                celX, celY = int ( numpy.floor( posX / dimCW ) ), int( numpy.floor( posY / dimCH ) )
                
                food.set_position( celX, celY )
                food.add_food()
                modify = False

            if pygame.mouse.get_pressed()[0] and  modify == True :

                posX, posY = pygame.mouse.get_pos()
                dimCW, dimCH = int( height/rows ), int( width/cols )
                celX, celY = int( numpy.floor( posX / dimCW ) ), int( numpy.floor( posY / dimCH ) )
                
                colony.set_nest( (celX, celY) )
                modify = False


            keys = pygame.key.get_pressed()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q or \
               event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                done = True
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b :
                show_board = not show_board

            if event.type == pygame.KEYDOWN and event.key == pygame.K_g :
                show_grid = not show_grid

            if event.type == pygame.KEYDOWN and event.key == pygame.K_p :
                show_footprint = not show_footprint
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_PAUSE or\
               event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_pause = not game_pause

            if event.type == pygame.KEYDOWN and event.key == pygame.K_a :
                colony.add_ant()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_z :
                colony.delete_ant()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
               modify = True


        ## Move Ant and Check if it founded food, also remeber his footprints

        colony.step( not game_pause, terrain )

        ## Check if any ant has found food
        for n in range ( colony.count_ants() ):

            if( is_ant_found_food( colony.get_ant(n).get_position(), food.get_position() ) ):
                colony.ant_get_food( n, food )
        
        ## Show game

        screen.fill( (0,0,0) )

        terrain.plot_terrain( show_board, screen )
        terrain.plot_grid( show_grid, screen )
        food.plot_food( screen )       
        colony.plot_colony( show_footprint, game_pause, screen )

        
        pygame.display.update()

pygame.quit()

