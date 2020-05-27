height =int(input('Enter height of triangle'))
base= int(input('Enter base'))
hypotenuse = (height**2+base**2)**(1/2)
area = 0.5*base*height
perimeter= height+base+hypotenuse
print("Area : ",area)
print("Perimeter :",perimeter) 