import art
import game_data 
import random
import os 


temp_list_hidden = list(range(len(game_data.data)))
#index list to prevent redundant data in comparisons

def rand_choice_index_and_array(temp_list):
    if temp_list == []:
        return -1
    random_choice = random.choice(temp_list)
    temp_list.remove(random_choice)
    return [random_choice , temp_list]

def entry_values(index_value , data):
#Gets all 4 values for the index value
    name = data[index_value]["name"]
    follower_count = data[index_value]["follower_count"]
    description = data[index_value]["description"]
    country = data[index_value]["country"]
    return follower_count,(f"{name}, {description}, from {country}") 



os.system('cls')
print(art.logo)
print("Welcome to higher Lower game CLI-ed")
begin_ques = input("Wanna begin? Type y/n: ").lower()
if begin_ques == "y":
    print("Let's go!")
#Clears screen
count = 0
temp_score = count

guess = "right"
while guess == "right":
    
    os.system('cls')
    print(art.logo)
    print(f"Welcome to higher Lower game CLI-ed      Score ({count})\n-----------------------------------")

    if temp_score != count:
        temp_score +=1
    else:
        rand_index = rand_choice_index_and_array(temp_list_hidden)[0]    

    values_at_index = entry_values(rand_index,game_data.data)
    follower_count1 = values_at_index[0]
    print(f"Compare A : {values_at_index[1]}")

    print(art.vs)

    rand_index = rand_choice_index_and_array(temp_list_hidden)[0]
    values_at_index = entry_values(rand_index,game_data.data)
    follower_count2 = values_at_index[0]
    print(f"Against B : {values_at_index[1]}\n")
    
    user_guess= input("Which has higher number of followers? Type a / b : ")


    if user_guess=="a" and follower_count1 > follower_count2:
        print(f"Yes, they have {follower_count1}M followers")
       
    elif user_guess=="b" and follower_count2 > follower_count1:
        print(f"Yes, they have {follower_count2}M followers")
       
    else :
        print("Sorry, better luck next time!")
        guess = "wrong"
    count +=1