import pygame
from Actors.Ant import Ant


class Colony():
    """description of class"""

    __ants = []


    def __init__( self, size ):
        """description of class"""
        self.__nestx = 0
        self.__nesty = 0
        self.__cols = size[0]
        self.__rows = size[1]


    def set_colony( self, site, n_ants ):
        """description of class"""

        self.__nestx = site[0]
        self.__nesty = site[1]
        
        for n in range (n_ants):
            new_ant = Ant( (self.__cols, self.__rows) )
            new_ant.set_position( self.__nestx, self.__nesty )
            self.__ants.append( new_ant )


    def add_ant(self):
        """description of class"""

        new_ant = Ant( (self.__cols, self.__rows) )
        new_ant.set_position( self.__nestx, self.__nesty )
        self.__ants.append( new_ant )


    def get_ant(self, ant_id):
        """description of class"""

        return self.__ants[ ant_id ]


    def ant_get_food(self, ant_id, food ):
        """description of class"""

        if ( food.count_food() > 1 ):
            food.pick_food()
            self.__ants[ant_id].get_food()


    def delete_ant(self):
        """description of class"""

        if( len(self.__ants)>0 ):
            self.__ants.pop(0)


    def count_ants(self):
        """returns number of ants in the colony"""
        
        return ( len( self.__ants ) )


    def step( self, enabled, terrain ):
        """description of class"""

        for n in range ( len( self.__ants )):
            self.__ants[n].step( enabled, terrain )
            position = self.__ants[n].get_position()
            if( position[0] == self.__nestx and \
                position[1] == self.__nesty ):
                if( self.__ants[n].is_get_food() ):
                    self.__ants[n].free_food()


    def __plot_nest( self, screen ):
        """Plot nest colony in screen"""

        color  = 64, 242, 64
    
        w, h = int( screen.get_width()/self.__cols), int( screen.get_height()/self.__rows )
        
        pygame.draw.rect( screen,  color, ( self.__nestx * w, self.__nesty * h, w, h ) )


    def plot_colony( self, show_footprint, screen ):
        """description of class"""

        self.__plot_nest( screen )

        for n in range ( len( self.__ants )):
            self.__ants[n].plot_ant( show_footprint, screen )

#EOF
