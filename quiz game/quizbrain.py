class QuizBrain:

    def __init__(self, question_list):
        self.questions = question_list
        self.question_number = 1
        self.score = 0

    def nextQuestion(self):
        """shows the next question and also takes input"""
        current_question = self.questions[self.question_number-1]
        answer = input(
            f"Q.{self.question_number} {current_question.text} (true/false) : ")

        self.checkAnswer(user_answer=answer,
                         question_answer=current_question.answer)

        self.question_number += 1

    def isStillHasQuestions(self):
        """checks the question number"""
        return self.question_number <= len(self.questions)

    def checkAnswer(self, user_answer, question_answer):
        """validate the answer and update the score"""
        if (question_answer.lower() == user_answer.lower()):
            print("You got it right!")
            self.score += 1

        else:
            print("Oops that was a wrong answer!")
            print(f"The right answer was {question_answer}")

        print(f"Your current score {self.score}/{self.question_number}")
        print("\n")

    def giveFeedback(self):
        """give the feedback to players depending upon their score"""
        print("Quiz Over")
        print(f"Your final score is {self.score}/{self.question_number}")

        if (self.score <= 3):
            print("Better luck next time!")
        elif (self.score <= 5):
            print("Good you are really trying hard!")
        elif (self.score <= 7):
            print("Great you are intelligent!")
        elif (self.score > 7 and self.score <= 9):
            print("Wonderfull you are a genius!")
        elif (self.score == 10):
            print("Unbelieveble you are genius keep going!")

import random

print(random.rand_int())