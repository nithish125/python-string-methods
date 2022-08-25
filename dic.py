from turtle import left, right


a= int( input("a :"))
b= int( input("b :"))
left1=(a+b)**2
right1=((a**2)+(b**2)+(2*a*b))
print(left1)
print(right1)
if(right1==left1):
  print("true")
