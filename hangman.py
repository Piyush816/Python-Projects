import random




man = [
"""
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
  ___|___

""",
"""
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
  ___|___

""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
  ___|___

""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
  ___|___

""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
  ___|___

"""
,

"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
  ___|___
"""

]


word_list = ["hello", "people", "word", "wolf", "cockroch", "telepathy"]

no_of_attempts = 0

selected_word = word_list[random.randint(0, len(word_list)-1)]

# char list entered by user 
char_list = [ "_" for i in selected_word ]


def display_word(char):
    global  char_list
    for index,letter in enumerate(selected_word):
        if (char == letter ):
            char_list[index] = char

def check_char(char):
    global no_of_attempts
    if (char in selected_word):
        if (char in char_list):
            no_of_attempts+=1 
            return False

        else:
            return True
    else:
        no_of_attempts+=1
        return False


if __name__ == "__main__":

    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         
    
    """)


    print()

    while (no_of_attempts < 6):
        
        print(" ".join(char_list))

        print()
      
        char = input("Guess the word: ")

        if (not check_char(char)):
            print(man[no_of_attempts-1])

        display_word(char)

        if  ("".join(char_list)==selected_word):
            print("Winner!")
            break


    





    


