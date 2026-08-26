
#Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

"""
 euclidean distance formula = sqrt((x2-x1)**2 + (y2-y1)**2)
"""
#solution----
   #METHOD 1
print("Enter the cordinates for point1")
x1=float(input("x1"))
y1=float(input("y1"))
print("Enter the cordinates for point2")
x2=float(input("x2"))
y2=float(input("y2"))

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(distance)

    #METHOD 2 
import math
print("Enter the cordinates for point1")
x1=float(input("x1"))
y1=float(input("y1"))
print("Enter the cordinates for point2")
x2=float(input("x2"))
y2=float(input("y2"))

point1 = (x1,y1)
point2 = (x2,y2)
distance = math.dist(point1,point2)
print(distance)
