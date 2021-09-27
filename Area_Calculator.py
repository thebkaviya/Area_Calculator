global length
global width
global area
global shape
global x 

####Area of rectangle####   
def rectangle ():
    unit = str(input("Enter unit "))
    length = float(input("Enter length = "))
    width = float(input("Enter width = "))
    print ("Area = Length X Width")
    area = float(length*width)
    print ("Area = ", area, unit)
    
####Area of square####
def square():
    unit = str(input("Enter unit "))
    length = float(input("Enter length = "))
    width = float(input("Enter width = "))
    print ("Area = Length X Width or Area = Length/Width ** 2")
    area = float(length*width)
    print ("Area = ", area, unit)

####Area of triangle####
def triangle():
    unit = str(input("Enter unit "))
    height = float(input("Enter height = "))
    base = float(input("Enter base = "))
    print ("Area = (Height X Base) / 2")
    area = float((height*base)/2)
    print ("Area = ", area, unit)

####Area of parallelogram####
def parallelogram ():
    unit = str(input("Enter unit "))
    height = float(input("Enter height = "))
    base = float(input("Enter base = "))
    print ("Area = Height X Base")
    area = float(height*base)
    print ("Area = ", area, unit)
    
####Area of circle####
def circle():
    unit = str(input("Enter unit "))
    radius = float(input("Enter radius = "))
    print ("Area = Pi X (Radius**2) ")
    area = float((22*(radius**2))/7)
    print ("Area = ", area, unit)

####Area of trapezium####
def trapezium():
    unit = str(input("Enter unit "))
    height = float(input("Enter height = "))
    length1 = float(input("Enter length 1 = "))
    length2 = float(input("Enter length 2 = "))
    print ("Area = (Height X (Length 1 + Length 2)) / 2")
    area = float((height*(length1+length2)/2))
    print ("Area = ", area, unit)



def main_function():
    print('''

+--------------------------------------------------+
| Please enter valid inputs for the program.       |
| If not, rubbish data in, rubbish results out.... |
+--------------------------------------------------+

''')
    while True:#keeps the program running
        print ('''

            +-----------------------+
            |  Rectangle = R        |
            |  Square = s           |
            |  Triangle = T         |
            |  Parallelogram = P    |
            |  Trapezium = TR       |
            |  Circle = C           |
            +-----------------------+

            ''')#list of shapes
        shape = str(input("Enter the letter of the shape you need... "))
        shape = shape.upper()#converts to uppercase
        print("You entered", shape)#To remind
        if shape == str("R"):
            rectangle()
        elif shape == str("S"):
            square()       
        elif shape == str("T"):
            triangle()
        elif shape == str("P"):
            parallelogram ()
        elif shape == str("TR"):
            trapezium()
        elif shape == str("C"):
            circle()
        x = input("Exit ?....(y/n)... ")#to quit the program
        if x == "y":
            break

main_function()
