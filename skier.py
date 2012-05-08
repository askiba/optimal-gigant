class Skier:
    '''
    Model of the skier
    '''
    def __init__(self, mi, alfa, k1, k2, m, x0, v0, ksi ):
        '''
        Model of the skier. Arguments that models the races:
        Arguments:
            mi      - coefficient of friction. May vary for ex. on different waxes used.
            alfa    - slope degree. It is here - as a racer property, we can imagine 
                        unprofessional parallel slalom with slightly different slope degree for racer
            k1      - factor for air friction force for small velocity
            k2      - factor for air friction force for higher velocity, dependent on
                        drag coefficient, density of the air, projected front area of the skier
            m       - mass
            x0      - initial position
            v0      - initial velocity
            ksi     - initial inverse of radius of the curve (1/r)
        '''
        self.mi, self.alfa, self.k1, self.k2, self.m, self.ksi = mi, alfa, k1, k2, m, ksi
        
        # values of position and velocity. Current values
        # are on the tail of the list
        self.positions = [x0]
        self.velocities = [v0]
        
        # function that control the movement - that is
        # control changing of the radius
        self.radius_processor = None
        
        # time in second of the finish. None if not finished yet
        self.result = None
    
    def update_position(self, x):
        self.positions.append(x)
        
    def update_velocity(self, v):
        self.velocities.append(v)
        # steat the racer's turn based on velocity update, it stearin function if provided 
        if self.radius_processor:
            self.ksi = self.radius_processor(self)  
             
    def position(self):
        '''
        returns current position of the skier
        '''
        return self.positions[-1]

    def velocity(self):
        '''
        returns current velocity of the skier
        '''
        return self.velocities[-1]        
    