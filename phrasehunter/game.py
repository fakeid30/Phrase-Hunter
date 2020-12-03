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

    @staticmethod
    def welcome():
        print(
            """
        =================================
            Welcome to Phrase Hunter
        =================================
        """
        )

    def start(self):
        self.welcome()
        i = 0
        while int(i) < 1:
            try:
                if not self.active_phrase.check_complete(self.guesses):
                    if self.missed > 5:
                        self.game_over()
                        break
                    print(f"\nNumbers Missed: {self.missed}")
                    self.active_phrase.display(self.guesses)
                    user_guess = input("\nEnter a Letter: ")
                    user_guess = user_guess.lower()
                    if not re.match("^[A-Za-z]*$", user_guess):
                        print("\nOnly (A-Z) and (a-z) Allowed")
                        replay = input("\nDo you want to replay?\n")
                        self.error_replay(replay)
                    elif len(user_guess) > 1:
                        print("\nOnly one character allowed")
                        replay = input("\nDo you want to replay?\n")
                        self.error_replay(replay)
                    self.get_guess(user_guess)
                    if not self.active_phrase.check_guess(user_guess):
                        self.remove_guess()
                        self.missed += 1
                elif self.active_phrase.check_complete(self.guesses):
                    print("\nCongratulations you have won the game.\n")
                    ask = input("\nDo you want to replay this game?\n")
                    ask = ask.lower()
                    if ask == "yes":
                        again_ask = input(
                            "\nDo you want to play this game in a fresh state?\n"
                        )
                        again_ask = again_ask.lower()
                        if again_ask == "yes":
                            self.guesses = [" "]
                            self.missed = 0
                            self.start()
                        elif again_ask == "no":
                            self.guesses = [" "]
                            self.start()
                        else:
                            sys.exit()
                    else:
                        break
            except Exception as e:
                print(e)
                pass

    def game_over(self):
        print("\nYou have lost the game\n")
        ask = input("\nDo you wanna play again?\n")
        self.game_reset_zero(ask)

    def get_guess(self, user_guess):
        self.guesses.append(user_guess)

    def remove_guess(self):
        self.guesses.pop()

    def error_replay(self, input):
        input = input.lower()
        if input == "yes":
            self.guesses = [" "]
            self.missed = 0
            self.start()
        else:
            sys.exit()

    def game_reset_zero(self, input):
        input = input.lower()
        if input == "yes":
            self.guesses = [" "]
            self.missed = 0
            self.start()
        else:
            print("\nExiting the game\n")
            sys.exit()
