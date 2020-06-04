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
        """
        set ant col, row """

        self.__cols = col
        self.__rows = row



    def set_position( self, posx, posy ):
        """
        Set ant position"""

        self.__antx = posx
        self.__anty = posy


    def get_food( self ):
        """description of class"""

        if( self.__food < 2 ):
            self.__food += 1

    def free_food(self):
        """description of class"""

        self.__food = 0

    
    def is_get_food(self):
        """description of class"""

        if (self.__food>0):
            return True

        return False
    

    def get_position( self ):
        """Return ant position as vector"""

        return self.__antx, self.__anty
    

    def plot_ant( self, show_footprint, pause, screen ):
        """Return ant position as vector"""

        red   =  64, 64, 64
        blue  =  16, 16, 242
        
        w, h = int( screen.get_width()/self.__cols), int( screen.get_height()/self.__rows )

        if( self.__food == 0):
            color = red
        else:
            color = blue                    
        
        if ( show_footprint == True ):
            self.footprint.plot_board( True, pause, screen, self.__food )

        pygame.draw.rect( screen, color, ( self.__antx * w, self.__anty * h, w, h ) )
        

    def __calculate_new_direction( self, terrain ):
        direction = numpy.random.randint(0,8)    
        
        sum_left   = self.footprint.get_footprint( self.__antx-1, self.__anty  )+self.footprint.get_footprint( self.__antx-2, self.__anty  )
        sum_right  = self.footprint.get_footprint( self.__antx+1, self.__anty  )+self.footprint.get_footprint( self.__antx+2, self.__anty  )
        sum_top    = self.footprint.get_footprint( self.__antx, self.__anty-1  )+self.footprint.get_footprint( self.__antx, self.__anty-2  )        
        sum_bottom = self.footprint.get_footprint( self.__antx, self.__anty+1  )+self.footprint.get_footprint( self.__antx, self.__anty+2  )        

        sum_top_left  = self.footprint.get_footprint( self.__antx-1, self.__anty-1)+self.footprint.get_footprint( self.__antx-2, self.__anty-2  )
        sum_top_right = self.footprint.get_footprint( self.__antx+1, self.__anty-1)+self.footprint.get_footprint( self.__antx+2, self.__anty-2  )
        sum_bot_left  = self.footprint.get_footprint( self.__antx-1, self.__anty+1)+self.footprint.get_footprint( self.__antx-2, self.__anty+2  )        
        sum_bot_right = self.footprint.get_footprint( self.__antx+1, self.__anty+1)+self.footprint.get_footprint( self.__antx+2, self.__anty+2  )  

        # move = ( (-1, 0), ( 0,-1 ), ( 1, 0), ( 0, 1),
        #          (-1,-1), ( 1,-1 ), (-1, 1), ( 1, 1) )
        
        self.__cost = []
        self.__cost.append( sum_left )    
        self.__cost.append( sum_top )
        self.__cost.append( sum_right )  
        self.__cost.append( sum_bottom )        
        self.__cost.append( sum_top_left )    
        self.__cost.append( sum_top_right )
        self.__cost.append( sum_bot_left )  
        self.__cost.append( sum_bot_right )   
        
        direction = numpy.argmin( self.__cost )

        return direction



    def step( self, enabled, terrain ):
        """Fa avançar el conjunt de la colonia un pas en la seva evolució"""
        
        
        if (not enabled):
            return

        possible = False

        move = ( (-1, 0), ( 0,-1 ), ( 1, 0), ( 0, 1),
                 (-1,-1), ( 1,-1 ), (-1, 1), ( 1, 1) )
        
        dir_random = True
        while( not possible ):
            
            direction = numpy.random.randint( 0, 4 )

            if( self.__antx > 2 and self.__antx < ( self.__rows - 3) and \
                self.__antx > 2 and self.__antx < ( self.__rows - 1) ):
                direction = self.__calculate_new_direction( terrain )
                dir_random = False
  
            newx = self.__antx + move[direction][0] #* numpy.random.randint(1,4)
            newy = self.__anty + move[direction][1] #* numpy.random.randint(1,4)          

            if( terrain.get_terrain( newx, newy ) > 0 ):
                possible = not possible  
        
        if( terrain.get_terrain( newx, newy ) < 1 ):
            return 
        
        print("Direccion random", dir_random )


        if( newx > -1 and newx < self.__cols and \
            newy > -1 and newy < self.__rows ):

            self.__antx = newx
            self.__anty = newy

            self.footprint.set_footprint( (self.__antx, self.__anty) )

#EOF