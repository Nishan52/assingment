#to find area using a function
def cirarea(r=0):
    pi=3.14
    area=pi*r*r
    return area
radius=int(input("Enter the value of the radius"))
result=cirarea(radius)
print("THe area of the circle is",result)