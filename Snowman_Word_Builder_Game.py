""" 
Name = Swastika Rijal
Date = 3rd Dec, 2025
Purpose = To create built-a-snowman word guessing game.
"""
import random
from graphics import *

# Function 1: draw_graphic_scene
# Purpose: To crreate graphics window with the  title and background
def draw_graphic_scene():
    # Creating  graphics window
    win = GraphWin("Build-a-Snowman Game", 400, 400)
    # Set background color
    win.setBackground(color_rgb(173, 216, 230))
    
    # Draw title in graphics window
    title = Text(Point(200, 30), "Build-a-Snowman Game")
    title.setSize(16)
    title.setStyle("bold")
    title.setTextColor("dark blue")
    title.draw(win)
    
    # Draw snowflakes in background
    for s in range(20):
        x = random.randint(30, 370)
        y = random.randint(30, 250)
        flake = Text(Point(x, y), "❄")
        flake.setSize(random.randint(8, 14))
        flake.setTextColor("white")
        flake.draw(win)
    
    # Draw ground
    ground = Rectangle(Point(0, 300), Point(400, 400))
    ground.setFill("white")
    ground.setOutline("white")
    ground.draw(win)
    
    return win

# Function 2: pick_random_word_from_file
# Purpose: To read words from file and return random word
def pick_random_word_from_file(inputfile):
    # Creates an empty list for storing valid words from the file
    words = []
    # Loops through the file to read each line
    for line in inputfile:
        # Use split() function to break the line into individual words
        line_words = line.split()
        # Add each word to the 'words' list
        for word in line_words:
            words.append(word.lower())
    # Select and return a random word
    return random.choice(words)

# Function 3: check_guess
# Purpose: To check if guessed letter is in secret word
def check_guess(guess, secret_word, guessed_letters):
    # Add guess to guessed_letters
    guessed_letters.append(guess)
    # Checks if guess is in secret_word
    return guess in secret_word

# Function 4: update_displayed_word
# Purpose: Create display string with underscores for unguessed letters
def update_displayed_word(secret_word, correct_letters):
    # Create display with underscores
    display = ""
    # Loop through each letter in secret_word
    for letter in secret_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

# Function 5: print_welcome
# Purpose: To print welcome message and instructions
def print_welcome():
    print("Welcome to the Build-a-Snowman Game!")
    print("\nINSTRUCTIONS:")
    print("Try to guess thee secret word")
    print("Each correct letter adds a part to your snowman")
    print("You have 6 incorrect guesses allowed\n")

# Function 6: termination_message
# Purpose: To display termination message when game ends
def termination_message():
    print("\nGame over!")
    print("Thank you for playing Build-a-Snowman!")

