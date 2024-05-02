# Rock Paper Scissor Mini Game with PC
import random
# Make a function to check who win this game
def win_method(player,pc):
    if player == pc:
        print("↪\tTie!")
        return 0
    elif player == "Rock":
        if pc == "Scissor":
            print("↪\tYou Win!")
            return 1
        elif pc == "Paper":
            print("↪\tYou Lose!")
            return 2
    elif player == "Paper":
        if pc == "Scissor":
            print("↪\tYou Lose!")
            return 2
        elif pc == "Rock":
            print("↪\tYou Win!")
            return 1
    elif player == "Scissor":
        if pc == "Rock":
            print("↪\tYou Lose!")
            return 2
        elif pc == "Paper":
            print("↪\tYou Win!")
            return 1
print("    ----- Welcome To RPS Game ----- ")
player_score = 0
pc_score = 0
while True: # while loop until player don't want repeat
    list = ['Rock','Paper','Scissor'] # 3 choices for both
    pc = random.choice(list) # computer choose
    print("[Rock]\t\t[Paper]\t\t[Scissor]\n")
    player = str(input("> ")).title() # player choose
    print("")
    if player in list: # if player reply answer in choices
        print("> > > Computer: "+pc+" < < <")
        print("")
        print("> > > You: "+player+" < < <")
        print("")
        W = win_method(player,pc) #  call function 
        if W == 1:
            player_score += 1
        elif W == 2:
            pc_score += 1
        print(" - "*10)
        print("Player: ",player_score)
        print("Pc: ",pc_score)
        print(" - "*10)
        repeat = input("Do you want play again? (Yes/No): ").upper() # player want play again or not?
        if repeat == "YES":
            pass
        elif repeat == "NO":
            print("😁 Thanks For Playing")
            break
        else:
            print("😢 Invalid Value!")
            break
    else: # if player reply answer not in choices
        print("")
        print(" ⊠ "*12)
        print("Invalid Value, Please Write Again!")
        print(" ⊠ "*12)
        print("")
