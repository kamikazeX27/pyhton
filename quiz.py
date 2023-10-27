# quiz.py
"""
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def jouer(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.afficher_question()
            reponse_utilisateur = input("Votre réponse (a, b, c) : ").lower()
            if question.verifier_reponse(reponse_utilisateur):
                print("Bonne réponse!\n")
                self.score += 1
            else:
                print("Mauvaise réponse.\n")
        self.afficher_resultats()

    def afficher_resultats(self):
        print(f"Score final : {self.score}/{len(self.questions)}")
        print("Voici les réponses correctes :")
        for i, question in enumerate(self.questions):
            print(f"{i + 1}. {question.text} Réponse correcte : {chr(ord('a') + question.reponses.index(next(filter(lambda x: x.is_correct, question.reponses)))}")

if __name__ == "__main__":
    from question import Question, Reponse

    questions = [
        Question("Quelle est la capitale de la France ?", [Reponse("a) Paris", True), Reponse("b) Madrid", False), Reponse("c) Berlin", False)]),
        # Ajoutez les autres questions ici
    ]

    quiz = Quiz(questions)
    quiz.jouer()
"""
import random
from question import Question

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def take_quiz(self):
        for question in self.questions:
            question.shuffle_options()
            print(question.text)
            for i, option in enumerate(question.options):
                print(f"{chr(97 + i)}. {option}")
            
            user_answer = input("Votre réponse (a/b/c) : ").lower()
            
            if question.is_correct(user_answer):
                print("Bonne réponse!\n")
                self.score += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte était {question.correct_answer}.\n")

    def display_score(self):
        print(f"Votre score final est de {self.score}/{len(self.questions)}")

    def display_answers(self):
        print("Réponses correctes :")
        for i, question in enumerate(self.questions):
            print(f"{i+1}. {question.text} - Réponse correcte : {question.correct_answer}")
