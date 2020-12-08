class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")

    def check_guess(self, guess):
        let = []
        for letters in self.phrase:
            let.append(letters)
        if guess in let:
            return True
        if guess not in let:
            return False
        raise ValueError

    def check_complete(self, guesses):
        let = []
        for letter in self.phrase:
            let.append(letter)
        # print(set(let))
        # print(guesses)
        if set(let) == set(guesses):
            return True
        return False
