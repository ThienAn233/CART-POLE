from vpython import vec
import numpy as np

class CART_OBJECT():
    def __init__(self,friction,vpython_obj,pole_mass):
        self.friction       = friction
        self.vpython_obj    = vpython_obj
        self.pole_mass      = pole_mass
        self.mass           = 1
        self.force      = 0
        self.acceleration   = vec(0, 0, 0)
        self.velocity       = vec(0, 0, 0)
        self.position       = vpython_obj.pos
    
    def set_mass(self,mass):
        self.mass = mass
    
    def set_force(self,force):
        self.force = force
    
    def set_acceleration(self,acceleration):
        self.acceleration = acceleration
    
    def set_velocity(self,velocity):
        self.velocity = velocity
    
    def set_position(self,position):
        self.position           = position
        self.vpython_obj.pos    = self.position
        
    def update_pos(self,dt):
        self.acceleration = vec((self.force)/(self.mass+self.pole_mass)-np.sign(self.velocity.x)*self.friction,0,0)
        self.velocity           = self.velocity + self.acceleration*dt
        self.position           = self.position + self.velocity*dt
        self.vpython_obj.pos    = self.position
        
class POLE_OBJECT():
    def __init__(self,friction,vpython_obj,cart_obj):
        self.friction               = friction
        self.vpython_obj            = vpython_obj
        self.cart_obj               = cart_obj
        self.mass                   = 1
        self.angular_acceleration   = 0
        self.angular_velocity       = 0
        self.angle                  = 0
        self.position               = vpython_obj.pos
    
    def set_mass(self,mass):
        self.mass = mass
    
    def set_angular_acceleration(self,acceleration):
        self.angular_acceleration = acceleration
    
    def set_angular_velocity(self,velocity):
        self.angular_velocity = velocity
    
    def set_angle(self,angle):
        self.angle = angle
        self.vpython_obj.rotate(angle=self.angle,axis=vec(0,0,1),origin=self.cart_obj.position)
        
    def update_pos(self):
        self.vpython_obj.pos = self.cart_obj.position + vec(self.vpython_obj.length*np.cos(self.angle)/2,self.vpython_obj.length*np.sin(self.angle)/2,0)
    
    def update_angle(self,dt):
        self.angular_acceleration   = 1.5*(+self.cart_obj.acceleration.x*np.sin(self.angle)-9.8*np.cos(self.angle)-2*self.friction*self.angular_velocity/(self.mass*self.vpython_obj.length))/(self.vpython_obj.length)
        self.angular_velocity       = self.angular_velocity + self.angular_acceleration*dt
        self.vpython_obj.rotate(angle=self.angular_velocity*dt,axis=vec(0,0,1),origin=self.cart_obj.position)
        self.angle                  = self.angle + self.angular_velocity*dt