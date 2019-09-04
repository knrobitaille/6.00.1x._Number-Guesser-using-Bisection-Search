print("Please think of a secret number between 0 and 100!")
low = 0
high = 100
ans = int((high + low) / 2)
response = ""
guessed = False

while not guessed:
    print("Is your secret number " + str(ans) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while response not in ['h','l','c']:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(int(ans)) + "?")  
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == 'h':
        high = ans
    elif response == 'l':
        low = ans
    elif response == 'c':
        print("Game over. Your secret number was: " + str(int(ans)))
        guessed == True
        break
    ans = int(float((high + low) / 2))
    
    
