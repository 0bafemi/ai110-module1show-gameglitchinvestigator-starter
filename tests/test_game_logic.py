from logic_utils import check_guess 
from logic_utils import parse_guess
from logic_utils import update_score
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Go LOWER"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Go HIGHER"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_guess_out_of_range_too_low():
    """Test that guesses below the range are rejected"""
    ok, guess, err = parse_guess("0", 1, 20)
    assert ok == False
    assert err == "Please enter a number between 1 and 20."

def test_guess_out_of_range_too_high():
    """Test that guesses above the range are rejected"""
    ok, guess, err = parse_guess("25", 1, 20)
    assert ok == False
    assert err == "Please enter a number between 1 and 20."

def test_guess_within_range():
    """Test that valid guesses within range are accepted"""
    ok, guess, err = parse_guess("10", 1, 20)
    assert ok == True
    assert guess == 10
    assert err == None

def test_winning_score_first_attempt():
    """Test that winning on first attempt awards maximum points"""
    score = update_score(0, "Win", 1)
    # 100 - 10 * (1 + 1) = 100 - 20 = 80
    assert score == 80

def test_winning_score_many_attempts():
    """Test that winning after many attempts awards minimum points"""
    score = update_score(0, "Win", 10)
    # 100 - 10 * (10 + 1) = 100 - 110 = -10, but minimum is 10
    assert score == 10

def test_wrong_guess_always_loses_points():
    """Test that wrong guesses always lose 5 points"""
    score_high = update_score(100, "Too High", 2)
    score_low = update_score(100, "Too Low", 2)
    score_high_odd = update_score(100, "Too High", 3)
    
    # All should lose 5 points regardless of attempt number
    assert score_high == 95
    assert score_low == 95
    assert score_high_odd == 95