import math
import re

class Password:
    def __init__(self, password):
        self.password = password

    def calculate_entropy(self):
        # Calcul de l'entropie selon les critères de l'ANSSI
        length = len(self.password)
        uppercase = len(re.findall(r'[A-Z]', self.password))
        lowercase = len(re.findall(r'[a-z]', self.password))
        digits = len(re.findall(r'[0-9]', self.password))
        special = len(self.password) - uppercase - lowercase - digits
        character_set = 26 + 26 + 10 + 33  # Lettres majuscules, minuscules, chiffres et caractères spéciaux
        total_combinations = character_set ** length
        entropy = math.log2(total_combinations)

        return entropy

    def get_strength(self):
        entropy = self.calculate_entropy()
        if entropy < 28:
            return "Très faible"
        elif entropy < 36:
            return "Faible"
        elif entropy < 60:
            return "Moyenne"
        elif entropy < 128:
            return "Forte"
        else:
            return "Très forte"
