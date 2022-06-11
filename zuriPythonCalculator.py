import sys
print("Welcome to the Python Calculator")
print("Operations: 'Addition', 'Subtraction', 'Division', 'Multiplication' and 'Modulus'")
print("")


while True:
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        break
    except KeyboardInterrupt:
        print("User cancelled operation. Exiting...")
        sys.exit()
    except:
        print("Input a number!")

print("\nWhat calculation would you like to perform?")
task = input("(Type in the operation you would like to perform): ")
task = task.capitalize()

if task == "Addition":
    addition_result = first_number + second_number 
    print(f"The sum of {str(first_number)} and {str(second_number)} is " + str(addition_result))

elif task == "Subtraction":
    subtraction_result = first_number - second_number
    print(f"The difference between {str(first_number)} and {str(second_number)} is " + str(subtraction_result))

elif task == "Multiplication":
    multi_result = first_number * second_number
    print(f"The product of {str(first_number)} and {str(second_number)} is " + str(multi_result))

elif task == "Division":
    div_result = first_number/second_number
    print(f"The quotient of {str(first_number)} and {str(second_number)} is " + str(div_result))

elif task == "Modulus":
    mod_result = first_number % second_number
    print(f"The result of the modulo operation of {str(first_number)} and {str(second_number)} is " + str(mod_result))

else:
    print("The operation is not supported")
