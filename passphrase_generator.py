import random
import wordlist  # on peut utiliser une liste de mots pour les passphrases

class PassphraseGenerator:
    def __init__(self, num_words):
        self.num_words = num_words

    def generate_passphrase(self):
        words = random.sample(wordlist.wordlist, self.num_words)
        passphrase = ' '.join(words)
        return passphrase
