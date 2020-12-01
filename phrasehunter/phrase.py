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
        return guess in let

    def check_complete(self, guesses):
        # print("Check complete")
        let = []
        for letter in self.phrase:
            let.append(letter)
        return set(let) == set(guesses)
