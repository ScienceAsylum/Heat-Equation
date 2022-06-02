#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** May 2022 **********************************
#*******************************************************************************
from vpython import *
import numpy as np

#---------------------- Canvas ----------------------
scene = canvas()
scene.height = 1080
scene.width = 1920
scene.fov = pi/6
scene.userspin = 0
scene.userzoom = 0

#---------------------- Changeable Info -------------------------
Max_Temp_Dev = 5 #kelvin
Rod_L = 20 #meters
Rod_D = 1 #meters
Num_of_Points = 500

def Solution(L,A,x,t): #Fourier Series for Two Uniform Rods
    T = 0
    Num_of_Terms = 200
    for n in arange( 1 , Num_of_Terms , 2 ):
        T += A * 4/(n*pi) * sin( n*pi * (x+L/2)/L ) * exp( -(n*pi/L)**2 * t )
    return T

#---------------------- 3D Objects -------------------------
scene.range = 0.5 * Rod_L
scene.center = vector( 0.5 * Rod_L , 0 , 0 )

#X-Axis
arrow( pos = vector( -0.25 * Rod_L , 0 , 0 ) ,
       axis = vector( 1.5 * Rod_L , 0 , 0 ) ,
       shaftwidth = 0.2 , headwidth = 0.4 , headlength = 0.6 )

#Y-Axis
arrow( pos = vector( 0 , -1.5 * Max_Temp_Dev , 0 ) ,
       axis = vector( 0 , 3 * Max_Temp_Dev , 0 ) ,
       shaftwidth = 0.2 , headwidth = 0.4 , headlength = 0.6 )

#Metal Rod
Rod = curve( color = vector(0.5,0.5,0.5) , radius = Rod_D/2 )
RodPoints = np.linspace( 0 , Rod_L , Num_of_Points )

def Point_Color(T,Tmax):
    if T >= 0:
        C = vector(0.5,0.5,0.5) + T/(2*Tmax) * vector(1,-1,-1)
    else:
        C = vector(0.5,0.5,0.5) + T/(2*Tmax) * vector(1,1,-1)
    return C

for x in RodPoints:
    Temperature = Solution( Rod_L , Max_Temp_Dev , x , 0 )
    Rod.append( dict( pos = vector(x,0,0) ,
                      color = Point_Color( Temperature , Max_Temp_Dev ) ) )

#Temperature Curve
TempCurve = curve( radius = Rod_D/20 )
for x in RodPoints:
    Temperature = Solution( Rod_L , Max_Temp_Dev , x , 0 )
    TempCurve.append( pos = vector( x , Temperature , 0 ) )

#---------------------- Animation -------------------------
scene.waitfor('click')
dt = 0.0001
t = 0
while 1:
    rate(500)
    #scene.capture("HeatEqu.png")
    for N in arange( 0 , Num_of_Points , 1 ):
        x = TempCurve.point(N)['pos'].x
        Temperature = Solution( Rod_L , Max_Temp_Dev , x , t )
        Rod.modify( int(N) ,
                    color = Point_Color( Temperature , Max_Temp_Dev ) )
        TempCurve.modify( int(N) ,
                          pos = vector( x , Temperature , 0 ) )
        t += dt
