import random

def generate_number(): 
    return random.randint(1,100)

def get_player_input():
    while True:
        try:
            guess = int(input("ENTER YOUR GUESS (1-100):"))
            if 1 <= guess <= 100:
                return guess
            else:
                print("PLEASE ENTER A NUMBER IN THE RANGE OF 1 TO 10")
        except ValueError:
            print("invalid input.pls provide a valid number")     
            
            
def play_round():
    target = generate_number()
    attempts = 0
    
    while True:
        guess = get_player_input()
        attempts += 1
         
        if guess < target:
                print("TOO LOW. GIVE ANOTHER GUESS")

        elif guess > target:
            print("TOO HIGH. GIVE ANOTHER GUESS")

        else:
            print(f"EXCELLENT! YOU GUESSED THE NUMBER IN {attempts} ATTEMPTS.")

            if 1 <= attempts <= 5:
                    print("EXCELLENT JOB!!!")
            elif 6 <= attempts <= 10:
                    print("GOOD JOB!!")
            elif 11 <= attempts <= 15:
                    print("UMMM... STILL GOOD!")
            else:
                    print("NOT THAT GOOD. KEEP PRACTICING")

            return attempts
def ask_replay():
    return input("\nWould you like to play another round? (y/n):").lower() == "y"

def guess_the_number():
    print("\nWELCOME TO GUESS THE GUESS THE NUMBER EXPERIENCE !!!")
    print("YOU HAVE TO GUESS THE NUMBER FROM 1 TO 100\n")
    print("1 TO 15 ATTEMPTS = EXCELLENT!!!!")
    print("6 TO 10 ATTEMPTS = GOOD JOB.!!")
    print("more than 10 = UMMM....STILL GOOOD!")
    print("AFTER 10 ATTEMPTS = NOT THAT GOOD. KEEP PRACTICING")
    
    total_attempts = 0
    rounds_played = 1

    while True:
        print(f"\n--- Round number {rounds_played}---")
        attempts = play_round()
        
        total_attempts += attempts
        rounds_played += 1
        
        if not ask_replay():
            break
        
    print("\n---Session Summary---")
    print(f"TOTAL ROUNDS PLAYED : {rounds_played}")
    print(f"TOTAL ATTEMPTS : {total_attempts}")
    print("THANK YOU FOR PLAYING.Session terminated\n")
    
guess_the_number()