'''
Write a function called calculate_area that takes base and height as an input and
returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height
'''

# def calculate_area(base, height):
#     area = (1/2)*base*height
#     return area

# base = float(input('Enter base : '))
# height = float(input('Enter height : '))
# area_triangle =  calculate_area(base, height)
# print(f'Area of triangle {area_triangle}')

'''Modify above function to take third parameter shape type. 
It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape'''

def calculate_area(x, y, shapeType=''):
    if(shapeType == 'rectangle'):
        area = x*y
        return area
    elif(shapeType == '' or shapeType == 'triangle'):
        area = (1/2)*x*y
        return area

area = calculate_area(2,2,'triangle')
print(area)


    
        


