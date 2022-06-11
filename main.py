from random import choice

print("Welcome to Rock, Paper, Scissors. Good luck!")

while True:
    print("")
    print("You have  the following options: \n    * R - Rock          * P - Paper         * S - Scissors")

    options = ["R","P","S"]
    computer_choice = choice(options) 

    
    user_input = input("Make a choice: ")
    user_choice = user_input.upper()
    
    if user_choice not in options:
        print("You must pick one of the following: \"R\", \"P\", \"S\"")
        continue

    if user_choice in options:
        print(f"Player ({user_choice}) : CPU ({computer_choice})")
        
        #R/P condition
        if user_choice == "R" and computer_choice == "S":
            print("Rock smashes Scissors. You win!")

        elif user_choice == "S" and computer_choice == "R":
            print("Rock smashes Scissors. You lose!")
    
        #S/P condition
        elif user_choice == "S" and computer_choice == "P":
            print("Scissors cuts Paper. You win!")

        elif user_choice == "P" and computer_choice == "S":
            print("Scissors cuts Paper. You lose!")
    
        #R/P condition
        elif user_choice == "P" and computer_choice == "R":
            print("Paper covers Rock. You win!")

        elif user_choice == "R" and computer_choice == "P":
            print("Paper covers Rock. You lose!")

        #Draw condition
        elif user_choice == computer_choice:
            print("It's a draw")
    
    play_again = input("Would you like to play again? [y/n] :")
    play_again = play_again.lower().strip()
    if play_again == "n":
        print("Ending game, thanks for playing...")
        break
# Print the right message, based on the choices
