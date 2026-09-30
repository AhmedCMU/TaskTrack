import random
def generate_number():
    Number = random.randint(1,1000)
    
    while Number % 2 == 0:
      Number = random.randint(1,1000)
    return Number
  
def is_valid_guess(guess):
  if 1 <= guess <= 1000 and guess % 2 == 1:
    return True
 
  else:
     return False 
   
def check_guess(guess, secret_number):
  if guess < secret_number:
    return "Too low"
  elif guess > secret_number:
    return "Too high" 
  else:
    return "Correct"