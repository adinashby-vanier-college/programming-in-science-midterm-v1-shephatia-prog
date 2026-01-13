import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area_of_circle = math.pi * radius ** 2

    return round(area_of_circle, 2)

print(area_of_circle(5))
    


# Q2: Hollow Right Triangle

def hollow_right_triangle(n):

    if n < 4:
        return "The triangle height should be at least 4."
    
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
    



# Q3: Inverted Pyramid
def inverted_pyramid(n):

    if n < 3:
        return "The pyramid height should be at least 3."
    
    result = ""

    for i in range(n, 0, -1):

        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        result += spaces + stars + "\n"

    return result

print(inverted_pyramid(5))
        

# ----------------------------------------------------------------
print(area_of_circle(5))
print()


print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
  
