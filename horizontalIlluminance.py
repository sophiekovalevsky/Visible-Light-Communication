#!/usr/bin/env python
 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# This code plot the horizontal illuminance inside a room using a SISO array.

# Semi-angle at half illuminance (degree)
tethaHalf = 70

# Lambertian emission order (adimensional)
m = -np.log(2)/np.log10(np.cos(np.deg2rad(tethaHalf)))

# Center luminous intensity (cd)
I0 = 0.73

# Room's dimensions
dimZ = 3
dimX = 5
dimY = dimX

# LED's position (m)
xt = dimX*0.5
yt = dimY*0.5

# Grid number in the receiver plane
ngx = dimX*10
ngy = dimY*10

# Generate the grid vectors
x = np.linspace(0,dimX,ngx)
y = np.linspace(0,dimY,ngy)

# Distance between the transmitter and receiver plane (m)
ht = 3
hr = 0.85
htr = ht - hr

# Numbers of LEDs per array
nLed = 60

# Generate the receiver plane based on grid vectors
[xr, yr] = np.meshgrid(x,y)

# Create a zero matrix to store values of horizontal iluminance
E = np.zeros((ngx,ngy))

# Distance vector from source to receiver plane
d = np.sqrt(np.square(xr-xt) + np.square(yr-yt) + np.square(htr))

# Cos(tetha)
cosTetha = htr/d

# Get individual horizontal illuminace per LED
E = (I0*(cosTetha)**(m+1) )/np.square(d) 

# Get the horizontal illuminance per LED array
E = E*nLed*nLed

fig = plt.figure()
figE = fig.add_subplot(111, projection='3d')
figE.plot_surface(x,y,E)
figE.set_xlabel('X (m)')
figE.set_ylabel('Y (m)')
figE.set_zlabel('Horizontal Illuminance (lx)')

plt.show()