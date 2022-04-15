class Game():


    def play_game(self, player1_choice, player2_choice):                     
        if player1_choice == "scissors" and player2_choice == "rock":
            return "Player 2 wins by playing rock"

        elif player1_choice == "scissors" and player2_choice == "paper":
            return "Player 1 wins by playing scissors" 

        elif player1_choice == "rock" and player2_choice == "scissors":
            return "Player 1 wins by playing rock"
            
        elif player1_choice == "rock" and player2_choice == "paper":
            return "Player 2 wins by playing paper"

        elif player1_choice == "paper" and player2_choice == "scissor":
            return "Player 2 wins by playing scissor"
        
        elif player1_choice == "paper" and player2_choice == "rock":
            return "Player 1 wins by playing paper"

        else:
            player1_choice == player2_choice
            return "Its a draw"


            
