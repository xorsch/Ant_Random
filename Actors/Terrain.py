
import pygame, sys
import numpy

        
class Terrain():
    """description of class"""
    
    __terrain = []
    

    def __init__(self, size ):
        
        self.__cols = size[0]
        self.__rows = size[1]
        self.__terrain = numpy.zeros( ( size[0], size[1] ) )


    def get_terrain( self, col, row ):

        if( col > -1 and col < (self.__cols) and
            row > -1 and row < (self.__rows) ):
        
            return self.__terrain[ col ][ row ]
        
        else:
            return -1

    
    def __generate_perlin_noise_2d( self, res ):
        
        def f(t):
            return 6*t**5 - 15*t**4 + 10*t**3

        
        delta = ( res[0] / self.__cols, res[1] / self.__rows )
        d     = (self.__cols // res[0], self.__rows // res[1])
        grid  = numpy.mgrid[ 0:res[0]:delta[0], 0:res[1]:delta[1] ].transpose( 1, 2, 0 ) % 1


        # Gradients
        angles    = 2 * numpy.pi * numpy.random.rand( res[0]+1, res[1]+1 )
        gradients = numpy.dstack( ( numpy.cos(angles), numpy.sin(angles) ) )
        
        g00 = gradients[ 0:-1,0:-1 ].repeat( d[0], 0).repeat(d[1], 1 )
        g10 = gradients[ 1:  ,0:-1 ].repeat( d[0], 0).repeat(d[1], 1 )
        g01 = gradients[ 0:-1,1:   ].repeat( d[0], 0).repeat(d[1], 1 )
        g11 = gradients[ 1:  ,1:   ].repeat( d[0], 0).repeat(d[1], 1 )

        # Ramps
        n00 = numpy.sum( numpy.dstack( (grid[:,:,0]  , grid[:,:,1]  ) ) * g00, 2 )
        n10 = numpy.sum( numpy.dstack( (grid[:,:,0]-1, grid[:,:,1]  ) ) * g10, 2 )
        n01 = numpy.sum( numpy.dstack( (grid[:,:,0]  , grid[:,:,1]-1) ) * g01, 2 )
        n11 = numpy.sum( numpy.dstack( (grid[:,:,0]-1, grid[:,:,1]-1) ) * g11, 2 )

        # Interpolation
        t = f( grid )
        n0 = n00 * ( 1-t[:,:,0] ) + t[:,:,0] * n10
        n1 = n01 * ( 1-t[:,:,0] ) + t[:,:,0] * n11
        
        return numpy.sqrt(2)*( (1-t[:,:,1]) * n0 + t[:,:,1]*n1 )


    def create_terrain( self, complexity, levels, seed ):
        
        self.__levels = levels-1
        self.__complexity_x = complexity[0]
        self.__complexity_y = complexity[1]
        self.__random_seed = seed

        numpy.random.seed( self.__random_seed )
        
        self.__terrain = self.__generate_perlin_noise_2d( ( self.__complexity_x, self.__complexity_y ) )

        max_terrain = -1000
        min_terrain =  1000
        
        for nx in range ( self.__cols ):
            for ny in range ( self.__rows ):
            
                if ( max_terrain < self.__terrain[nx][ny] ):
                     max_terrain = self.__terrain[nx][ny]
                if ( min_terrain > self.__terrain[nx][ny] ):
                     min_terrain = self.__terrain[nx][ny]

        height_terrain = max_terrain - min_terrain
        steps = height_terrain / self.__levels;


        for nx in range ( self.__cols ):
            for ny in range ( self.__rows ):
                value = ( self.__terrain[nx][ny]-min_terrain )/(height_terrain)           
                self.__terrain[nx][ny] = int( value / steps )
        
    
    def plot_terrain(self, enabled, screen ):

        if ( not enabled ):
            return
        
        width_tile  = int( screen.get_width() /self.__cols ) 
        height_tile = int( screen.get_height()/self.__rows )

        for nCol in range ( self.__cols ):
            for nRow in range ( self.__rows ):
            
                rectangle = ( nCol * width_tile, nRow* height_tile, width_tile, height_tile )

                if  ( self.__terrain[ nCol, nRow ] == 0 ):
                    color =  ( 63,  61, 219)
                elif( self.__terrain[ nCol, nRow ] == 1 ):             
                    color =  (209, 199,  39)
                elif( self.__terrain[ nCol, nRow ] == 2 ):
                    color =  (230, 157,   0)
                elif( self.__terrain[ nCol, nRow ] == 3 ):            
                    color =  (219,  97,  21)

                pygame.draw.rect( screen, color, rectangle )


    def plot_grid( self, enabled, screen ):
        """description of class""" 

        if ( not enabled ):
            return
        
        black =  234, 234, 234
        w, h = int( screen.get_width()/self.__cols), int( screen.get_height()/self.__rows )
        
        for i in range ( self.__cols ):
            pygame.draw.line( screen, black, ( ( i + 1 ) * w, 0), ( (i+1) * w, screen.get_height() ), 1)
            
        for i in range ( self.__rows ):
            pygame.draw.line( screen, black, (0, ( i + 1) * h ), ( screen.get_width(), (i+1) * h ), 1 )


#EOF
