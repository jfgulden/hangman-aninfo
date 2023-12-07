from user_statistics import UserStatistics
import random

CLUE_COST = 2

class ClueHandler:
    def __init__(self, some_score, some_basic_clues, some_hint_clues):
        self.score = some_score
        self.basic_clues = some_basic_clues
        self.hint_clues = some_hint_clues
        self.hint_used = False

    def from_stats(user_statistics):
        return ClueHandler(user_statistics.get_score(), user_statistics.get_basic_clues(), user_statistics.get_hint_clues())

    def get_score(self):
        return self.score

    def get_basic_clues(self):
        return self.basic_clues

    def get_hint_clues(self):
        return self.hint_clues

    def increase_score(self, amount):
        self.score += amount

    def decrease_score(self, amount):
        self.score -= amount

    def increase_basic_clues(self):
        self.basic_clues += 1

    def decrease_basic_clues(self):
        self.basic_clues -= 1

    def increase_hint_clues(self):
        self.hint_clues += 1

    def decrease_hint_clues(self):
        self.hint_clues -= 1

    def buy_basic_clue(self):
        if self.get_score() < CLUE_COST:
            print("\nNo tienes suficientes puntos para comprar una pista\n")
            return
        
        self.increase_basic_clues()
        self.decrease_score(CLUE_COST)
        print("\nCompraste una pista!\n")


    def use_basic_clue(self, letters_to_guess, letters_guessed):
        if len(letters_to_guess) <= 1:
            print("\nTe queda solo una letra, no podes usar la pista!\n")
            return

        if self.get_basic_clues() <= 0:
            print("\nNo tienes pistas para usar, compra mas y volve a intentar!\n")
            return

        clue = random.choice(letters_to_guess)
        letters_to_guess.remove(clue)
        letters_guessed.append(clue)
        self.decrease_basic_clues()

    def was_hint_used(self):
        return self.hint_used

    def buy_hint_clue(self):
        if self.get_score() < HINT_COST:
            print("\nNo tienes suficientes puntos para comprar una ayuda de palabra!\n")
            return
        
        self.increase_hint_clues()
        self.decrease_score(HINT_COST)
        print("\nCompraste una ayuda de palabra!\n")

    def use_hint_clue(self):
        if self.was_hint_used():
            print("\nYa te dimos una ayuda en esta partida!\n")
            return

        if self.get_hint_clues() <= 0:
            print("\nNo tienes ayudas para usar, compra mas y volve a intentar!\n")
            return

        print("\nAyuda obtenida\n")
        self.hint_used = True
        self.decrease_hint_clues()
            
    