import html
from question import Question
from quizbrain import QuizBrain
import requests
import json


url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"


question_bank = []


def getQuestions():
    """fetch questions from api"""
    res = requests.get(url)
    return json.loads(res.text)["results"]


for question in getQuestions():
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))


quiz = QuizBrain(question_bank)

while quiz.isStillHasQuestions():
    quiz.nextQuestion()


quiz.giveFeedback()