# Function 7: main
# Purpose: contols the game flow 
def main():
    # call print_welcome
    print_welcome()
    
    games_played = 0
    games_won = 0
    play_more = "yes"
    while play_more == "yes":
        games_played += 1
        print("Game " + str(games_played))
        
        # PART 2: Safer file handling with 'with' statement
        try:
            with open("words.txt", "r") as f:
                word = pick_random_word_from_file(f)
        except FileNotFoundError:
            print("Error: 'words.txt' not found.")
            return
        
        # Checks the file is not empty
        if not word:
            print("Error: No valid words found in the file.")
            return
        
        print("Secret word has " + str(len(word)) + " letters")
        
        # Game variables
        wrong = 0
        max_wrong = 6
        correct = ""
        guessed_letters = []
        parts_built = 0
        
        # Lists to track correct and incorrect letters
        correct_letters_list = []
        incorrect_letters_list = []
        
        # Create graphics window
        graphics_window = draw_graphic_scene()
        
        # Draw snowman parts directly in main function
        def draw_part(part_num):
            if part_num == 1:
                circle = Circle(Point(200, 300), 50)
                circle.setFill("white")
                circle.setOutline("black")
                circle.setWidth(2)
                circle.draw(graphics_window)
            elif part_num == 2:
                circle = Circle(Point(200, 230), 40)
                circle.setFill("white")
                circle.setOutline("black")
                circle.setWidth(2)
                circle.draw(graphics_window)
            elif part_num == 3:
                circle = Circle(Point(200, 170), 30)
                circle.setFill("white")
                circle.setOutline("black")
                circle.setWidth(2)
                circle.draw(graphics_window)
            elif part_num == 4:
                left_eye = Circle(Point(185, 165), 4)
                left_eye.setFill("black")
                left_eye.draw(graphics_window)
                right_eye = Circle(Point(215, 165), 4)
                right_eye.setFill("black")
                right_eye.draw(graphics_window)
            elif part_num == 5:
                nose = Polygon(Point(200, 170), Point(193, 180), Point(207, 180))
                nose.setFill("yellow")
                nose.setOutline("orange")
                nose.setWidth(2)
                nose.draw(graphics_window)
            elif part_num == 6:
                arm = Line(Point(160, 230), Point(130, 210))
                arm.setWidth(3)
                arm.setOutline(color_rgb(101, 67, 33))
                arm.draw(graphics_window)
            elif part_num == 7:
                arm = Line(Point(240, 230), Point(270, 210))
                arm.setWidth(3)
                arm.setOutline(color_rgb(101, 67, 33))
                arm.draw(graphics_window)
            elif part_num == 8:
                smile = Polygon(Point(180, 185), Point(187, 190), 
                              Point(200, 192), Point(213, 190),
                              Point(220, 185))
                smile.setFill("black")
                smile.draw(graphics_window)
            elif part_num == 9:
                hat_brim = Rectangle(Point(175, 140), Point(225, 150))
                hat_brim.setFill("black")
                hat_brim.draw(graphics_window)
                hat_top = Rectangle(Point(185, 125), Point(215, 140))
                hat_top.setFill("black")
                hat_top.draw(graphics_window)
        
        # Game loop
        while wrong < max_wrong:
            show_word = update_displayed_word(word, correct)
            print("\nWord: " + show_word)
            print("Wrong guesses: " + str(wrong) + "/" + str(max_wrong))
            
            if correct_letters_list:
                print("Correct letters: " + ", ".join(sorted(correct_letters_list)))
            if incorrect_letters_list:
                print("Incorrect letters: " + ", ".join(sorted(incorrect_letters_list)))
            
            # Get letter from user
            guess = input("Enter a letter (a-z): \n").lower()
            
            # Input validation
            if len(guess) != 1:
                print("Enter one letter only")
                continue
            
            if not guess.isalpha():
                print("Enter a letter (a-z) only")
                continue
            
            if guess in guessed_letters:
                print("You already tried that letter!")
                continue
            
            # Check the guess using the check_guess function  
            if check_guess(guess, word, guessed_letters):
                # CORRECT - Add to correct letters list
                if guess not in correct_letters_list:
                    correct_letters_list.append(guess)
                
                print("Good job! The letter '" + guess + "' is in the word.")
                correct += guess
                
                # Count occurrences in word
                count_in_word = word.count(guess)
                
                # Add snowman parts directly
                for _ in range(count_in_word):
                    parts_built += 1
                    if parts_built <= 9:
                        draw_part(parts_built)
                
                # Check if player won
                won = True
                for letter in word:
                    if letter not in correct:
                        won = False
                        break
                
                if won:
                    games_won += 1
                    print("\nBRAVO! You built the snowman!")
                    print("The word was: " + word.upper())
                    break
            else:
                # if incorrect then Add to incorrect letters list
                if guess not in incorrect_letters_list:
                    incorrect_letters_list.append(guess)
                
                print("Sorry, '" + guess + "' is not in the word.")
                wrong += 1
        
        # Game over message
        if wrong >= max_wrong:
            print("\nGAME OVER!")
            print("The word was: " + word.upper())
        
        # Save score to file directly in main
        try:
            remaining = max_wrong - wrong
            with open("scores.txt", "a") as f:
                f.write(f"Word: {word}, Correct parts: {parts_built}, Remaining chances: {remaining}\n")
        except:
            pass
        
        # After game ends, asking user to click to continue
        print("\nClick on the graphics window to continue...")
        graphics_window.getMouse()
        graphics_window.close()
        
        # Ask if player wants to play again
        print("\nPlay again? (yes/no)")
        play_more = input("Your choice: ").lower()
        while play_more not in ["yes", "no", "y", "n"]:
            print("Please type yes or no")
            play_more = input("Your choice: ").lower()
        
        if play_more == "y":
            play_more = "yes"
        elif play_more == "n":
            play_more = "no"
    
    # Save final scores when game ends
    try:
        with open("scores.txt", "a") as f:
            f.write(f"\nFINAL SCORES: Games played: {games_played}, Games won: {games_won}\n")
    except:
        pass
    
    # Show termination message
    termination_message()

# Run the program
if __name__ == "__main__":
    main()