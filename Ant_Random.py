import pygame

from Actors.Terrain import Terrain
from Actors.Ant import Ant
from Actors.Food import Food 

                        
        
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
    ant  = Ant( ( cols, rows ) )    
    ant2 = Ant( ( cols, rows ) ) 
    food = Food( ( cols, rows ) )

    pygame.init()
    screen = pygame.display.set_mode( (width, height) )
    clock  = pygame.time.Clock()

 
    terrain.create_terrain( (2,2), 5, 343 )
    ant.set_position(  int(cols/4), int(rows/4) )
    ant.set_nest( ant.get_position() )
    ant2.set_position(  int(cols/4)-3, int(rows/4)-3 )
    ant2.set_nest( ant.get_position() )
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

        ant.step( not game_pause, terrain )
        if( is_ant_found_food( ant.get_position(), food.get_position() ) ):
            ant.get_food();

        ant2.step( not game_pause, terrain )
        if( is_ant_found_food( ant2.get_position(), food.get_position() ) ):
            ant2.get_food();            
        
        ## Show game

        terrain.plot_terrain( show_board, screen )
        terrain.plot_grid( show_grid, screen )
        food.plot_food( screen )       
        
        ant.plot_ant( show_footprint, screen )
        ant2.plot_ant( show_footprint, screen )
        ant.plot_nest( screen )
        ant2.plot_nest( screen )
        
        pygame.display.update()

pygame.quit()

