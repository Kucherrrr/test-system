from django.test import TestCase
from .models import Question

class QuestionModelTest(TestCase):
    def test_create_question(self):
        q = Question.objects.create(
            text="Тест?",
            correct_answer="Да",
            option_a="Да", option_b="Нет", option_c="Мб", option_d="Нзн",
            level="easy"
        )
        self.assertEqual(q.text, "Тест?")
        self.assertEqual(q.level, "easy")
        self.assertEqual(q.correct_answer, "Да")