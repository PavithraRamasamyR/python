a=float(input("Enter the value of one side a:"))
b=float(input("Enter the value of second side b:"))
c=float(input("Enter the value of third side c:"))
s=(a+b+c)/2
print("Area of semitriangle:",s)
area=s*((s-a)*(s-b)*(s-c))
print("Area of triangle with sides a,b,c,is:",area)

