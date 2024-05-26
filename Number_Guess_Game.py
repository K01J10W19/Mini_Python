#-----------------------------------------------------------------------------------------------------------------------------
# Modules Part
import fontstyle
import random
import math
#-----------------------------------------------------------------------------------------------------------------------------
# Function Part
def start_game(ans,N1,N2):
    times = 0
    F = N1
    L = N2
    Minimum_Guessing = round(math.log(L-F+1,2))
    print("<<<<< GAME START >>>>>")
    try:
        while True:
            print(fontstyle.apply(f"You Have {Minimum_Guessing-times} Chance Recently 😉","BOLD/UNDERLINE/WHITE"))
            user_input = int(input("Enter Your Answer: "))
            if user_input < F or user_input > L:
                    print("Your Input Is Out Of Range\nPlease Write a Correct Number in the Range !")
            else:
                times += 1
                if times < Minimum_Guessing:
                        if user_input == ans:
                            print(fontstyle.apply("CONGRATULATION 😁","BOLD/UNDERLINE/GREEN_BG/WHITE"))
                            print(fontstyle.apply(f"Totally Guess {times} Times 😁","BOLD/UNDERLINE/GREEN_BG/WHITE"))
                            break
                        else:
                            if user_input < ans:
                                F = user_input
                                print(fontstyle.apply("Try Again! You guessed too small","BOLD/UNDERLINE/BLUE_BG/WHITE"))
                                print(fontstyle.apply(f"{F} ~ {L}","BOLD/UNDERLINE/BLUE_BG/WHITE"))
                            elif user_input > ans:
                                L = user_input
                                print(fontstyle.apply("Try Again! You guessed too high","BOLD/UNDERLINE/BLUE_BG/WHITE"))
                                print(fontstyle.apply(f"{F}~{L}","BOLD/UNDERLINE/BLUE_BG/WHITE"))
                else:
                    print(fontstyle.apply("SORRY, You Are Answered Maximum!","BOLD/UNDERLINE/PURPLE_BG/WHITE"))
                    print(fontstyle.apply(f"The Correct Answer is {ans}!","BOLD/UNDERLINE/PURPLE_BG/WHITE"))
                    print(fontstyle.apply("Better Luck Next Time 🥲","BOLD/UNDERLINE/PURPLE_BG/WHITE"))
                    break
    except ValueError:
        print(fontstyle.apply("Invalid Input !","BOLD/UNDERLINE/RED"))
#------------------------------------------------------------------------------------------------------------------------------
# Implement Part
print("   ----- Welcome Number Guessing Game -----")
print("\t \\\ Select a Range of Number //")
try:
    while True:
        D = 0
        N1 = input("Head Of Num --> ")
        N2 = input("Last Of Num --> ")
        if N1.isalpha() or N2.isalpha():
            print(fontstyle.apply("Alphabetic Character is not Allowed!","BOLD/UNDERLINE/RED"))
            D = 1
        if '.' in N1 or '.' in N2:
            print(fontstyle.apply("Float Values is not Allowed!","BOLD/UNDERLINE/RED"))
            D = 1
        if D == 0:
            N1, N2 = int(N1),int(N2)
            R_NUM = random.randint(N1,N2)
            hint = fontstyle.apply("**Hint: Answer will appeared randomly from the range!","ITALIC/UNDERLINE/YELLOW")
            print(hint)
            start_game(R_NUM,N1,N2)
            print("\t \\\ User, You Want Play One More Game? //")
            re_play = input("[Yes/No] : ").upper()
            if re_play == "NO":
                print("THANK YOU FOR PLAYING NUMBER GUESSING GAMES🙉")
                break
            elif re_play == "YES":
                continue
            else:
                print("Invalid Value")
                break
except ValueError:
    pass

