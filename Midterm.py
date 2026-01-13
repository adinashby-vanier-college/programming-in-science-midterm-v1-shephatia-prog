import math



# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area_of_circle = math.pi * radius ** 2

    return round(area_of_circle, 2)

print(area_of_circle(5))
    
    
print(round(area_of_circle,5))
# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    for i in range(1, n + 1):

        if i == 1:
            result += "*" + "\n"

        elif i == 2:
            result += "**" + "\n"

        elif i == n: 
            result += "*" * n + "\n"

        else: 
            result += "*" + " " * (i - 2) + "*" + "\n"

        return result 

        
    
print(hollow_right_triangle(5))
