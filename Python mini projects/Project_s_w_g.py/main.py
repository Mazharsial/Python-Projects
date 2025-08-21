import random


# -1 for snake
# 0 for water
# 1 for gun

startgame=input("Do You want To Start The Game?\n Enter y/n: ")
if(startgame=="n"):
    print("Game Exiting....")
else:
    while True:

                computer=random.choice([-1,0,1])
                userinput=input("Enter Your Choice: s/w/gy ")
                userinputdict={"s":-1, "w":0, "g":1}
                reversedict={-1:"snake", 0:"water", 1:"gun"}

                yourchoice=userinputdict[userinput]

                print(f"You choices: {reversedict[yourchoice]}\n Computer choices: {reversedict[computer]}")


                if(computer==yourchoice):
                    print("Match Drawn")

                else:
                            if (computer == -1 and yourchoice == 0):  # Snake vs Water
                                print("Computer wins! Snake drinks water.")
                            elif (computer == -1 and yourchoice == 1):  # Snake vs Gun
                                print("You win! Gun kills snake.")
                            elif (computer == 0 and yourchoice == -1):  # Water vs Snake
                                print("You win! Snake drinks water.")
                            elif (computer == 0 and yourchoice == 1):  # Water vs Gun
                                print("Computer wins! Water drowns gun.")
                            elif (computer == 1 and yourchoice == 0):  # Gun vs Water
                                print("You win! Water drowns gun.")
                            elif (computer == 1 and yourchoice == -1):  # Gun vs Snake
                                print("Computer wins! Gun kills snake.")
                            else:
                                print("It's a draw or something went wrong.")

                            