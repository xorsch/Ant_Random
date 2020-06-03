import pygame

from Actors.Terrain import Terrain
from Actors.Food import Food 
from Actors.Colony import Colony

                        
        
def is_ant_found_food( ant, food ):

    if( ant[0] == food[0] and ant[1]==food[1]):
        print("found food")
        return True

    return False


# Main


width, height = 960, 720
cols, rows = 32, 24


show_grid = False
show_board = True
show_footprint = True
game_pause = False
done = False

frame_rate = 15


    
if __name__ == "__main__":

    terrain = Terrain( (cols, rows) )
    colony  = Colony( (cols, rows) )
    food = Food( ( cols, rows ) )

    pygame.init()
    screen = pygame.display.set_mode( (width, height) )
    clock  = pygame.time.Clock()

 
    terrain.create_terrain( (2,2), 5, 343 )
    colony.set_colony( (8,6), 4 )
    food.set_position( 30, 22 )    


    while not done:
                
        clock.tick( frame_rate )

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True


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


        ## Move Ant and Check if it founded food, also remeber his footprints

        colony.step( not game_pause, terrain )

        
        #if( is_ant_found_food( ant.get_position(), food.get_position() ) ):
        #    ant.get_food();
        
        #if( is_ant_found_food( ant2.get_position(), food.get_position() ) ):
        #    ant2.get_food();            
        
        ## Show game

        screen.fill( (0,0,0) )

        terrain.plot_terrain( show_board, screen )
        terrain.plot_grid( show_grid, screen )
        food.plot_food( screen )       
        colony.plot_colony( show_footprint, screen )

        
        pygame.display.update()

pygame.quit()

