import pygame
import numpy


class Footprint():
    """description of class"""    

   
    __footprint = []

   
    def __init__( self, size ):
        """description of class""" 
        
        self.__footprint = numpy.zeros( ( size[0], size[1] ) )


    def get_footprint( self, col, row ):
        """description of class""" 
        try:            
            return self.__footprint[ col ][ row ]           
        except:
            return -1

        
    def paint_box( self, position ):
        """description of class""" 
  
        self.__footprint[ position[0] ][ position[1] ] += 32


        
    def plot_board( self, enabled, screen, with_food ):
        """description of class""" 


        if ( not enabled ):
            return
        
        footprint_surface = pygame.Surface( (screen.get_width(), screen.get_height() ), pygame.SRCALPHA )

        cols = self.__footprint.shape[0]
        rows = self.__footprint.shape[1]
        width_tile  = int( screen.get_width() /cols ) 
        height_tile = int( screen.get_height()/rows )
                
        for col in range ( cols ):
            for j in range ( rows ):
                if( self.__footprint[col][j] > 1 ):
                    c = self.__footprint[col][j]
                    if c < 120:
                        c = 120
                    elif c>255:
                        c = 255

                    self.__footprint[col][j] -= .25

                    if(with_food==0):
                        pygame.draw.rect( footprint_surface,  ( 204,   0, 204, c-64 ), ( col*width_tile, j*height_tile, width_tile, height_tile ) )
                    else:
                        pygame.draw.rect( footprint_surface,  ( 102, 204, 204, c-64 ), ( col*width_tile, j*height_tile, width_tile, height_tile ) )


        screen.blit( footprint_surface, (0, 0) )
