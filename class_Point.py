# -*- coding: utf-8 -*-
"""
This file will contain the "Point" Class
"""
import numpy as np

class Point():
    """
    This class will contain information about a point in space. It has the function of show(), move() and distance().
    """
    
    def __init__(self,x=0,y=0,z=0):
        "If no coordinates were input, initialise to origin."

        self.x0=x
        self.y0=y
        self.z0=z
        
    def show(self):
        "This function will return the coordinates of the point"
        
        print("Coordinates are: %s,%s,%s" % (self.x0,self.y0,self.z0))
        
    def move(self,x=0,y=0,z=0):
        "This function will move the point to the desired coordinates. If no values are added, the point will not move."

        self.x0+=x
        self.y0+=y
        self.z0+=z
        
    def dist(self,p):
        """This function will calculate the distance between this point and another point and print the result. 
        The value can also be saved into another variable outside of the class."""
        
        distx=abs(self.x0-p.x0)
        disty=abs(self.y0-p.y0)
        distz=abs(self.z0-p.z0)
        
        distance = np.sqrt(distx**2 + disty**2 + distz**2) 
        print("The distance between the two points is: %s" % distance)
        return distance
        
