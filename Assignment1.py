#Assignment_1: MATHEMATICAL OPERATION:

v1= float(input("Enter first number: "))
v2= float(input("Enter second number: "))

add= v1+v2
minus= v1-v2
multiple= v1*v2
if v2!=0: divide= v1/v2
else: divide= "undefined(Division by zero not allowed)"

print('Addition: ', add)
print('Substraction: ', minus)
print('Multiplication: ',multiple)
print('Divison: ',divide)
