from .phrase import Phrase
import re
import sys


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.guesses = [" "]
        self.create_phrases(self.phrases)
        self.active_phrase = self.get_random_phrase()

    def create_phrases(self, phrases):
        list_of_phrases = [
            "Hello World",
            "There is no Trying",
            "May The Force be With you",
            "You have to See the Matrix for yourself",
            "Life is like a box of Chocolates",
        ]
        self.phrases = [Phrase(items) for items in list_of_phrases]
        return self.phrases

    def get_random_phrase(self):
        import random

        ret = random.choice(self.phrases)
        return ret

    def welcome(self):
        print(
            """
        =================================
            Welcome to Phrase Hunter
        =================================
        """
        )

    def start(self):
        self.welcome()
        while True:
            if not self.active_phrase.check_complete(self.guesses):
                if self.missed > 5:
                    self.game_over()
                    break

                print(f"\nNumbers Missed: {self.missed}")
                self.active_phrase.display(self.guesses)
                user_guess = input("\nEnter a Letter: ")
                if not re.match("^[a-z]*$", user_guess):
                    print("\nOnly (a-z) Allowed")
                    sys.exit()
                elif len(user_guess) > 1:
                    print("\nOnly one character allowed")
                    sys.exit()
                self.get_guess(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
            elif self.active_phrase.check_complete(self.guesses):
                print("\nCongratulations you have won the game.\n")
                break

    def game_over(self):
        print("\nYou have lost the game")

    def get_guess(self, user_guess):
        self.guesses.append(user_guess)
