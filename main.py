from password import Password
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

# Exemple d'utilisation
user_password = input("Entrez un mot de passe à tester : ")
password_tester = Password(user_password)
strength = password_tester.get_strength()
print(f"Force du mot de passe : {strength}")

# Exemple de génération de mot de passe
generator = PasswordGenerator(length=12, num_lower=4, num_upper=2, num_digits=2, num_special=2)
generated_password = generator.generate_password()
print(f"Mot de passe généré : {generated_password}")

# Exemple de génération de passphrase
passphrase_generator = PassphraseGenerator(num_words=5)
generated_passphrase = passphrase_generator.generate_passphrase()
print(f"Passphrase générée : {generated_passphrase}")
