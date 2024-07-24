#Python Program to Make a Simple Calcultor Using Funtions.

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

number1 =float(input("Enter 1st number:"))
number2 =float(input("Enter 2nd number:"))

print("select opertion:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplicaton")
print ("4. Division")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1','2','3','4'):
         
            if choice =='1':
               print(number1,"+",number2,"=",addition(number1,number2))

            elif choice =='2':
               print(number1,"-",number2,"=",subtraction(number1,number2))
             
            elif choice =='3':
               print(number1,"*",number2,"=",multiplication(number1,number2))

            elif choice =='4':
               print(number1,"/",number2,"=",division(number1,number2))
    break 
    exit()
else:  
         print("Invalid Input") 

