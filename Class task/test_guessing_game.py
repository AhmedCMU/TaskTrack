from GuessingGame import generate_number, is_valid_guess,check_guess
def test_number():
    number = generate_number()

    assert number >= 1
    assert number <= 1000
    assert number % 2 == 1

def test_valid_guess():
    assert is_valid_guess(501) == True
    assert is_valid_guess(500) == False
  
  
def test_check_guess():
    assert check_guess(300, 501) == "Too low"
    assert check_guess(700, 501) == "Too high"
    assert check_guess(501, 501) == "Correct"