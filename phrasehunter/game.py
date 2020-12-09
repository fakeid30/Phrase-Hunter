from .phrase import Phrase
import re
import sys


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.guesses = [" "]
        self.active_phrase = self.get_random_phrase()

    def create_phrases(self):
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
                        self.number_error_replay()

                    elif len(user_guess) > 1:
                        self.one_letter_error_replay()

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
                            self.active_phrase = self.get_random_phrase()
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

    def game_reset_zero(self, _input):
        _input = _input.lower()
        if _input == "yes":
            self.guesses = [" "]
            self.missed = 0
            self.start()
        else:
            print("\nExiting the game\n")
            sys.exit()

    def one_letter_error_replay(self):
        # ask = input("\nOoops! One letter at a time, please\n")
        #
        # while True:
        #     print(len(ask))
        #     if len(ask) == 1:
        #         break
        #     if re.match(r'[0-9]+', ask):
        #         self.number_error_replay()
        # self.get_guess(ask)
        ask = input("\nOoops! One letter at a time, please\n")
        if not re.match("^[A-Za-z]*$", ask):
            self.number_error_replay()
        else:
            if len(ask) > 1:
                self.one_letter_error_replay()
            elif len(ask) == 1:
                self.get_guess(ask)

    def number_error_replay(self):
        # replay = input("\nWoops! That was a number... not a letter\n")
        #
        # while True:
        #     if re.match("^[A-Za-z]*$", replay) and len(replay) < 2:
        #         break
        #     elif len(replay) > 1:
        #         self.one_letter_error_replay()
        # self.get_guess(replay)
        reply = input("\nWoops! That was a number... not a letter\n")

        if len(reply) > 1:
            self.one_letter_error_replay()
        else:
            if not re.match("^[A-Za-z]*$", reply):
                self.number_error_replay()
            elif re.match("^[A-Za-z]*$", reply):
                self.get_guess(reply)


## TODO
# Change number_error_Display
