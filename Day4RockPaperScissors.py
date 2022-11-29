rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
RPS = [rock,paper,scissors]
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
RockPaperScissors = int(input())
x = random.randint(0,2)
print(RPS[RockPaperScissors])
print(RPS[x])
if RockPaperScissors == x:
  print("Draw")
elif RockPaperScissors == 0 and x == 1 or RockPaperScissors == 1 and x == 2 or RockPaperScissors == 2 and x == 0:
  print("You Lose")
else:
  print("You Win")

  
