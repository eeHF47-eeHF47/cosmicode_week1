# Task 4: Implement a program to calculate the area of complex shapes like a trapezoid or an ellipse.
import math

def calculate_trapezoid_area(a,b,h):
    return 0.5*(a+b)*h

def calculate_ellipse_area(a,b):
    return math.pi*a*b

def main():
    print("````````````````")
    print("SELECT THE SHAPE")
    print("````````````````")
    print("1.Trapezoid")
    print("2.Ellipse")

    choice= input("Enter choice (1/2):")

    if choice == '1':
        # trapezoid
        print("```````````````````````````````````````````````````````")
        a= float(input("Enter the length of first parallel side:" ))
        b=float(input("Enter the length of second parallel side:" ))
        h=float(input("Enter the height between the parallel sides:" ))
        print("```````````````````````````````````````````````````````")
        area= calculate_trapezoid_area(a,b,h)
        print(f"The area of the trapezoid is:{area}")

    elif choice =='2':
        # Ellipse
        a= float(input("Enter the length of semi-major axis:" ))
        b=float(input("Enter the length of semi-minor axis:" )) 
        area=calculate_ellipse_area(a,b)
        print(f"The area of the ellipse is:{area}")

    else:
        print("Invalid choise,Please select 1 or 2.")
        
if __name__=="__main__":
    main()