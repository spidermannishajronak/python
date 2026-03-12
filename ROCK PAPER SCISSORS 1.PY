import random

def display_rules():
    print("\n________GAME RULES________")
    print("ROCK BEATS SCISSORS")
    print("SCISSORS BEAT PAPER")
    print("PAPER BEATS ROCK")
    
def determine_winner(user,computer):
    if user == computer:
        return "tie"
        
        
    if (user == "rock" and computer == "scissors")or\
        (user == "scissors" and computer == "paper")or\
        (user == "paper" and computer == "rock"):
        return "user"
    
    else:
        return computer
    
    
def rock_paper_scissors():
     total_choices = ["rock" , "paper" , "scissors"]
     
     while True:
         user_score = 0 
         computer_score = 0
         rounds_played = 1
             
         print("\nWELCOME TO ROCK PAPER SCISSORS.IO")
         print("TYPE RULES TO SEE THE GAMES RULES OR TYPE LEAVE TO EXIT THE GAME")
         
         while True:
              print(f"\n__________ROUND {rounds_played}__________")
              print(f"\nAVALIBLE CHOICES : ROCK , PAPER , SCISSORS , RULES , EXIT")
              user_choice = input("ENTER YOUR CHOICE:")
              
              if user_choice == "exit":
                  print("GET OUT")
                  print(f"user score: {user_score} computer score: {computer_score}")
                  return exit
              if user_choice == "rules":
                  display_rules()
                  continue
              
              elif user_choice not in total_choices:
                  print("INVALID INPUT")
                  continue
              computer_choice = random.choice(total_choices)
              print(f"COMPUTER CHOOSE: {computer_choice}")
              
              result = determine_winner(user_choice,computer_choice)
              
              if result == "user" == "computer":
                  print("ITS A TIE")
              elif result == "user":
                  print("YOU WIN")
                  user_score += 1
              elif result == "computer":
                  print("YOU LOSE")
                  computer_score += 1
                  
                  print(f"USER SCORE : {user_score} COMPUTER SCORE : {computer_score}")
                  rounds_played += 1
                  
                  play_again = input("WOULD YOU LIKE TO PLAY ANOTHER ROUND(YES/NO)?:")
                  if play_again == ('NO'):
                      print("BYE")
                      break
rock_paper_scissors()

        

                

        










































































      