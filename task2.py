# Task 2: Create a program to perform advanced arithmetic operations (power, modulo) using functions.
def power(base,power):
    return base**power
def modulo(dividend,divisor):
    return dividend%divisor

def main():
    print("ADVANCD ARITHMETIC OPERATIONS")

    # power operation
    base=int(input("Enter the base number for power operation: "))
    exponent=int(input("Enter the exponent:"))
    power_result=power(base,exponent)
    print(f"The resut of {base} raise to the power of {exponent}is: ",power_result)

    # modulo operation
    dividend=int(input("Enter the dividend for modulo operation: "))
    divisor=int(input("Enter the divisor:"))
    modulo_result=modulo(dividend,divisor)
    print(f"The resut of {dividend} raise to the power of {divisor}is: ",modulo_result)

if __name__=="__main__":
    main()