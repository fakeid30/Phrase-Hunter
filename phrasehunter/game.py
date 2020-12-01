from .phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.guesses = [" "]
        self.create_phrases(self.phrases)
        self.active_phrase = self.get_random_phrase()

    def create_phrases(self, phrases):
        phrase1 = Phrase("Hello World")
        phrase2 = Phrase("There is no Trying")
        phrase3 = Phrase("May The Force be With you")
        phrase4 = Phrase("You have to See the Matrix for yourself")
        phrase5 = Phrase("Life is like a box of Chocolates")
        phrases.append(phrase1)
        phrases.append(phrase2)
        phrases.append(phrase3)
        phrases.append(phrase4)
        phrases.append(phrase5)
        return self.phrases

    def get_random_phrase(self):
        import random
        ret = random.choice(self.phrases)
        return ret

    def welcome(self):
        print("""
        =================================
            Welcome to Phrase Hunter
        =================================
        """)

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
                self.get_guess(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
            elif self.active_phrase.check_complete(self.guesses):
                print(f"\nCongratulations you have won the game.\n")
                break

    def game_over(self):
        print("\nYou have lost the game")

    def get_guess(self, user_guess):
        self.guesses.append(user_guess)


