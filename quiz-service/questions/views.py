from django.http import JsonResponse
from .models import Question
import random

def get_question_by_level(request, level):
    questions = list(Question.objects.filter(level=level))
    if not questions:
        return JsonResponse({"error": "No questions"}, status=404)
    q = random.choice(questions)
    return JsonResponse({
        "id": q.id,
        "text": q.text,
        "level": q.level,
        "correct_answer": q.correct_answer,
        "options": {
            "A": q.option_a,
            "B": q.option_b,
            "C": q.option_c,
            "D": q.option_d
        }
    })