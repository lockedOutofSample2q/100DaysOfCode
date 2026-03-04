import random 




dead_fish = ''' 
|\    \ \ \ \ \ \ \      __
|  \    \ \ \ \ \ \ \   | O~-_
|   >----|-|-|-|-|-|-|--|  __/
|  /    / / / / / / /   |__/
|/     / / / / / / /           
'''


#1
new_fish = '''           /"*._         _
      .-*'`    `*-.._.-\'/
    < * ))     ,       (
      `*-._`._(__.--*\"`.\ '''
#2
ball = '''   _._
.'--.`.    
|  .' |    
 `--`' '''

#3
pan = '''     (\
     \ \
 __    \/ ___,.-------..__        __
//\\ _,-'\\               `'--._ //\\
\\ ;'      \\                   `: //
 `(          \\                   )'
   :.          \\,----,         ,;
    `.`--.___   (    /  ___.--','
      `.     ``-----'-''     ,'
         -.               ,-
            `-._______.-' '''


wine = ''' ()   ()      ()    /
  ()      ()  ()  /
    _____________/__   
    \^^^^^^^^^^/^^^/
     \     ___/   /
      \   (   )  /
       \  (___) /
        \ /    /
         \    /
          \  /
           \/
           ||
           ||
           ||
           /\
          /;;\
     ==============  '''



user_input = input(" Choose from Fish(1) or Ball(2) or Pan(3) ")
system_output = random.randint(1,3)

if user_input == "1" :
    print(new_fish)
    print("\nsystem chose:          \n\n\n")
    if (system_output)==1:
        print(new_fish)
        print("DRAW")
    elif (system_output)==2:  
        print(ball)
        print("YOU LOSE")
        print(dead_fish)
    else: 
        print(pan)
        print("YOU LOSE")
        print(dead_fish)
elif user_input == "2" :
    print(ball)
    print("system chose:         \n\n\n ")
    if (system_output)==1:
        print(new_fish)
        print("YOU WIN")
        print(dead_fish)
    elif (system_output)==2:
        print(ball)
        print("DRAW")
    else: 
        print(pan)
        print("YOU WIN")
        print(wine)
elif user_input == "3" :
    print(pan)
    print("system chose:       \n\n\n   ")
    if (system_output)==1:
        print(new_fish)
        print("YOU WIN")
        print(dead_fish)

    elif (system_output)==2:
        print(ball)
        print("YOU LOSE")
        
    else: 
        print(pan)
        print("DRAW")


