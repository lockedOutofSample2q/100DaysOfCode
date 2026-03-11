wordlist = ["topaz", "snake", "mouse", "tubes", "phone"]
import os
import random
chosen_word = random.choice(wordlist)



count = 0
arr = ['_', '_', '_', '_', '_']
temp_count = 0
while count<5:
    os.system('cls')
    if(count > temp_count):
        temp_count = count
        print(f"Wrong guess! \nYou have {5-count}/5 guesses left")
        print("\n\n\nguess word: ")
    else : 
        print("\n\n\n\nguess word: ")
    print(" ".join(arr))
    alphabet_guess = input()
    
    if alphabet_guess in chosen_word:
        print("Correct guess!")
       
        for i in chosen_word:
            if alphabet_guess == i:
                arr[chosen_word.index(i)] = alphabet_guess
        print(" ".join(arr))
        if arr==list(chosen_word):
            print("You win!")
            break
    else :
        count+= 1
        
    
print(f"You lose! The word was {chosen_word}")
