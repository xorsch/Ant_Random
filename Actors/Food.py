import pygame, sys
import numpy


class Food():

    """description of class"""
    __food_color   = 64,  242, 242, 125
    __foodx, __foody = 0, 0        
    __cols,  __rows  = 0, 0
    color = (204,102,0,255)

    def __init__( self, size ):
        """description of class"""

        self.__cols = size[0]
        self.__rows = size[1]



    def set_position( self, posx, posy ):
        """description of class"""

        self.__foodx = posx
        self.__foody = posy



    def get_position( self ):
        """description of class"""
        try:
            return self.__foodx, self.__foody        
        except:
            return -1, -1
            
    

    def plot_food( self, screen ):
        """description of class"""     

        width_tile  = int( screen.get_width() /self.__cols ) 
        height_tile = int( screen.get_height()/self.__rows )

        food_rectangle = ( (self.__foodx) * width_tile, (self.__foody) * height_tile, width_tile, height_tile )

        pygame.draw.rect( screen, self.color , food_rectangle )

#EOF
