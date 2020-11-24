# Must install sympy for this to function properly
import sympy

# Will change the input so what it functions with sympy
def properInput(str):
    str.replace("sin", "sympy.sin")
    str.replace("cos", "sympy.cos")
    str.replace("tan", "sympy.tan")
    return str

continueVal = 'yes'

print("Instructions: Enter your problem in python input for equations ")
print("(Like ** for exponents and proper paranthesis use)")
print("Remeber tan(x)**2 + 1 is sec**2(x), sin(x)**2 + cos(x)**2 = 1, 1 + cot(x)**2 = csc(x)**2\n")


while (continueVal == 'yes' or continueVal == 'y'):
    try:
        equation = input("Enter your problem: ")
        equation = properInput(equation)
        result = sympy.diff(equation)

        print(result)
        continueVal = input("Another (Yes/Y/No/N)?: ")
        continueVal = continueVal.lower()

    except:
        print("Invalid Syntax: Enter the eqaution properly.")


        
    
