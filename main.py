import os
import random

from art import logo, vs
from list_a import celeberities


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



print(logo)
user_score = 0
game_over = False
list_of_celebs = []
for celebs in celeberities:
    list_of_celebs.append(celebs)
def randomchoice():
    global random_celeb1 
    global random_celeb2
    global choices_for_second
    random_celeb1 = random.choice(list_of_celebs)
    choices_for_second = list_of_celebs.copy()
    choices_for_second.remove(random_celeb1)
    random_celeb2 = random.choice(choices_for_second)

def higherorlower():
    randomchoice()
    print(f"Compare A: {random_celeb1}")
    print(vs)
    print(f"Compare B: {random_celeb2}")
    
        

clear_screen()
print(logo)
while not game_over:
    higherorlower()
    user_input = input("Who has more followers? 'a' or 'b': ")
    user_input_lower = user_input.lower()
    if (user_input_lower == "a" and random_celeb1 > random_celeb2) or \
        (user_input_lower == "b" and random_celeb2 > random_celeb1):
        user_score += 1
        clear_screen()
        print(logo)
        print(f"You're Right! Score:{user_score}")
    else:
        game_over = True
        clear_screen()
        print(logo)
        print(f"Sorry, That's the wrong answer! Score:{user_score}")