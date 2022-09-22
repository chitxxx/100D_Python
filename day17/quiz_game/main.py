from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz_brain = QuizBrain(question_bank)

quiz_brain.run_quiz()