import random

def display_rules():
    print("\n______________GAME RULES__________________")
    print("ROCK BEATS SCISSORS.")
    print("SCISSORS BEATS PAPER")
    print("PAPER BEATS ROCK")
    
def determine_winner(user,computer):
    if user == computer:
        return "tie"
    
    if (user == "rock" and computer == "scisssors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "user"
        
    else:
        return "computer"
    
def rock_paper_scissors():
    total_choices = ["rock", "paper", "scissors"]
    
    while True:
        user_score = 0
        computer_score = 0    
        rounds_played = 1
        
        print("\nWELCOME TO ROCK PAPER SCISSORS !!!!!!!!!")
        print("TYPE'rules'TO SEE HOW TO PLAY THE GAME OR TYPE 'EXIT' TO EXIT THE GAME.")
        print("THANK YOU.")
        
        while True:
            print(f"\n______________ROUND{rounds_played}_____________")
            print("AVAILAIBLE CHOICES:ROCK,PAPER,SCISSORS,RULES,EXIT")
            user_choice = input("ENTER YOUR CHOICE:")
            
            if user_choice == "exit":
                print("BYE BYE SEE YOU NEXT TIME :]")
                print(f"FINAL SCORES => you: {user_score} AND computer score: {computer_score}")
                return exit
            elif user_choice == 'rules':
                display_rules()
                continue 
            
            elif user_choice not in total_choices:
                print("INVALID INPUT.PLEASE ENTER ROCK,PAPER OR SCISSSORS,RULES,EXIT")
                continue
            
            computer_choice = random.choice(total_choices)
            print(f"COMPUTER CHOOSE:{computer_choice}")
            
            result = determine_winner(user_choice,computer_choice)
            
            if result == "tie":
                print("ITS A DRAW")
                
            elif result == "user":
                print("YOU WIN !!!")
                user_score +=1  
            elif result == "computer":
                print("YOU LOSE!!!")
                computer_score +=1
                
                
            print(f"current score => you: {user_score}_______________computer_score:{computer_score}")
            rounds_played += 1
            
            play_again = input("WOULD YOU LIKE TO PLAY ANOTHER ROUND(yes/no):").lower()
            if play_again==('no'):
                print("GOODBYE")
                break
rock_paper_scissors()             

                
            
                   
