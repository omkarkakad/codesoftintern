# Rock Paper Scissor
import random

def USERchoise():
	while True:
		user = input("Choose Rock, Paper, or Scissors: ").strip().lower()
		if user in ["rock", "paper", "scissors"]:
			return user
		else:
			print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def COMPUTERchoice():
	options = ["rock", "paper", "scissors"]
	return random.choice(options)

def WINNER(user, computer):
	if user == computer:
		return "It's a tie!"
	elif (
		(user == "rock" and computer== "scissors") or
		(user == "paper" and computer== "rock") or
		(user == "scissors" and computer == "paper")
	):
		return "You win!"
	else:
		return "Computer wins!"

def main():
	print("Welcome to Rock, Paper, Scissors!")
	while True:
		user=USERchoise()
		computer= COMPUTERchoice()
		print(f"You choose {user}")
		print(f"Computer choose {computer}")
		result = WINNER(user, computer)
		print(result)
        
		play_again = input("Do you want to play again? (yes/no): ").strip().lower()
		if play_again != "yes":
			break

if __name__ == "__main__":
	main()
