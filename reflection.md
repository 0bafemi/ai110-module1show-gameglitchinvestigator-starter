# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, several core features were broken. Pressing Enter to submit a guess did not work, even though the game instructed the user to press Enter, so I had to click the button manually. The hint system was also incorrect when compared to the actual secret number, and no warning appeared when I entered numbers outside the allowed range. Changing the difficulty did not update the secret number or the displayed guess range, and the New Game button did not fully reset the game, preventing new guesses. 


## 2. How did you use AI as a teammate?

I used GitHub Copilot for every bug fix in this project. One example I accepted: Copilot suggested using `st.form()` and `st.form_submit_button()` to handle Enter key submission, which was the exact solution needed - wrapping the input field in a form automatically triggers submission on Enter. One suggestion I changed: Copilot initially suggested creating a `reset_game()` function in logic_utils.py, but I rejected it because you wanted to keep refactoring focused only on moving existing functions, not creating new ones - so I implemented the reset logic directly in app.py instead while moving other functions to utils.

## 3. Debugging and testing your fixes

I decided a bug was fixed by running the Streamlit app and manually testing each scenario - for example, I pressed Enter on the guess input and verified it submitted; I changed the difficulty and confirmed the secret number changed and the displayed range updated. For testing with pytest, I ran tests like `test_guess_too_high()` and `test_guess_too_low()` to verify the hint system returned the correct messages ("Go LOWER" vs "Go HIGHER"), which immediately showed the original bug where hints were backwards. Copilot helped me structure test cases by suggesting the `assert outcome == "Too High"` and `assert message == "📉 Go LOWER!"` pattern to test both the outcome and the message tuple together.

## 4. What did you learn about Streamlit and state?

The secret number kept changing because Streamlit reruns the entire script from top to bottom every time you interact with the app (click a button, type in a field, etc.). Without `st.session_state`, the line `st.session_state.secret = random.randint(low, high)` would execute on every rerun, generating a new number each time. I would explain Streamlit reruns to a friend like this: "Every time you interact with a Streamlit app, it re-executes the whole script. Session state is like a sticky note that remembers values across reruns - you save things there so they don't reset." The key change was tracking the difficulty in session state and detecting when it changed, then only regenerating the secret when difficulty actually changed rather than on every rerun.

## 5. Looking ahead: your developer habits

One habit I want to reuse: committing after each bug fix with a clear, concise commit message describing exactly what was fixed. This made it easy to track which bugs were addressed and why. Next time with AI, I would ask clearer questions upfront about what should be refactored vs. what should stay in place, rather than having Copilot suggest new functions when the goal was to move existing ones. This project showed me that AI-generated code isn't production-ready by default - it had multiple logical bugs (backwards hints, rewarding wrong guesses, hardcoded values) that required careful testing and critical thinking to catch and fix.
