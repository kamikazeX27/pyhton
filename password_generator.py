import random
import string

class PasswordGenerator:
    def __init__(self, length, num_lower, num_upper, num_digits, num_special):
        self.length = length
        self.num_lower = num_lower
        self.num_upper = num_upper
        self.num_digits = num_digits
        self.num_special = num_special

    def generate_password(self):
        lowercase = ''.join(random.choices(string.ascii_lowercase, k=self.num_lower))
        uppercase = ''.join(random.choices(string.ascii_uppercase, k=self.num_upper))
        digits = ''.join(random.choices(string.digits, k=self.num_digits))
        special_chars = ''.join(random.choices(string.punctuation, k=self.num_special))

        all_chars = lowercase + uppercase + digits + special_chars

        # Si la somme des caractères générés est inférieure à la longueur souhaitée,
        # ajoutez des caractères aléatoires
        if len(all_chars) < self.length:
            additional_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=self.length - len(all_chars)))
            all_chars += additional_chars

        # Mélangez les caractères pour plus de sécurité
        password_list = list(all_chars)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password
