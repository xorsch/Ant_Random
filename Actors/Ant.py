import pygame, sys
import numpy

from Actors.Footprint import Footprint 


class Ant():
    """description of class"""   
    
    __id = 0

    def __init__( self, size ):
        """description of class"""
        self.footprint = Footprint( size )

        self.__antx = 0
        self.__anty = 0        

        self.__food = 0

        self.__cols = size[0]
        self.__rows = size[1]
    

    
    def set_ant( self, col, row ):
        """description of class"""
        self.__cols = col
        self.__rows = row



    def set_position( self, posx, posy ):
        """description of class"""

        self.__antx = posx
        self.__anty = posy


    def get_food( self ):
        
        if( self.__food < 10):
            self.__food += 1


    def is_get_food(self):
        if (self.__food==1):
            return True

        return False
    

    def get_position( self ):
        
        return self.__antx, self.__anty
    

    def plot_ant( self, show_footprint, screen ):
        
        red   =  64, 64, 64
        blue  =  16, 16, 242
        
        w, h = int( screen.get_width()/self.__cols), int( screen.get_height()/self.__rows )

        if( self.__food == 0):
            color = red
        else:
            color = blue                    
        
        if ( show_footprint == True ):
            self.footprint.plot_board( True, screen, self.__food )

        pygame.draw.rect( screen, color, ( self.__antx * w, self.__anty * h, w, h ) )
        

        
    def step( self, enabled, terrain ):

        possible = False
        
        if (not enabled):
            return
        
        move = ( (0, -1), (1, 0), (0, 1), (-1, 0),
                 (1, -1), (1, 1), (-1, 1), (-1, -1))
        
        while( not possible ):
        
            direction = numpy.random.randint(0,8)
        
            newx = self.__antx + move[direction][0] #* numpy.random.randint(1,4)
            newy = self.__anty + move[direction][1] #* numpy.random.randint(1,4)
            
            if( self.__food == 1 and 
                self.__antx == self.__nestx and \
                self.__anty == self.__nesty ):

                self.__food = 0
                print("Food in nest")

            if( terrain.get_terrain( newx, newy ) > 0 ):
                possible = not possible  
                

        if( newx > -1 and newx < self.__cols and \
            newy > -1 and newy < self.__rows ):

            self.__antx = newx
            self.__anty = newy

            self.footprint.paint_box( (self.__antx, self.__anty) )

#EOF