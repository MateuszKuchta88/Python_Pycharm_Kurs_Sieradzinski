# PD8 4 - Hangman

# TASK DESCRIPTION
# Modify the Hangman game so that passwords are drawn from a text file.

# Import libraries
import random
import tkinter as tk
from tkinter import messagebox


class HangmanApp:
    def __init__(self, root):
        """
        Initialize the Hangman application, setting up the UI and game state.

        Args:
            root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Hangman Game")

        # Load words from the file specified
        self.word_list = self.load_words("words.txt")
        if not self.word_list:
            # If no words are loaded, show an error message and exit
            messagebox.showerror("Error", "Word list is empty. Please check words.txt")
            root.destroy()
            return

        # Initialize game variables
        self.word_to_guess = random.choice(self.word_list)  # Randomly choose a word to guess
        self.guessed_letters = []  # Store guessed letters
        self.hangman = '-------'  # Visual representation of hangman progress
        self.word_encoded = self.encode_word()  # Encoded version of the word with hidden letters

        # Create UI components for the game
        self.label_word = tk.Label(root, text=f"Word to guess: {self.word_encoded}", font=("Arial", 14))
        self.label_word.pack(pady=10)

        self.label_hangman = tk.Label(root, text=f"Hangman: {self.hangman}", font=("Arial", 14))
        self.label_hangman.pack(pady=10)

        self.entry_guess = tk.Entry(root, font=("Arial", 14))
        self.entry_guess.pack(pady=10)

        self.button_guess = tk.Button(root, text="Guess", command=self.handle_guess, font=("Arial", 12))
        self.button_guess.pack(pady=5)

        self.button_reset = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 12))
        self.button_reset.pack(pady=5)

    def load_words(self, file_path):
        """
        Load words from a text file.

        Args:
            file_path: Path to the file containing words.

        Returns:
            A list of words if the file is found and readable, otherwise an empty list.
        """
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"The file '{file_path}' does not exist.")
            return []

    def encode_word(self):
        """
        Encode the word by replacing unguessed letters with dashes.

        Returns:
            A string where guessed letters are revealed, and unguessed letters are replaced with '-'.
        """
        return ''.join(letter if letter in self.guessed_letters else '-' for letter in self.word_to_guess)

    def update_hangman(self):
        """
        Update the hangman graphic by adding the next letter in 'HANGMAN'.
        """
        for i, char in enumerate(self.hangman):
            if char == '-':
                self.hangman = self.hangman[:i] + 'HANGMAN'[i] + self.hangman[i + 1:]
                break

    def handle_guess(self):
        """
        Handle the user's guess input, updating the game state accordingly.
        """
        guess = self.entry_guess.get().lower()  # Get the guess and convert to lowercase
        self.entry_guess.delete(0, tk.END)  # Clear the entry field

        # Validate input: ensure it's a single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please guess a single letter.")
            return

        # Check if the letter has already been guessed
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter. Try a different one.")
            return

        # Update guessed letters and hangman state
        if guess in self.word_to_guess:
            self.guessed_letters.append(guess)
        else:
            self.update_hangman()

        self.word_encoded = self.encode_word()  # Update encoded word
        self.update_ui()  # Refresh UI

        # Check for win or lose conditions
        if self.word_encoded == self.word_to_guess:
            messagebox.showinfo("Congratulations", "Great!!! You won!!!")
            self.reset_game()
        elif self.hangman == 'HANGMAN':
            messagebox.showinfo("Game Over", f'HANGMAN!!!\nYou lost. The word was "{self.word_to_guess}". Try again!')
            self.reset_game()

    def update_ui(self):
        """
        Update the UI components to reflect the current state of the game.
        """
        self.label_word.config(text=f"Word to guess: {self.word_encoded}")
        self.label_hangman.config(text=f"Hangman: {self.hangman}")

    def reset_game(self):
        """
        Reset the game state to start a new game.
        """
        self.word_to_guess = random.choice(self.word_list)  # Pick a new word
        self.guessed_letters = []  # Clear guessed letters
        self.hangman = '-------'  # Reset hangman progress
        self.word_encoded = self.encode_word()  # Re-encode the new word
        self.update_ui()  # Refresh UI


# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
