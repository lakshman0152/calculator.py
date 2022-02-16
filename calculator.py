print("CALCULATOR \n\n")

print("CHOOSE UR OPERATION \n")

operator = ((input(" ADD , SUB , MULTIPLY , DIVISION ---> ")))
num_1 = float(input("enter your first number : "))
num_2 = float(input("enter your second number : "))

if operator == 'add':
    print( num_1 ," + ", num_2 ," = ", num_1+num_2 )

elif operator == 'sub':
    print( num_1 ," + ", num_2 ," = ", num_1-num_2 )  
 
elif operator == 'multiply':
    print( num_1 ," + ", num_2 ," = ", num_1*num_2 )

elif operator == 'division':
    print( num_1 ," + ", num_2 ," = ", num_1/num_2 )

else:
    print("enter valid operation")

print("THANK YOU !!")