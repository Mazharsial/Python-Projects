import random

n=random.randint(1,100)
a=-1
guess=1
while(a != n):
    a=int(input("Guess the number : "))
    if(a>n):
        print("Enter the lower number please.")
        guess +=1
    elif(a<n):
        print("Enter the higher number PLease.")
        guess +=1
    
print(f"You have guessed the number {n} in attempts {guess}.")
