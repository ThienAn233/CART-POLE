from vpython import *
from utils import *
import time as t
import numpy as  np

### ADJUST CANVAS ###
scene.background    = color.white
scene.range         = 0.6
scene.align         = 'right'
### CONSTANT ###
r           = 30    # step/s 
cart_mass   = 3     # kg
pole_mass   = 0.1   # kg
lin_fric    = 0.1
rev_fric    = 0.0001
window      = 3

### OBJECT ###
CART = CART_OBJECT(lin_fric,box(pos=vec(0, 0, 0), length=0.06, height=0.02, width=0.04, color=color.blue),pole_mass)
CART.set_mass(cart_mass)
POLE = POLE_OBJECT(rev_fric,box(length=0.1, height=0.01, width=0.01,color=color.black),CART)
POLE.set_mass(pole_mass)
POLE.update_pos()
POLE.set_angle(-pi/2)

### PLOTTING ###
g1 = graph(title='CART_Velocity', xtitle='t', ytitle='m/s', align='right',xmax=window,xmin=0,scroll=True)
cur1 = gcurve(graph=g1)
g2 = graph(title='POLE_Acceleration', xtitle='t', ytitle='rad/s^2', align='right',xmax=window,xmin=0,scroll=True)
cur2 = gcurve(graph=g2)
g3 = graph(title='POLE_Velocity', xtitle='t', ytitle='rad/s', align='right',xmax=window,xmin=0,scroll=True)
cur3 = gcurve(graph=g3)

### SIMULATION ###
t = 0
F = 10
while True:
    rate(r)
    my_keys = keysdown()
    if 'a' in my_keys:
        CART.set_force(-F)
    elif 'd' in my_keys:
        CART.set_force(F)
    else:
        CART.set_force(0)
    CART.update_pos(1/r)
    POLE.update_pos()
    POLE.update_angle(1/r)
    cur1.plot(t,CART.velocity.x)
    cur2.plot(t,POLE.angular_acceleration)
    cur3.plot(t,POLE.angular_velocity)
    t += 1/r
    # print(t,CART.force,CART.acceleration.x,CART.velocity.x,CART.position.x)
    # print(t,POLE.angular_acceleration,POLE.angular_velocity,POLE.angle)