def circel_area(r):
    area = 3.14 *r*r
    return area 

def triangle_area(base , heigth):
    area = (base * heigth) / 2
    return area

def rectangle_perimeter(length , width):
    p = 2 * (length + width)
    return p

def square_area(a):
    area = a * a 
    return area

r = int(input("enter number:"))
print(circel_area(r))

b = int(input("enter number:"))
h = int(input("enter number:"))
print(triangle_area(b , h))

l = int(input("enter number:"))
w = int(input("enter number:"))
print(rectangle_perimeter(l , w))

s = int(input("enter number:"))
print(square_area(s))

 