''' TRY AND EXCEPT 
We use the try and exception to handle exception or error.
'''

# TRY Block : Inside this block we write those code that may occur an error
# Except : In this we write what kind of error is occur.
# Else : That run when there is no error is occur.
#finally : This block is always run , whenever error is occur or not occur.

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))

# only one try with one exception
try:
    c = int(a) / int(b)
    print("Result :",c)

except ZeroDivisionError:
    print("Cant be divided by zero")

# Second program
try:
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    m = a * b
    r = a// b

except ZeroDivisionError:
    print("Cant Divided by Zero")

except Exception as e: # Return an type of error
    print("Error" ,e)

else:  # Run when there is no exception 
     print(f"Multipilcation of {a} or {b} is :" ,m)
     print(f"Remainder of {a} or {b} :",r)


# Check for age for vote
try:
    def check(age):
        
        if age< 0:
            print(" Age cant nagative ")

        elif age < 18:
            print("You are not aligible for vote")

        else:
            print(" You can vote ")

        

    age = int(input("Enter your age :"))
    check(age)

except Exception as e:
            print("Error :",e)
finally:
     print("This block of code is always run.")



