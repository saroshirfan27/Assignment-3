import random

num = random.randint(0, 100)
guess = -1
i = 0
while( guess != num ):
    guess = int(input("Enter number between 1 and 100 : "))
    if( guess < 1 or guess > 100 ):
        print("OUT OF RANGE")
        continue
    i = i + 1
    if( guess == num ):
        break
    if( num - guess > 50 ):
        print("V.LOW")
    elif ( guess - num > 50 ):
        print("V.HIGH")
    elif( num - guess > 25 ):
        print("LOW")
    elif ( guess - num > 25 ):
        print("HIGH")
    elif( num - guess > 10 ):
        print("Slight LOW")
    elif ( guess - num > 10 ):
        print("Slight HIGH")
    else:
        print("You are almost there")
    

print("\n\nNUMBER IS " + str (guess) )
print("CONGRATS YOU GUESSED IT RIGHT!!! AFTER " + str(i) + " ATTEMPTS")
