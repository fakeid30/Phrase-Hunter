class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print(f"_", end=" ")

    def check_guess(self, guess):
        let = []
        for letters in self.phrase:
            let.append(letters)
        if guess in let:
            return True
        else:
            return False

    def check_complete(self, guesses):
        # print("Check complete")
        let = []
        for letter in self.phrase:
            let.append(letter)
        if set(let) == set(guesses):
            return True
        else:

            return False



