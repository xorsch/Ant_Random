import pygame, sys
import numpy


class Food():

    """description of class"""
    __food_color   = 64,  242, 242, 125
    color = (204,102,0,255)
    __foodx, __foody = 0, 0        
    __cols,  __rows  = 0, 0
    __quantity = 0


    def __init__( self, size ):
        """description of class"""
        self.__quantity = 5
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
            

    def add_food(self):
        self.__quantity += 5


    def pick_food( self ):
        """description of class"""

        if(self.__quantity > 1):          
            self.__quantity -= 1
            print( self.__quantity )


    def count_food(self):
        return self.__quantity


    def plot_food( self, screen ):
        """description of class"""     

        if ( self.__quantity > 1 ):
            
            width_tile  = int( screen.get_width() /self.__cols ) 
            height_tile = int( screen.get_height()/self.__rows )

            food_rectangle = ( (self.__foodx) * width_tile, (self.__foody) * height_tile, width_tile, height_tile )

            pygame.draw.rect( screen, self.color , food_rectangle )

#EOF
