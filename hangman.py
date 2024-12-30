import random
import time

def display_word_status(word, guessed_letters):
    print("\nCurrent word status: ", end="")
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def display_hangman(wrong_guesses, stages):
    if wrong_guesses < len(stages):
        print(stages[wrong_guesses])
    else:
        print(stages[-1]) 
def get_random_word(difficulty):
    easy_words = [
        'cat', 'dog', 'fish', 'tree', 'book', 'bird', 'ball', 'sun', 'moon', 'star'
    ]
    
    medium_words = [
        'planet', 'guitar', 'python', 'elephant', 'garden', 'puzzle', 'rocket', 'jungle', 'camera', 'forest'
    ]
    
    hard_words = [
        'encyclopedia', 'constellation', 'philosophy', 'astronomy', 'metamorphosis', 'architecture', 
        'bioluminescence', 'photosynthesis', 'thermodynamics', 'anthropology'
    ]
    
    if difficulty == "Easy":
        return random.choice(easy_words)
    elif difficulty == "Medium":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)

scoreboard = {}

def update_scoreboard(player_name, score, time_taken, difficulty):
    if player_name in scoreboard:
        scoreboard[player_name].append((score, time_taken, difficulty))
    else:
        scoreboard[player_name] = [(score, time_taken, difficulty)]

def display_scoreboard():
    print("\nScoreboard:")
    if scoreboard:
        for player, scores in scoreboard.items():
            for score, time_taken, difficulty in scores:
                print(f"{player}: {score} points, Time: {time_taken:.2f} seconds, Difficulty: {difficulty}")
    else:
        print("No scores yet.")

def play_hangman(player_name, difficulty):
    full_stages = [
        """
           -----   
           |   |   
               |   
               |   
               |   
               |   
        --------
        """,
        """
           -----   
           |   |   
           O   |   
               |   
               |   
               |   
        --------
        """,
        """
           -----   
           |   |   
           O   |   
           |   |   
               |   
               |   
        --------
        """,
        """
           -----   
           |   |   
           O   |   
          /|   |   
               |   
               |   
        --------
        """,
        """
           -----   
           |   |   
           O   |   
          /|\\  |   
               |   
               |   
        --------
        """,
        """
           -----   
           |   |   
           O   |   
          /|\\  |   
          /    |   
               |   
        --------
        """,
        """
           -----   
           |   |   
           O   |   
          /|\\  |   
          / \\  |   
               |   
        --------
        """
    ]
    
    stages = full_stages  
    max_guesses = 6  
    word_to_guess = get_random_word(difficulty)
    guessed_letters = set()
    wrong_guesses = 0
    score = 0
    
    start_time = time.time() 

    while wrong_guesses < max_guesses and set(word_to_guess) != guessed_letters:
        display_word_status(word_to_guess, guessed_letters)
        display_hangman(wrong_guesses, stages)

        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, {guess} is not in the word.")

    end_time = time.time() 
    time_taken = end_time - start_time

    if set(word_to_guess) == guessed_letters:
        print(f"Congratulations! You've guessed the word '{word_to_guess}'!")
        score = (max_guesses - wrong_guesses) * 10 
    else:
        display_hangman(max_guesses, stages)
        print(f"Game over! The word was '{word_to_guess}'.")

    update_scoreboard(player_name, score, time_taken, difficulty)

def main():
    while True:
        print("\nWelcome to the Hangman Game!")
        choice = input("Enter 'P' to play, 'S' to view the scoreboard, or 'Q' to quit: ").upper()

        if choice == 'P':
            player_name = input("Enter your player name: ")
            difficulty = input("Choose difficulty level (Easy, Medium, Hard): ").capitalize()
            if difficulty not in {"Easy", "Medium", "Hard"}:
                print("Invalid difficulty level. Defaulting to Medium.")
                difficulty = "Medium"
            play_hangman(player_name, difficulty)
        elif choice == 'S':
            display_scoreboard()
        elif choice == 'Q':
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()