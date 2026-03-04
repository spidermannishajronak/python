import random

def generate_number():
    return random.randint(1, 20)

def get_player_input():
    while True:
        try:
            guess = int(input("ENTER YOUR GUESS(1 TO 20):"))
            if 1 <= guess <= 20:
                return guess
            else:
                print("INVALID NUMBER! PLEASE PUT A NUMBER IN THE RANGE OF 1 TO 20.")
        except ValueError:
            print("INVALID.THIS IS NOT A NUMBER.PLEASE PUT A NUMBER IN A RANGE OF 1 TO 20.")
            
            
def play_round():
    target = generate_number()
    attempts = 0
    
    while True:
        guess = get_player_input()
        attempts += 1
        
        if guess < target:
            print("TOO LOW.GIVE ANOTHER GUESS \:")
            
        elif guess > target:
            print("TOO HIGH.GIVE ANOTHER GUESS /:")
            
        else:
            print(f"EXCELLENT!!!!!!!!!!!!!!!YOU GUSSED THE NUMBER IN {attempts} attempts")
            return attempts
        
def ask_replay():
    return input("\nWOULD YOU LIKE TO PLAY ANOTHER ROUND(y/n):").lower() == "y"

def guess_the_number():
    print("\nWELCOME TO GUESS THE NUMBER!!! THIS IS A GAME WHERE YOU HAVE TO GUESS THE NUMBER FROM 1 TO 20\n")
    
    total_attempts =  0
    rounds_played = 0
    
    while True:
        print(f"\n___ROUND NUMBER{rounds_played}___")
        attempts = play_round()
        
        total_attempts += attempts
        rounds_played += 1
        
        if not ask_replay():
            break
        
    print("\n______SESSION SUMMARY______")
    print(f"total rounds played : {rounds_played}")
    print(f"total attempts : {total_attempts}")
    print("THANKYOU FOR PLAYING.SESSION TERMINATED\n")
            
guess_the_number()