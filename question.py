# question.py
"""
class Reponse:
    def __init__(self, text, is_correct):
        self.text = text
        self.is_correct = is_correct

class Question:
    def __init__(self, text, reponses):
        self.text = text
        self.reponses = reponses

    def afficher_question(self):
        print(self.text)
        for i, reponse in enumerate(self.reponses):
            print(f"{chr(97 + i)}) {reponse.text}")

    def verifier_reponse(self, reponse_utilisateur):
        return self.reponses[ord(reponse_utilisateur) - ord('a')].is_correct
"""


import random

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer

    def shuffle_options(self):
        random.shuffle(self.options)
