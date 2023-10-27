# à lancer
import random
from question import Question
from quiz import Quiz

# Les questions
questions = [
    Question("Quelle est la capitale de la France?", ["a) Paris", "b) Londres", "c) Berlin"], "a"),
    Question("Quel est le plus grand océan du monde?", ["a) Océan Atlantique", "b) Océan Indien", "c) Océan Pacifique"], "c"),
    Question("Combien de continents y a-t-il sur Terre?", ["a) 5", "b) 6", "c) 7"], "b"),
    Question("Qui a peint la Mona Lisa?", ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci"], "c"),
    Question("Quelle est la plus haute montagne du monde?", ["a) Mont Kilimandjaro", "b) Mont Everest", "c) Mont McKinley"], "b"),
    Question("Quel gaz compose la majeure partie de l'atmosphère terrestre?", ["a) Oxygène", "b) Azote", "c) Dioxyde de carbone"], "b"),
    Question("Quel élément chimique a le symbole 'H'?", ["a) Hydrogène", "b) Hélium", "c) Argon"], "a"),
    Question("Qui a écrit 'Romeo et Juliette'?", ["a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen"], "a"),
    Question("Quel est le symbole chimique de l'or?", ["a) Ag", "b) Au", "c) Cu"], "b"),
    Question("Quel pays est célèbre pour sa Grande Muraille?", ["a) Japon", "b) Chine", "c) Inde"], "b"),
    # Ajoute d'autres questions ici
]

# Crée le quiz
quiz = Quiz(questions)

# Mélangez les questions
random.shuffle(questions)

# Passe le quiz
quiz.take_quiz()

# Affichez le score final et les réponses correctes
quiz.display_score()
quiz.display_answers()
