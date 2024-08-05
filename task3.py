# Task 3: Write a program that takes user input for three numbers and prints the largest and smallest among them.

#Function To find the largest number:

def find_largest(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
#Function To find the smallest number:

def find_smallest(num1,num2,num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3
# main function:

def main():
    # Get the input from user for three numbers

    print("ENTER THREE NUMBERS TO FIND THE LARGEST AND SMALLEST AMONG THEM")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    num1=float(input("Enter the 1st number: "))
    num2=float(input("Enter the 2nd number: "))
    num3=float(input("Enter the 3rd number: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    largest =find_largest(num1,num2,num3)
    smallest =find_smallest(num1,num2,num3)

    print(f"\nThe largest number among {num1},{num2},and{num3} is : {largest}")
    print(f"\nThe smallest number among {num1},{num2},and{num3} is : {smallest}")

if __name__ == "__main__":
    main()