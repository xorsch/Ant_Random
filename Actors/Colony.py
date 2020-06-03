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


    def step(self, enabled, terrain ):
        """description of class"""

        for n in range ( len( self.__ants )):
            self.__ants[n].step( enabled, terrain )


    def __plot_nest( self, screen ):

        color  = 64, 242, 64
    
        w, h = int( screen.get_width()/self.__cols), int( screen.get_height()/self.__rows )
        
        pygame.draw.rect( screen,  color, ( self.__nestx * w, self.__nesty * h, w, h ) )


    def plot_colony( self, show_footprint, screen ):
        """description of class"""

        self.__plot_nest( screen )

        for n in range ( len( self.__ants )):
            self.__ants[n].plot_ant( show_footprint, screen )

#EOF
